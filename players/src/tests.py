import json
from unittest.mock import patch
from django.http import JsonResponse
from django.test import TestCase

from src.models import DatabaseError, PlayerNotFoundError, Position
from src.views import create_player, handle_errors, parse_body


class TestRequest:
    def __init__(self, body: str, method: str):
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

        request = TestRequest(json.dumps(player), "POST")

        name, age, height, weight, position, team_id = parse_body(request)

        self.assertEqual(name, "Michael Yi")
        self.assertEqual(age, 19)
        self.assertEqual(height, "5' 10\"")
        self.assertEqual(weight, 140)
        self.assertEqual(position, Position.SS)
        self.assertEqual(team_id, 1)

    def test_handle_value_error(self):
        res = handle_errors_wrapper(ValueError("ID must be positive"))
        self.assertEqual(
            json.loads(res.content.decode())["error"], "ID must be positive"
        )
        self.assertEqual(res.status_code, 400)

    # TODO: key error value
    def test_handle_key_error(self):
        res = handle_errors_wrapper(KeyError("ID must be positive"))
        self.assertEqual(
            json.loads(res.content.decode())["error"], "ID must be positive"
        )
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

        req = TestRequest(json.dumps(player), "POST")
        res = create_player(req)

        mock_service.create_player.assert_called_once_with(
            "Michael Yi", 19, "5' 10\"", 140, Position.SS, 1
        )

        self.assertEqual(json.loads(res.content.decode())["message"], "Player created")
        self.assertEqual(res.status_code, 201)
