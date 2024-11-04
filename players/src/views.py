import json
from django.db import DatabaseError
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from src.models import PlayerNotFoundError, PlayerService, Position


def parse_body(request) -> tuple[str, int, str, int, Position, int]:
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


def handle_errors(func):
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


@require_http_methods(["POST"])
@handle_errors
def create_player(request):
    name, age, height, weight, position, team_id = parse_body(request)

    PlayerService.create_player(name, age, height, weight, position, team_id)
    return JsonResponse({"message": "Player created"}, status=201)


@require_http_methods(["GET", "PATCH", "DELETE"])
def player_view(request, id):
    if request.method == "GET":
        return get_player(request, id)
    if request.method == "PATCH":
        return update_player(request, id)
    return delete_player(request, id)


@handle_errors
def get_player(request, id):
    player = PlayerService.get_player(id)
    return JsonResponse({"player": player.serialize()}, status=200)


@handle_errors
def update_player(request, id):
    name, age, height, weight, position, team_id = parse_body(request)

    PlayerService.update_player(id, name, age, height, weight, position, team_id)
    return JsonResponse({"message": "Player updated"}, status=200)


@handle_errors
def delete_player(request, id):
    PlayerService.delete_player(id)
    return JsonResponse({"message": "Player deleted"}, status=200)
