from unittest.mock import MagicMock, patch
from django.test import TestCase
from src.models import Player, Position
from src.service import PlayerService


class PlayerServiceTests(TestCase):
    @patch("src.util.PlayerServiceUtil")
    @patch("src.dao.PlayerDao")
    def test_create_player_will_throw_if_data_validation_fails(self, mockDao, mock):
        mock.validate_data.return_value.raiseError.side_effect = ValueError(
            "id must be positive"
        )

        with self.assertRaises(ValueError) as e:
            PlayerService.create_player(
                "Michael Yi", -1, "5' 10\"", 140, Position.SS, 1
            )

            self.assertEqual(str(e.exception), "age must be positive")
            mock.validate_data.assert_called_once_with(
                "Michael Yi", -1, "5' 10\"", 140, Position.SS, 1
            )
            mock.validate_height.assert_not_called()
            mockDao.assert_not_called()

    @patch("src.util.PlayerServiceUtil")
    @patch("src.dao.PlayerDao")
    def test_create_player_will_throw_if_height_validation_fails(self, mockDao, mock):
        mock.validate_data.return_value = None
        mock.validate_height.return_value.raiseError.side_effect = ValueError(
            "Height must match the following pattern: <ft>'<in>\""
        )

        with self.assertRaises(ValueError) as e:
            PlayerService.create_player("Michael Yi", 19, "5 10", 140, Position.SS, 1)

            self.assertEqual(
                str(e.exception), "Height must match the following pattern: <ft>'<in>\""
            )
            mock.validate_data.assert_called_once_with(
                "Michael Yi", 19, "5 10", 140, Position.SS, 1
            )
            mock.validate_height.assert_called_once_with("5 10")
            mockDao.assert_not_called()

    # @patch("src.util.PlayerServiceUtil")
    # @patch("src.dao.PlayerDao")
    # def test_create_player(self, mock_dao, mock_util):
    #     mock_dao_instance = MagicMock()
    #
    #     mock_util.validate_data.return_value = None
    #     mock_util.validate_height.return_value = None
    #     mock_dao.return_value = mock_dao_instance
    #
    #     PlayerService.create_player("Michael Yi", 19, "5' 10\"", 140, Position.SS, 1)
    #
    #     mock_util.validate_data.assert_called_once_with(
    #         "Michael Yi", 19, "5' 10\"", 140, Position.SS, 1
    #     )
    #     mock_util.validate_height.assert_called_once_with("5' 10\"")
    #
    #     mock_dao_instance.create.assert_called_once_with(
    #         Player(None, "Michael Yi", 19, "5' 10\"", 140, Position.SS, 1)
    #     )
