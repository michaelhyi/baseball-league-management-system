# from django.shortcuts import render
from django.db import DatabaseError
from django.http import JsonResponse
from django.http.response import json
from django.views.decorators.http import require_http_methods

from players.src.models import PlayerNotFoundError, PlayerService, Position


@require_http_methods(["POST"])
def create_player(request):
    try:
        body = json.loads(request.body)

        name = body.get("name")
        age = body.get("age")
        height = body.get("height")
        weight = body.get("weight")
        position = Position[body.get("position")]
        team_id = body.get("teamId")

        PlayerService.create_player(name, age, height, weight, position, team_id)
        return JsonResponse({"message": "Player created"}, status=201)
    except ValueError as e:
        return JsonResponse({"error": str(e)}, status=400)
    except KeyError as e:
        return JsonResponse({"error": str(e)}, status=400)
    except DatabaseError as e:
        return JsonResponse({"error": "Internal server error"}, status=500)


@require_http_methods(["GET"])
def get_player(request, id):
    try:
        player = PlayerService.get_player(id)
        return JsonResponse(player.__dict__, status=200)
    except ValueError as e:
        return JsonResponse({"error": str(e)}, status=400)
    except PlayerNotFoundError as e:
        return JsonResponse({"error": str(e)}, status=404)
    except DatabaseError as e:
        return JsonResponse({"error": "Internal server error"}, status=500)


@require_http_methods(["PATCH"])
def update_player(request, id):
    try:
        body = json.loads(request.body)

        name = body.get("name")
        age = body.get("age")
        height = body.get("height")
        weight = body.get("weight")
        position = Position[body.get("position")]
        team_id = body.get("teamId")

        PlayerService.update_player(id, name, age, height, weight, position, team_id)
        return JsonResponse({"message": "Player updated"}, status=200)
    except ValueError as e:
        return JsonResponse({"error": str(e)}, status=400)
    except KeyError as e:
        return JsonResponse({"error": str(e)}, status=400)
    except PlayerNotFoundError as e:
        return JsonResponse({"error": str(e)}, status=404)
    except DatabaseError as e:
        return JsonResponse({"error": "Internal server error"}, status=500)


@require_http_methods(["DELETE"])
def delete_player(request, id):
    try:
        PlayerService.delete_player(id)
        return JsonResponse({"message": "Player deleted"}, status=200)
    except ValueError as e:
        return JsonResponse({"error": str(e)}, status=400)
    except PlayerNotFoundError as e:
        return JsonResponse({"error": str(e)}, status=404)
    except DatabaseError as e:
        return JsonResponse({"error": "Internal server error"}, status=500)
