from django.test import TestCase
from src.models import Player, Position


class PositionTests(TestCase):
    def test_position_str(self):
        pitcher = Position.P
        self.assertEqual(str(pitcher), "Pitcher")

        catcher = Position.C
        self.assertEqual(str(catcher), "Catcher")

        first_base = Position.FIRST_BASE
        self.assertEqual(str(first_base), "First Base")

        second_base = Position.SECOND_BASE
        self.assertEqual(str(second_base), "Second Base")

        third_base = Position.THIRD_BASE
        self.assertEqual(str(third_base), "Third Base")

        short_stop = Position.SS
        self.assertEqual(str(short_stop), "Shortstop")

        left_field = Position.LF
        self.assertEqual(str(left_field), "Left Field")

        center_field = Position.CF
        self.assertEqual(str(center_field), "Center Field")

        right_field = Position.RF
        self.assertEqual(str(right_field), "Right Field")

        designated_hitter = Position.DH
        self.assertEqual(str(designated_hitter), "Designated Hitter")


class PlayerTests(TestCase):
    def test_player_serialize(self):
        player = Player(
            id=1,
            name="Michael Yi",
            age=19,
            height="5' 10\"",
            weight=140,
            position=Position.SS,
            team_id=1,
        )
        self.assertEqual(
            player.serialize(),
            '{"id": 1, "name": "Michael Yi", "age": 19, "height": "5\' 10\\"", "weight": 140, "position": "Shortstop", "teamId": 1}',
        )
