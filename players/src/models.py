from typing import Optional
from django.db import DatabaseError, connection
from enum import Enum
from dataclasses import dataclass
import re


class Position(Enum):
    P = "Pitcher"
    C = "Catcher"
    FIRST_B = "First Base"
    SECOND_B = "Second Base"
    THIRD_B = "Third Base"
    SS = "Shortstop"
    LF = "Left Field"
    CF = "Center Field"
    RF = "Right Field"
    DH = "Designated Hitter"


@dataclass
class Player:
    id: Optional[int]
    name: str
    age: int
    height: str
    weight: int
    position: Position
    team_id: int


class PlayerDao:
    @staticmethod
    def create(player: Player):
        sql = """
        INSERT INTO player (name, age, height, weight, position, team_id)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    sql,
                    (
                        player.name,
                        player.age,
                        player.height,
                        player.weight,
                        player.position.value,
                        player.team_id,
                    ),
                )
        except DatabaseError as e:
            raise e

    @staticmethod
    def get(id: int) -> Optional[Player]:
        sql = """
        SELECT id, name, age, height, weight, position, team_id
        FROM player
        WHERE id = %s
        """

        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, [id])
                row = cursor.fetchone()
                if row:
                    return Player(*row)
                return None
        except DatabaseError as e:
            raise e

    @staticmethod
    def update(player: Player):
        sql = """
        UPDATE player
        SET name = %s, age = %s, height = %s, weight = %s, position = %s, team_id = %s
        WHERE id = %s
        """

        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    sql,
                    (
                        player.name,
                        player.age,
                        player.height,
                        player.weight,
                        player.position.value,
                        player.team_id,
                        player.id,
                    ),
                )
        except DatabaseError as e:
            raise e

    @staticmethod
    def delete(id: int):
        sql = """
        DELETE FROM player WHERE id = %s
        """

        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, [id])
        except DatabaseError as e:
            raise e


class PlayerNotFoundError(Exception):
    pass


height_pattern = r"^(?:(\d{1,2})'(\d{1,2})\"|\d{1,2}'\s*\d{1,2}\s*\"|(?:(\d{1,2})\s*feet\s*(\d{1,2})\s*inches))$"


class PlayerServiceUtil:
    @staticmethod
    def validate_data(**kwargs):
        for key, value in kwargs:
            if type(value) is str and (value is None or len(value) == 0):
                raise ValueError(f"{key} must not be empty")
            if type(value) is int and value <= 0:
                raise ValueError(f"{key} must be positive")

    @staticmethod
    def validate_height(height):
        if not re.match(height_pattern, height):
            raise ValueError("Height must match the following pattern: <ft>'<in>\"")


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
