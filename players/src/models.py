import json
import re
from typing import Optional
from enum import Enum
from datetime import datetime

from django.db import connection, DatabaseError

# TODO: avoid explicit error handling, let it bubble through to views
# TODO: simplify serialization (Django's model_to_dict)?
# TODO: enum usage (use Django Models?)
# TODO: use Django ORM vs. SQL Injection?

class PlayerNotFoundError(Exception):
    pass


class Position(Enum):
    P = "Pitcher"
    C = "Catcher"
    FIRST_BASE = "First Base"
    SECOND_BASE = "Second Base"
    THIRD_BASE = "Third Base"
    SS = "Shortstop"
    LF = "Left Field"
    CF = "Center Field"
    RF = "Right Field"
    DH = "Designated Hitter"

    def __str__(self):
        return self.value


def validate_data(**kwargs):
    for key, value in kwargs.items():
        if isinstance(value, str) and (value is None or len(value) == 0):
            raise ValueError(f"{key} must not be empty")
        if isinstance(value, int) and value <= 0:
            raise ValueError(f"{key} must be positive")


height_pattern = r"^(?:(\d{1,2})'(\d{1,2})\"|\d{1,2}'\s*\d{1,2}\s*\"|(?:(\d{1,2})\s*feet\s*(\d{1,2})\s*inches))$"


def validate_height(height):
    if not re.match(height_pattern, height):
        raise ValueError("Height must match the following pattern: <ft>'<in>\"")


class Player:
    def __init__(
        self,
        id: Optional[int],
        name: str,
        age: int,
        height: str,
        weight: int,
        position: Position,
        team_id: int,
        created_at: Optional[datetime],
        updated_at: Optional[datetime],
    ):
        self.id = id
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.position = position
        self.team_id = team_id
        self.created_at = created_at
        self.updated_at = updated_at

    def serialize(self):
        return json.dumps(
            {
                "id": self.id,
                "name": self.name,
                "age": self.age,
                "height": self.height,
                "weight": self.weight,
                "position": self.position.__str__(),
                "teamId": self.team_id,
                "createdAt": self.created_at,
                "updatedAt": self.updated_at,
            },
            default=str,
        )

    @staticmethod
    def create(
        name: str, age: int, height: str, weight: int, position: Position, team_id: int
    ):
        try:
            validate_data(
                name=name, age=age, height=height, weight=weight, team_id=team_id
            )
            validate_height(height)
        except ValueError as e:
            raise e

        player = Player(None, name, age, height, weight, position, team_id, None, None)

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
    def get(id: int) -> "Player":
        try:
            validate_data(id=id)
        except ValueError as e:
            raise e

        sql = "SELECT * FROM player WHERE id = %s LIMIT 1"

        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, [id])
                row = cursor.fetchone()
                if row:
                    return Player(*row)
        except DatabaseError as e:
            raise e

        raise PlayerNotFoundError("Player not found")

    @staticmethod
    def update(
        id: int,
        name: str,
        age: int,
        height: str,
        weight: int,
        position: Position,
        team_id: int,
    ):
        try:
            validate_data(
                id=id, name=name, age=age, height=height, weight=weight, team_id=team_id
            )
            validate_height(height)
        except ValueError as e:
            raise e

        try:
            Player.get(id)
        except PlayerNotFoundError as e:
            raise e

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
                        name,
                        age,
                        height,
                        weight,
                        position.value,
                        team_id,
                        id,
                    ),
                )
        except DatabaseError as e:
            raise e

    @staticmethod
    def delete(id: int):
        try:
            validate_data(id=id)
        except ValueError as e:
            raise e

        try:
            Player.get(id)
        except PlayerNotFoundError as e:
            raise e

        sql = "DELETE FROM player WHERE id = %s"

        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, [id])
        except DatabaseError as e:
            raise e
