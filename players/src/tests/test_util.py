import json
from django.test import TestCase
from django.db import DatabaseError
from django.http import JsonResponse
from src.util import (
    PlayerNotFoundError,
    PlayerServiceUtil,
    handle_view_errors,
    parse_json_body,
)
from src.models import Position
from src.tests.helpers import TestRequest


@handle_view_errors
def handle_errors_wrapper(exception=None):
    if exception:
        raise exception
    return JsonResponse({"message": "Success"}, status=200)


class UtilTest(TestCase):
    def test_parse_json_body(self):
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
        res = handle_errors_wrapper(ValueError("id must be positive"))
        self.assertEqual(
            json.loads(res.content.decode())["error"], "id must be positive"
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


class PlayerServiceUtilTest(TestCase):
    def test_validate_data_will_throw_when_id_not_positive(self):
        try:
            PlayerServiceUtil.validate_data(id=-1)
        except ValueError as e:
            self.assertRaises(ValueError)
            self.assertEqual(str(e), "id must be positive")

    def test_validate_data_will_throw_when_name_is_none(self):
        try:
            PlayerServiceUtil.validate_data(id=1, name=None)
        except ValueError as e:
            self.assertRaises(ValueError)
            self.assertEqual(str(e), "name must not be empty")

    def test_validate_data_will_throw_when_name_is_empty(self):
        try:
            PlayerServiceUtil.validate_data(id=1, name="")
        except ValueError as e:
            self.assertRaises(ValueError)
            self.assertEqual(str(e), "name must not be empty")

    def test_validate_data_will_throw_when_age_is_negative(self):
        try:
            PlayerServiceUtil.validate_data(id=1, name="Michael Yi", age=-1)
        except ValueError as e:
            self.assertRaises(ValueError)
            self.assertEqual(str(e), "age must be positive")

    def test_validate_data_will_throw_when_height_is_none(self):
        try:
            PlayerServiceUtil.validate_data(
                id=1, name="Michael Yi", age=19, height=None
            )
        except ValueError as e:
            self.assertRaises(ValueError)
            self.assertEqual(str(e), "height must not be empty")

    def test_validate_data_will_throw_when_height_is_empty(self):
        try:
            PlayerServiceUtil.validate_data(id=1, name="Michael Yi", age=19, height="")
        except ValueError as e:
            self.assertRaises(ValueError)
            self.assertEqual(str(e), "height must not be empty")

    def test_validate_data_will_throw_when_weight_is_negative(self):
        try:
            PlayerServiceUtil.validate_data(
                id=1, name="Michael Yi", age=19, height="5' 10\"", weight=-1
            )
        except ValueError as e:
            self.assertRaises(ValueError)
            self.assertEqual(str(e), "weight must be positive")

    def test_validate_data_will_throw_when_position_is_none(self):
        try:
            PlayerServiceUtil.validate_data(
                id=1,
                name="Michael Yi",
                age=19,
                height="5' 10\"",
                weight=140,
                position=None,
            )
        except ValueError as e:
            self.assertRaises(ValueError)
            self.assertEqual(str(e), "position must not be empty")

    def test_validate_data_will_throw_when_position_is_empty(self):
        try:
            PlayerServiceUtil.validate_data(
                id=1,
                name="Michael Yi",
                age=19,
                height="5' 10\"",
                weight=140,
                position="",
            )
        except ValueError as e:
            self.assertRaises(ValueError)
            self.assertEqual(str(e), "position must not be empty")

    def test_validate_data_will_throw_when_team_id_is_negative(self):
        try:
            PlayerServiceUtil.validate_data(
                id=1,
                name="Michael Yi",
                age=19,
                height="5' 10\"",
                weight=140,
                position="Shortstop",
                team_id=-1,
            )
        except ValueError as e:
            self.assertRaises(ValueError)
            self.assertEqual(str(e), "team_id must be positive")

    def test_validate_data_will_not_throw_when_data_is_valid(self):
        try:
            PlayerServiceUtil.validate_data(
                id=1,
                name="Michael Yi",
                age=19,
                height="5' 10\"",
                weight=140,
                position="Shortstop",
                team_id=1,
            )
        except:
            self.fail("validate_data should not throw an error")

    def test_validate_height_will_throw_when_height_is_invalid(self):
        try:
            PlayerServiceUtil.validate_height("5 10")
            PlayerServiceUtil.validate_height('5 10"')
            PlayerServiceUtil.validate_height("5' 10")
        except ValueError as e:
            self.assertRaises(ValueError)
            self.assertEqual(
                str(e), "Height must match the following pattern: <ft>'<in>\""
            )

    def test_validate_height_will_not_throw_when_height_is_valid(self):
        try:
            PlayerServiceUtil.validate_height("5' 10\"")
        except:
            self.fail("validate_height should not throw an error")
