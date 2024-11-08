import json
from typing import Optional
from enum import Enum
from datetime import datetime


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
