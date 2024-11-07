from typing import List, Optional
from django.db import connection, DatabaseError
from src.models import Player


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
        sql = "SELECT * FROM player WHERE id = %s LIMIT 1"

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
    def get_by_team_id(team_id: int) -> List[Player]:
        sql = "SELECT * FROM player WHERE team_id = %s"

        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, [team_id])
                rows = cursor.fetchall()
                return [Player(*row) for row in rows]
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
