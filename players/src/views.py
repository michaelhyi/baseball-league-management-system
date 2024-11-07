from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from src.util import handle_view_errors, parse_json_body
from src.service import PlayerService


@require_http_methods(["GET", "POST"])
@handle_view_errors
def create_player_or_get_players_by_team_id(request):
    team_id = request.GET.get("teamId")

    if team_id and request.method == "GET":
        players = PlayerService.get_players_by_team_id(team_id)
        return JsonResponse(
            {"players": [player.serialize() for player in players]}, status=200
        )

    if team_id and not request.method == "GET":
        return JsonResponse({"message": "method not allowed"}, status=405)

    if not team_id and request.method == "GET":
        return JsonResponse({"message": "teamId is required"}, status=400)

    name, age, height, weight, position, team_id = parse_json_body(request)

    PlayerService.create_player(name, age, height, weight, position, team_id)
    return JsonResponse({"message": "Player created"}, status=201)


@require_http_methods(["GET", "PATCH", "DELETE"])
def player_view(request, id):
    if request.method == "GET":
        return get_player(request, id)
    if request.method == "PATCH":
        return update_player(request, id)
    return delete_player(request, id)


@handle_view_errors
def get_player(request, id):
    player = PlayerService.get_player(id)
    return JsonResponse({"player": player.serialize()}, status=200)


@handle_view_errors
def update_player(request, id):
    name, age, height, weight, position, team_id = parse_json_body(request)

    PlayerService.update_player(id, name, age, height, weight, position, team_id)
    return JsonResponse({"message": "Player updated"}, status=200)


@handle_view_errors
def delete_player(request, id):
    PlayerService.delete_player(id)
    return JsonResponse({"message": "Player deleted"}, status=200)
