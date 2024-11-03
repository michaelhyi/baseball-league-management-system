from django.db import connection
from enum import Enum

class Position(Enum):
    P = 'Pitcher'
    C = 'Catcher'
    FIRST_B = 'First Base'
    SECOND_B = 'Second Base'
    THIRD_B = 'Third Base'
    SS = 'Shortstop'
    LF = 'Left Field'
    CF = 'Center Field'
    RF = 'Right Field'
    DH = 'Designated Hitter'

class Player:
    def __init__(self, id: int, name: str, age: int, height: str, weight: int, position: Position, team_id: int):
        self.id = id
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.position = position
        self.team_id = team_id

class PlayerDao:
    @staticmethod
    def create(player: Player):
        query = '''
        INSERT INTO player (name, age, height, weight, position, team_id)
        VALUES (%s, %s, %s, %s, %s, %s)
        '''

        with connection.cursor() as cursor:
            cursor.execute(query, (player.name, player.age, player.height, player.weight, player.position.value, player.team_id))

    @staticmethod
    def read(id: int):
        query = '''
        SELECT id, name, age, height, weight, position, team_id
        FROM player
        WHERE id = %s
        '''
        with connection.cursor() as cursor:
            cursor.execute(query, [id])
            row = cursor.fetchone()
            if row:
                return Player(*row)
            return None

    @staticmethod
    def update(player: Player):
        query = '''
        UPDATE player
        SET name = %s, age = %s, height = %s, weight = %s, position = %s, team_id = %s
        WHERE id = %s
        '''
        with connection.cursor() as cursor:
            cursor.execute(query, (player.name, player.age, player.height, player.weight, player.position.value, player.team_id, player.id))

    @staticmethod
    def delete(id: int):
        query = '''
        DELETE FROM player WHERE id = %s
        '''
        with connection.cursor() as cursor:
            cursor.execute(query, [id])
