from src.models import Player, Position
from src.util import PlayerServiceUtil, PlayerNotFoundError
from src.dao import PlayerDao
from django.db import DatabaseError


class PlayerService:
    @staticmethod
    def create_player(
        name: str, age: int, height: str, weight: int, position: Position, team_id: int
    ):
        try:
            PlayerServiceUtil.validate_data(
                name=name, age=age, height=height, weight=weight, team_id=team_id
            )
            PlayerServiceUtil.validate_height(height)
        except ValueError as e:
            raise e

        player = Player(None, name, age, height, weight, position, team_id)

        try:
            PlayerDao.create(player)
        except DatabaseError as e:
            raise e

    @staticmethod
    def get_player(id: int) -> Player:
        try:
            PlayerServiceUtil.validate_data(id=id)
        except ValueError as e:
            raise e

        try:
            player = PlayerDao.get(id)

            if player is None:
                raise PlayerNotFoundError("Player not found")

            return player
        except DatabaseError as e:
            raise e

    @staticmethod
    def update_player(
        id: int,
        name: str,
        age: int,
        height: str,
        weight: int,
        position: Position,
        team_id: int,
    ):
        try:
            PlayerServiceUtil.validate_data(
                id=id, name=name, age=age, height=height, weight=weight, team_id=team_id
            )
            PlayerServiceUtil.validate_height(height)
        except ValueError as e:
            raise e

        player = PlayerService.get_player(id)

        if player is None:
            raise PlayerNotFoundError("Player not found")

        player = Player(id, name, age, height, weight, position, team_id)

        try:
            PlayerDao.update(player)
        except DatabaseError as e:
            raise e

    @staticmethod
    def delete_player(id: int):
        try:
            PlayerServiceUtil.validate_data(id=id)
        except ValueError as e:
            raise e

        player = PlayerService.get_player(id)

        if player is None:
            raise PlayerNotFoundError("Player not found")

        try:
            PlayerDao.delete(id)
        except DatabaseError as e:
            raise e
