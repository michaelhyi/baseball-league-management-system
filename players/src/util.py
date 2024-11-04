import json
import re

from django.db import DatabaseError
from django.http import JsonResponse

from src.models import Position


class PlayerNotFoundError(Exception):
    pass


def parse_json_body(request) -> tuple[str, int, str, int, Position, int]:
    body = json.loads(request.body)

    name = body["name"]
    age = body["age"]
    height = body["height"]
    weight = body["weight"]

    position = Position(body["position"])

    # TODO: fix
    # if body["position"] not in Position.__members__:
    # raise ValueError("Invalid position")

    team_id = body["teamId"]

    return name, age, height, weight, position, team_id


def handle_view_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)
        except KeyError as e:
            return JsonResponse({"error": str(e)}, status=400)
        except PlayerNotFoundError as e:
            return JsonResponse({"error": str(e)}, status=404)
        except DatabaseError as e:
            return JsonResponse({"error": "Internal server error"}, status=500)

    return wrapper


height_pattern = r"^(?:(\d{1,2})'(\d{1,2})\"|\d{1,2}'\s*\d{1,2}\s*\"|(?:(\d{1,2})\s*feet\s*(\d{1,2})\s*inches))$"


class PlayerServiceUtil:
    @staticmethod
    def validate_data(**kwargs):
        for key, value in kwargs.items():
            if isinstance(value, str) and (value is None or len(value) == 0):
                raise ValueError(f"{key} must not be empty")
            if isinstance(value, int) and value <= 0:
                raise ValueError(f"{key} must be positive")

    @staticmethod
    def validate_height(height):
        if not re.match(height_pattern, height):
            raise ValueError("Height must match the following pattern: <ft>'<in>\"")
