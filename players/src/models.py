import re
import logging
from enum import Enum

from django.db import connection, DatabaseError

logging.basicConfig(level=logging.INFO)

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


date_pattern = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"
height_pattern = r"^(?:(\d{1,2})'(\d{1,2})\"|\d{1,2}'\s*\d{1,2}\s*\"|(?:(\d{1,2})\s*feet\s*(\d{1,2})\s*inches))$"


def validate_date(date):
    if not re.match(date_pattern, date):
        raise ValueError("date must match the following pattern: YYYY-MM-DDTHH")


def validate_height(height):
    if not re.match(height_pattern, height):
        raise ValueError("Height must match the following pattern: <ft>'<in>\"")


class Player:
    def __init__(self, **kwargs):
        self.id = kwargs["id"]
        self.name = kwargs["name"]
        self.dob = kwargs["dob"]
        self.age = kwargs["age"]
        self.height = kwargs["height"]
        self.weight = kwargs["weight"]
        self.position = kwargs["position"]
        self.team_id = kwargs["team_id"]
        self.created_at = kwargs["created_at"]
        self.updated_at = kwargs["updated_at"]

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "dob": str(self.dob),
            "age": self.age,
            "height": self.height,
            "weight": self.weight,
            "position": self.position.__str__(),
            "teamId": self.team_id,
            "createdAt": str(self.created_at),
            "updatedAt": str(self.updated_at),
        }

    @staticmethod
    def create(
        name: str, dob: str, height: str, weight: int, position: Position, team_id: int
    ):
        logging.info(
            f"Creating player with name {name}, dob {dob}, height {height}, weight {weight}, position {position}, and team_id {team_id}"
        )

        try:
            validate_data(
                name=name, dob=dob, height=height, weight=weight, team_id=team_id
            )
            validate_height(height)
        except ValueError as e:
            raise e

        sql = """
        INSERT INTO players (name, dob, height, weight, position, team_id)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    sql,
                    (
                        name,
                        dob,
                        height,
                        weight,
                        position.value,
                        team_id,
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

        sql = "SELECT *, TIMESTAMPDIFF(YEAR, dob, CURDATE()) AS age FROM players WHERE id = %s LIMIT 1"

        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, [id])
                row = cursor.fetchone()

                logging.info(f"Fetched row: {row}")

                columns = [col[0] for col in cursor.description]
                row_as_dict = dict(zip(columns, row))

                logging.info(f"row as dict: {row_as_dict}")

                # TODO: feels unsafe. gotta have some form of validation instead of dropping the dictionary straight into the constructor
                if row:
                    return Player(**row_as_dict)
        except DatabaseError as e:
            raise e

        raise PlayerNotFoundError("Player not found")

    @staticmethod
    def update(
        id: int,
        name: str,
        dob: str,
        height: str,
        weight: int,
        position: Position,
        team_id: int,
    ):
        try:
            validate_data(
                id=id, name=name, dob=dob, height=height, weight=weight, team_id=team_id
            )
            validate_height(height)
        except ValueError as e:
            raise e

        try:
            Player.get(id)
        except PlayerNotFoundError as e:
            raise e

        sql = """
        UPDATE players
        SET name = %s, dob = %s, height = %s, weight = %s, position = %s, team_id = %s
        WHERE id = %s
        """

        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    sql,
                    (
                        name,
                        dob,
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

        sql = "DELETE FROM players WHERE id = %s"

        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, [id])
        except DatabaseError as e:
            raise e
