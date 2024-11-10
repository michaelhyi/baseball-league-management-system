import datetime
from django.test import SimpleTestCase
from src.models import (
    Player,
    PlayerNotFoundError,
    Position,
    validate_data,
    validate_date,
    validate_height,
    validate_jersey_number,
)
from unittest.mock import MagicMock, call, patch


class PositionEnumTest(SimpleTestCase):
    def test_position_pitcher(self):
        position = Position.P
        self.assertEqual(position.__str__(), "Pitcher")

    def test_position_catcher(self):
        position = Position.C
        self.assertEqual(position.__str__(), "Catcher")

    def test_position_first_base(self):
        position = Position.FIRST_BASE
        self.assertEqual(position.__str__(), "First Base")

    def test_position_second_base(self):
        position = Position.SECOND_BASE
        self.assertEqual(position.__str__(), "Second Base")

    def test_position_third_base(self):
        position = Position.THIRD_BASE
        self.assertEqual(position.__str__(), "Third Base")

    def test_position_ss(self):
        position = Position.SS
        self.assertEqual(position.__str__(), "Shortstop")

    def test_position_left_field(self):
        position = Position.LF
        self.assertEqual(position.__str__(), "Left Field")

    def test_position_center_field(self):
        position = Position.CF
        self.assertEqual(position.__str__(), "Center Field")

    def test_position_right_field(self):
        position = Position.RF
        self.assertEqual(position.__str__(), "Right Field")

    def test_position_designated_hitter(self):
        position = Position.DH
        self.assertEqual(position.__str__(), "Designated Hitter")


class ModelsUtilTest(SimpleTestCase):
    def test_validate_data_will_throw_on_null(self):
        try:
            validate_data(name=None)
            self.fail("should have thrown value error")
        except ValueError as e:
            self.assertEqual(str(e), "name must not be null")

    def test_validate_data_will_throw_on_empty_str(self):
        try:
            validate_data(name="")
            self.fail("should have thrown value error")
        except ValueError as e:
            self.assertEqual(str(e), "name must not be empty")

    def test_validate_data_will_throw_on_negative_int(self):
        try:
            validate_data(id=-1)
            self.fail("should have thrown value error")
        except ValueError as e:
            self.assertEqual(str(e), "id must be positive")

    def test_validate_data_will_not_throw_on_valid_args(self):
        try:
            validate_data(
                id=1,
                name="Michael Yi",
                dob="2004-12-14",
                height="5' 10\"",
                weight=140,
                team_id=1,
            )
        except:
            self.fail("should not have thrown anything")

    def test_validate_date_will_throw_on_invalid_date(self):
        try:
            validate_date("2004-12-14T12:14:24Z")
            self.fail("should have thrown value error")
        except ValueError as e:
            self.assertEqual(
                str(e), "date must match the following pattern: YYYY-MM-DDTHH"
            )

    def test_validate_date_will_not_throw_on_valid_date(self):
        try:
            validate_date("2004-12-14")
        except:
            self.fail("should not have thrown anything")

    def test_validate_jersey_number_will_throw_when_jersey_number_is_longer_than_2_chars(
        self,
    ):
        try:
            validate_jersey_number("123")
            self.fail("should have thrown value error")
        except ValueError as e:
            self.assertEqual(str(e), "jersey number must contain 1-2 numeric digits")

    def test_validate_jersey_number_will_throw_when_jersey_number_contains_nonnumeric_chars(
        self,
    ):
        try:
            validate_jersey_number("-1")
            validate_jersey_number("#!")
            validate_jersey_number("ab")
        except ValueError as e:
            self.assertEqual(str(e), "jersey number must contain 1-2 numeric digits")

    def test_validate_jersey_number_will_not_throw_when_jersey_number_is_valid(self):
        try:
            validate_jersey_number("00")
            validate_jersey_number("1")
            validate_jersey_number("4")
            validate_jersey_number("14")
            validate_jersey_number("37")
            validate_jersey_number("99")
        except:
            self.fail("should not have thrown anything")

    def test_validate_height_will_throw_if_height_is_invalid_format(self):
        try:
            validate_height("170cm")
            validate_height("5' 10")
            validate_height('5 10"')
            validate_height("5 10")
        except ValueError as e:
            self.assertEqual(
                str(e), "height must match the following pattern: <ft>'<in>\""
            )

    def test_validate_height_will_not_throw_if_height_is_valid(self):
        try:
            validate_height("5' 10\"")
        except:
            self.fail("should not have thrown anything")


