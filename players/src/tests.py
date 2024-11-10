from django.test import SimpleTestCase
from src.models import (
    Position,
    validate_data,
    validate_date,
    validate_height,
    validate_jersey_number,
)


class PositionTest(SimpleTestCase):
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
