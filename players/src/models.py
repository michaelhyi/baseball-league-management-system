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

    @classmethod
    def choices(cls):
        return [(key.name, key.value) for key in cls]


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
        query = """
        INSERT INTO player (name, age, height, weight, position, team_id)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    query,
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
        query = """
        SELECT id, name, age, height, weight, position, team_id
        FROM player
        WHERE id = %s
        """

        try:
            with connection.cursor() as cursor:
                cursor.execute(query, [id])
                row = cursor.fetchone()
                if row:
                    return Player(*row)
                return None
        except DatabaseError as e:
            raise e

    @staticmethod
    def update(player: Player):
        query = """
        UPDATE player
        SET name = %s, age = %s, height = %s, weight = %s, position = %s, team_id = %s
        WHERE id = %s
        """

        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    query,
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
        query = """
        DELETE FROM player WHERE id = %s
        """

        try:
            with connection.cursor() as cursor:
                cursor.execute(query, [id])

        except DatabaseError as e:
            raise e


class PlayerNotFoundError(Exception):
    pass


height_pattern = r"^(?:(\d{1,2})'(\d{1,2})\"|\d{1,2}'\s*\d{1,2}\s*\"|(?:(\d{1,2})\s*feet\s*(\d{1,2})\s*inches))$"


class PlayerService:
    @staticmethod
    def create_player(
        name: str, age: int, height: str, weight: int, position: Position, team_id: int
    ):
        if name is None or len(name) == 0:
            raise ValueError("Name must not be empty")

        if age <= 0:
            raise ValueError("Age must be positive")

        if height is None or len(height) == 0:
            raise ValueError("Height must not be empty")

        if not re.match(height_pattern, height):
            raise ValueError("Height must match the following pattern: <ft>'<in>\"")

        if weight <= 0:
            raise ValueError("Weight must be positive")

        if team_id <= 0:
            raise ValueError("Team ID must be positive")

        player = Player(None, name, age, height, weight, position, team_id)

        try:
            PlayerDao.create(player)
        except DatabaseError as e:
            raise e

    @staticmethod
    def get_player(id: int) -> Player:
        if id <= 0:
            raise ValueError("ID must be positive")

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
        if id <= 0:
            raise ValueError("ID must be positive")

        if name is None or len(name) == 0:
            raise ValueError("Name must not be empty")

        if age <= 0:
            raise ValueError("Age must be positive")

        if height is None or len(height) == 0:
            raise ValueError("Height must not be empty")

        if not re.match(height_pattern, height):
            raise ValueError("Height must match the following pattern: <ft>'<in>\"")

        if weight <= 0:
            raise ValueError("Weight must be positive")

        if team_id <= 0:
            raise ValueError("Team ID must be positive")

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
        if id <= 0:
            raise ValueError("ID must be positive")

        player = PlayerService.get_player(id)

        if player is None:
            raise PlayerNotFoundError("Player not found")

        try:
            PlayerDao.delete(id)
        except DatabaseError as e:
            raise e
