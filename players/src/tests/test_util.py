import json
from django.test import TestCase
from django.db import DatabaseError
from django.http import JsonResponse
from src.util import PlayerNotFoundError, handle_view_errors, parse_json_body
from src.models import Position
from src.tests.helpers import TestRequest


@handle_view_errors
def handle_errors_wrapper(exception=None):
    if exception:
        raise exception
    return JsonResponse({"message": "Success"}, status=200)


class UtilTest(TestCase):
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

        name, age, height, weight, position, team_id = parse_json_body(request)

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
