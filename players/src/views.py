import json
import logging
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods

from src.models import Player, PlayerNotFoundError, Position

logging.basicConfig(level=logging.INFO)


def parse_body(request) -> tuple[str, str, str, str, int, Position, int]:
    logging.info(f"parsing json body: {request.body}")
    body = json.loads(request.body)

    name = body["name"]
    jersey_number = body["jerseyNumber"]
    dob = body["dob"]
    height = body["height"]
    weight = body["weight"]

    position = Position(body["position"])

    # TODO: fix
    # if body["position"] not in Position.__members__:
    # raise ValueError("Invalid position")

    team_id = body["teamId"]

    return name, jersey_number, dob, height, weight, position, team_id


def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, KeyError) as e:
            logging.error(str(e))
            return JsonResponse({"error": str(e)}, status=400)
        except PlayerNotFoundError as e:
            logging.error(str(e))
            return JsonResponse({"error": str(e)}, status=404)
        except Exception as e:
            logging.error(str(e))
            return JsonResponse({"error": "internal server error"}, status=500)

    return wrapper


@require_http_methods(["POST"])
@error_handler
def create_player(request):
    logging.info("create player request received")
    name, jersey_number, dob, height, weight, position, team_id = parse_body(request)

    logging.info("Successfully parsed json body")

    id = Player.create(name, jersey_number, dob, height, weight, position, team_id)
    return JsonResponse({"id": id}, status=201)


# TODO: rename function
@require_http_methods(["GET", "PATCH", "DELETE"])
def player_view(request, id):
    if request.method == "GET":
        return get_player(request, id)
    if request.method == "PATCH":
        return update_player(request, id)
    return delete_player(request, id)


# TODO: handle request not accesssed
@error_handler
def get_player(request, id):
    player = Player.get(id)
    return JsonResponse({"player": player.serialize()}, status=200)


@error_handler
def update_player(request, id):
    name, jersey_number, dob, height, weight, position, team_id = parse_body(request)

    Player.update(id, name, jersey_number, dob, height, weight, position, team_id)
    return HttpResponse(status=204)


@error_handler
def delete_player(request, id):
    Player.delete(id)
    return HttpResponse(status=204)