class PlayerModelTests(SimpleTestCase):
    def test_player_serialization(self):
        player = Player(
            1,
            "Michael Yi",
            "4",
            datetime.datetime(2004, 12, 14),
            19,
            "5' 10\"",
            140,
            Position.SS,
            1,
            datetime.datetime(2004, 12, 14),
            datetime.datetime(2004, 12, 14),
        )

        dict = player.serialize()

        self.assertEqual(dict["id"], 1)
        self.assertEqual(dict["name"], "Michael Yi")
        self.assertEqual(dict["jerseyNumber"], "#4")
        self.assertEqual(dict["dob"], "2004-12-14 00:00:00")
        self.assertEqual(dict["age"], 19)
        self.assertEqual(dict["height"], "5' 10\"")
        self.assertEqual(dict["weight"], 140)
        self.assertEqual(dict["position"], "Shortstop")
        self.assertEqual(dict["teamId"], 1)
        self.assertEqual(dict["createdAt"], "2004-12-14 00:00:00")
        self.assertEqual(dict["updatedAt"], "2004-12-14 00:00:00")

    def test_create(self):
        mock_cursor = MagicMock()
        mock_cursor.execute.return_value = None
        mock_cursor.fetchone.return_value = [1]
        mock_cursor.close.return_value = None

        player_id = Player.create(
            "Michael Yi", "4", "2004-12-14", "5' 10\"", 140, Position.SS, 1, mock_cursor
        )

        mock_cursor.execute.assert_has_calls(
            [
                call(
                    "INSERT INTO players (name, jersey_number, dob, height, weight, position, team_id) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    ["Michael Yi", "4", "2004-12-14", "5' 10\"", 140, "Shortstop", 1],
                ),
                call("SELECT LAST_INSERT_ID() AS id"),
            ]
        )

        self.assertEqual(player_id, 1)

    def test_get(self):
        mock_cursor = MagicMock()
        mock_cursor.execute.return_value = None
        mock_cursor.fetchone.return_value = (
            1,
            "Michael Yi",
            "4",
            "2004-12-14",
            19,
            "5' 10\"",
            140,
            "Shortstop",
            1,
            "2004-12-14",
            "2004-12-14",
        )
        mock_cursor.description = [
            ["id"],
            ["name"],
            ["jersey_number"],
            ["dob"],
            ["age"],
            ["height"],
            ["weight"],
            ["position"],
            ["team_id"],
            ["created_at"],
            ["updated_at"],
        ]
        mock_cursor.close.return_value = None

        player = Player.get(1, mock_cursor)

        mock_cursor.execute.assert_called_once_with(
            "SELECT *, TIMESTAMPDIFF(YEAR, dob, CURDATE()) AS age FROM players WHERE id = %s LIMIT 1",
            [1],
        )

        self.assertEqual(player.id, 1)
        self.assertEqual(player.name, "Michael Yi")
        self.assertEqual(player.jersey_number, "4")
        self.assertEqual(player.dob, "2004-12-14")
        self.assertEqual(player.age, 19)
        self.assertEqual(player.height, "5' 10\"")
        self.assertEqual(player.weight, 140)
        self.assertEqual(player.position, "Shortstop")
        self.assertEqual(player.team_id, 1)
        self.assertEqual(player.created_at, "2004-12-14")
        self.assertEqual(player.updated_at, "2004-12-14")

    def test_get_will_throw_if_player_not_found(self):
        mock_cursor = MagicMock()
        mock_cursor.execute.return_value = None
        mock_cursor.fetchone.return_value = None
        mock_cursor.description = [
            ["id"],
            ["name"],
            ["jersey_number"],
            ["dob"],
            ["age"],
            ["height"],
            ["weight"],
            ["position"],
            ["team_id"],
            ["created_at"],
            ["updated_at"],
        ]
        mock_cursor.close.return_value = None

        try:
            Player.get(1, mock_cursor)

            mock_cursor.execute.assert_called_once_with(
                "SELECT *, TIMESTAMPDIFF(YEAR, dob, CURDATE()) AS age FROM players WHERE id = %s LIMIT 1",
                [1],
            )

            self.fail("should have thrown playernotfounderror")
        except PlayerNotFoundError as e:
            self.assertEqual(str(e), "player not found")

    def test_update(self):
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = (
            1,
            "Michael Yi",
            "4",
            "2004-12-14",
            19,
            "5' 10\"",
            140,
            "Shortstop",
            1,
            "2004-12-14",
            "2004-12-14",
        )
        mock_cursor.description = [
            ["id"],
            ["name"],
            ["jersey_number"],
            ["dob"],
            ["age"],
            ["height"],
            ["weight"],
            ["position"],
            ["team_id"],
            ["created_at"],
            ["updated_at"],
        ]
        mock_cursor.execute.return_value = None
        mock_cursor.close.return_value = None

        Player.update(
            1,
            "Michael Yi",
            "4",
            "2004-12-14",
            "5' 10\"",
            140,
            Position.SS,
            1,
            mock_cursor,
        )

        mock_cursor.execute.assert_has_calls(
            [
                call(
                    "SELECT *, TIMESTAMPDIFF(YEAR, dob, CURDATE()) AS age FROM players WHERE id = %s LIMIT 1",
                    [1],
                ),
                call(
                    "UPDATE players SET name = %s, jersey_number = %s, dob = %s, height = %s, weight = %s, position = %s, team_id = %s WHERE id = %s",
                    [
                        "Michael Yi",
                        "4",
                        "2004-12-14",
                        "5' 10\"",
                        140,
                        "Shortstop",
                        1,
                        1,
                    ],
                ),
            ]
        )

    def test_delete(self):
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = (
            1,
            "Michael Yi",
            "4",
            "2004-12-14",
            19,
            "5' 10\"",
            140,
            "Shortstop",
            1,
            "2004-12-14",
            "2004-12-14",
        )
        mock_cursor.description = [
            ["id"],
            ["name"],
            ["jersey_number"],
            ["dob"],
            ["age"],
            ["height"],
            ["weight"],
            ["position"],
            ["team_id"],
            ["created_at"],
            ["updated_at"],
        ]
        mock_cursor.execute.return_value = None
        mock_cursor.close.return_value = None

        Player.delete(1, mock_cursor)

        mock_cursor.execute.assert_has_calls(
            [
                call(
                    "SELECT *, TIMESTAMPDIFF(YEAR, dob, CURDATE()) AS age FROM players WHERE id = %s LIMIT 1",
                    [1],
                ),
                call("DELETE FROM players WHERE id = %s", [1]),
            ]
        )
