import json
from typing import Optional
from unittest.mock import patch
from django.http import JsonResponse
from django.test import TestCase

from src.models import DatabaseError, Player, PlayerNotFoundError, Position
from src.views import (
    create_player,
    delete_player,
    get_player,
    handle_errors,
    parse_body,
    player_view,
    update_player,
)


class TestRequest:
    def __init__(self, path: str, body: Optional[str], method: str):
        self.path = path
        self.body = body
        self.method = method


@handle_errors
def handle_errors_wrapper(exception=None):
    if exception:
        raise exception
    return JsonResponse({"message": "Success"}, status=200)


class ViewsTest(TestCase):
    def test_parse_body(self):
        player = {
            "name": "Michael Yi",
            "age": 19,
            "height": "5' 10\"",
            "weight": 140,
            "position": "Shortstop",
            "teamId": 1,
        }

        request = TestRequest("v1/players/", json.dumps(player), "POST")

        name, age, height, weight, position, team_id = parse_body(request)

        self.assertEqual(name, "Michael Yi")
        self.assertEqual(age, 19)
        self.assertEqual(height, "5' 10\"")
        self.assertEqual(weight, 140)
        self.assertEqual(position, Position.SS)
        self.assertEqual(team_id, 1)

    def test_handle_success(self):
        res = handle_errors_wrapper()
        self.assertEqual(json.loads(res.content.decode())["message"], "Success")
        self.assertEqual(res.status_code, 200)

    def test_handle_value_error(self):
        res = handle_errors_wrapper(ValueError("ID must be positive"))
        self.assertEqual(
            json.loads(res.content.decode())["error"], "ID must be positive"
        )
        self.assertEqual(res.status_code, 400)

    # TODO: key error value
    def test_handle_key_error(self):
        res = handle_errors_wrapper(KeyError("id"))
        self.assertEqual(json.loads(res.content.decode())["error"], "'id'")
        self.assertEqual(res.status_code, 400)

    def test_handle_player_not_found_error(self):
        res = handle_errors_wrapper(PlayerNotFoundError("Player not found"))
        self.assertEqual(json.loads(res.content.decode())["error"], "Player not found")
        self.assertEqual(res.status_code, 404)

    def test_handle_database_error(self):
        res = handle_errors_wrapper(DatabaseError("Table `` not found"))
        self.assertEqual(
            json.loads(res.content.decode())["error"], "Internal server error"
        )
        self.assertEqual(res.status_code, 500)

    @patch("src.views.PlayerService")
    def test_create_player(self, mock_service):
        mock_service.create_player.return_value = None

        player = {
            "name": "Michael Yi",
            "age": 19,
            "height": "5' 10\"",
            "weight": 140,
            "position": "Shortstop",
            "teamId": 1,
        }

        req = TestRequest("v1/players/", json.dumps(player), "POST")
        res = create_player(req)

        mock_service.create_player.assert_called_once_with(
            "Michael Yi", 19, "5' 10\"", 140, Position.SS, 1
        )

        self.assertEqual(json.loads(res.content.decode())["message"], "Player created")
        self.assertEqual(res.status_code, 201)

    @patch("src.views.PlayerService")
    def test_create_player_method_not_allowed_when_method_is_not_post(
        self, mock_service
    ):
        mock_service.create_player.return_value = None

        player = {
            "name": "Michael Yi",
            "age": 19,
            "height": "5' 10\"",
            "weight": 140,
            "position": "Shortstop",
            "teamId": 1,
        }

        req = TestRequest("v1/players/1/", json.dumps(player), "GET")
        res = create_player(req)

        mock_service.create_player.assert_not_called()

        self.assertEqual(res.status_code, 405)

    @patch("src.views.get_player")
    def test_player_view_get_player(self, mock):
        mock.return_value = JsonResponse({"player": "Player"}, status=200)

        req = TestRequest("v1/players/1", None, "GET")
        res = player_view(req, 1)

        mock.assert_called_once_with(req, 1)
        self.assertEqual(json.loads(res.content.decode())["player"], "Player")
        self.assertEqual(res.status_code, 200)

    @patch("src.views.update_player")
    def test_player_view_update_player(self, mock):
        mock.return_value = JsonResponse({"message": "Player updated"}, status=200)

        req = TestRequest("v1/players/1", None, "PATCH")
        res = player_view(req, 1)

        mock.assert_called_once_with(req, 1)
        self.assertEqual(json.loads(res.content.decode())["message"], "Player updated")
        self.assertEqual(res.status_code, 200)

    @patch("src.views.delete_player")
    def test_player_view_delete_player(self, mock):
        mock.return_value = JsonResponse({"message": "Player deleted"}, status=200)

        req = TestRequest("v1/players/1", None, "DELETE")
        res = player_view(req, 1)

        mock.assert_called_once_with(req, 1)
        self.assertEqual(json.loads(res.content.decode())["message"], "Player deleted")
        self.assertEqual(res.status_code, 200)

    @patch("src.views.get_player")
    @patch("src.views.update_player")
    @patch("src.views.delete_player")
    def test_player_view_method_not_allowed(
        self, mock_get_player, mock_update_player, mock_delete_player
    ):
        req = TestRequest("v1/players/1", None, "POST")
        res = player_view(req, 1)

        mock_get_player.assert_not_called()
        mock_update_player.assert_not_called()
        mock_delete_player.assert_not_called()
        self.assertEqual(res.status_code, 405)

    @patch("src.views.PlayerService")
    def test_get_player(self, mock_service):
        mock_service.get_player.return_value = Player(
            1, "Michael Yi", 19, "5' 10\"", 140, Position.SS, 1
        )

        req = TestRequest("v1/players/1", None, "GET")
        res = get_player(req, 1)

        mock_service.get_player.assert_called_once_with(1)

        self.assertEqual(
            json.loads(res.content.decode())["player"],
            json.dumps(
                {
                    "id": 1,
                    "name": "Michael Yi",
                    "age": 19,
                    "height": "5' 10\"",
                    "weight": 140,
                    "position": "Shortstop",
                    "teamId": 1,
                }
            ),
        )
        self.assertEqual(res.status_code, 200)

    @patch("src.views.PlayerService")
    def test_update_player(self, mock_service):
        mock_service.update_player.return_value = None
        player = {
            "name": "Michael Yi",
            "age": 19,
            "height": "5' 10\"",
            "weight": 140,
            "position": "Shortstop",
            "teamId": 1,
        }

        req = TestRequest("v1/players/1", json.dumps(player), "PATCH")
        res = update_player(req, 1)

        mock_service.update_player.assert_called_once_with(
            1, "Michael Yi", 19, "5' 10\"", 140, Position.SS, 1
        )

        self.assertEqual(json.loads(res.content.decode())["message"], "Player updated")
        self.assertEqual(res.status_code, 200)

    @patch("src.views.PlayerService")
    def test_delete_player(self, mock_service):
        mock_service.delete_player.return_value = None

        req = TestRequest("v1/players/1", None, "DELETE")
        res = delete_player(req, 1)

        mock_service.delete_player.assert_called_once_with(1)
        self.assertEqual(json.loads(res.content.decode())["message"], "Player deleted")
        self.assertEqual(res.status_code, 200)
