import logging
import json

from django.http import JsonResponse
from src.models import BattingStats, PitchingStats, StatsNotFoundError
from django.views.decorators.http import require_http_methods

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_batting_stats(
    request,
) -> tuple[int, int, int, int, int, int, int, int, int, int, int, int, int, int]:
    logging.info(f"parsing json body: {request.body}")
    body = json.loads(request.body)

    player_id = body["playerId"]
    at_bats = body["atBats"]
    runs = body["runs"]
    hits = body["hits"]
    total_bases = body["totalBases"]
    doubles = body["doubles"]
    triples = body["triples"]
    home_runs = body["homeRuns"]
    rbi = body["rbi"]
    walks = body["walks"]
    strikeouts = body["strikeouts"]
    stolen_bases = body["stolenBases"]
    hit_by_pitches = body["hitByPitches"]
    sac_flies = body["sacFlies"]

    return (
        player_id,
        at_bats,
        runs,
        hits,
        total_bases,
        doubles,
        triples,
        home_runs,
        rbi,
        walks,
        strikeouts,
        stolen_bases,
        hit_by_pitches,
        sac_flies,
    )


def parse_pitching_stats(
    request,
) -> tuple[int, int, int, int, int, int, int, float, int, int, int]:
    logging.info(f"parsing json body: {request.body}")
    body = json.loads(request.body)

    player_id = body["playerId"]
    wins = body["wins"]
    losses = body["losses"]
    earned_runs = body["earnedRuns"]
    games = body["games"]
    games_started = body["gamesStarted"]
    saves = body["saves"]
    innings_pitched = body["inningsPitched"]
    strikeouts = body["strikeouts"]
    walks = body["walks"]
    hits = body["hits"]

    return (
        player_id,
        wins,
        losses,
        earned_runs,
        games,
        games_started,
        saves,
        innings_pitched,
        strikeouts,
        walks,
        hits,
    )


def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, KeyError) as e:
            logging.error(str(e))
            return JsonResponse({"error": str(e)}, status=400)
        except StatsNotFoundError as e:
            logging.error(str(e))
            return JsonResponse({"error": str(e)}, status=404)
        except Exception as e:
            logging.error(str(e))
            return JsonResponse({"error": "internal server error"}, status=500)

    return wrapper


@error_handler
@require_http_methods(["POST"])
def create_batting_stats_view(request):
    logger.info("creating batting stats")
    (
        player_id,
        at_bats,
        runs,
        hits,
        total_bases,
        doubles,
        triples,
        home_runs,
        rbi,
        walks,
        strikeouts,
        stolen_bases,
        hit_by_pitches,
        sac_flies,
    ) = parse_batting_stats(request)

    id = BattingStats.create(
        player_id,
        at_bats,
        runs,
        hits,
        total_bases,
        doubles,
        triples,
        home_runs,
        rbi,
        walks,
        strikeouts,
        stolen_bases,
        hit_by_pitches,
        sac_flies,
    )
    return JsonResponse({"id": id}, status=201)


@error_handler
@require_http_methods(["POST"])
def create_pitching_stats_view(request):
    logger.info("creating pitching stats")
    (
        player_id,
        wins,
        losses,
        earned_runs,
        games,
        games_started,
        saves,
        innings_pitched,
        strikeouts,
        walks,
        hits,
    ) = parse_pitching_stats(request)

    id = PitchingStats.create(
        player_id,
        wins,
        losses,
        earned_runs,
        games,
        games_started,
        saves,
        innings_pitched,
        strikeouts,
        walks,
        hits,
    )
    return JsonResponse({"id": id}, status=201)


@error_handler
@require_http_methods(["GET", "PATCH", "DELETE"])
def batting_stats_view(request, player_id):
    logger.info(f"handling request for batting stats with player id: {player_id}")
    if request.method == "GET":
        return get_batting_stats(request, player_id)

    if request.method == "PATCH":
        return update_batting_stats(request, player_id)

    return delete_batting_stats(request, player_id)


def get_batting_stats(request, player_id):
    logger.info(f"getting batting stats with player id: {player_id}")
    stats = BattingStats.get(player_id)
    logger.info(f"got batting stats: {stats}")
    return JsonResponse(
        {
            "battingStats": {
                "id": stats.id,
                "playerId": stats.player_id,
                "atBats": stats.at_bats,
                "runs": stats.runs,
                "hits": stats.hits,
                "totalBases": stats.total_bases,
                "doubles": stats.doubles,
                "triples": stats.triples,
                "homeRuns": stats.home_runs,
                "rbi": stats.runs_batted_in,
                "walks": stats.walks,
                "strikeouts": stats.strikeouts,
                "stolenBases": stats.stolen_bases,
                "hitByPitches": stats.hit_by_pitch,
                "sacrificeFlies": stats.sacrifice_flies,
                "createdAt": stats.created_at,
                "updatedAt": stats.updated_at,
                "battingAverage": stats.batting_average,
                "onBasePercentage": stats.on_base_percentage,
                "sluggingPercentage": stats.slugging_percentage,
                "ops": stats.on_base_plus_slugging,
            }
        },
        status=200,
    )


def update_batting_stats(request, player_id):
    (
        player_id,
        at_bats,
        runs,
        hits,
        total_bases,
        doubles,
        triples,
        home_runs,
        rbi,
        walks,
        strikeouts,
        stolen_bases,
        hit_by_pitches,
        sac_flies,
    ) = parse_batting_stats(request)

    BattingStats.update(
        player_id,
        at_bats,
        runs,
        hits,
        total_bases,
        doubles,
        triples,
        home_runs,
        rbi,
        walks,
        strikeouts,
        stolen_bases,
        hit_by_pitches,
        sac_flies,
    )
    return JsonResponse({}, status=204)


def delete_batting_stats(request, player_id):
    logger.info(f"handling request for batting stats with player id: {player_id}")
    if request.method == "DELETE":
        BattingStats.delete(player_id)
        return JsonResponse({}, status=204)


@error_handler
@require_http_methods(["GET", "PATCH", "DELETE"])
def pitching_stats_view(request, player_id):
    logger.info(f"handling request for pitching stats with player id: {player_id}")
    if request.method == "GET":
        return get_pitching_stats(request, player_id)

    if request.method == "PATCH":
        return update_pitching_stats(request, player_id)

    return delete_pitching_stats(request, player_id)


def get_pitching_stats(request, player_id):
    stats = PitchingStats.get(player_id)
    return JsonResponse(
        {
            "pitchingStats": {
                "id": stats.id,
                "playerId": stats.player_id,
                "wins": stats.wins,
                "losses": stats.losses,
                "earnedRuns": stats.earned_runs,
                "games": stats.games,
                "gamesStarted": stats.games_started,
                "saves": stats.saves,
                "inningsPitched": stats.innings_pitched,
                "strikeouts": stats.strikeouts,
                "walks": stats.walks,
                "hits": stats.hits,
                "createdAt": stats.created_at,
                "updatedAt": stats.updated_at,
                "earnedRunAverage": stats.earned_run_average,
                "whip": stats.walks_and_hits_per_inning_pitched,
            }
        },
        status=200,
    )


def update_pitching_stats(request, player_id):
    (
        player_id,
        wins,
        losses,
        earned_runs,
        games,
        games_started,
        saves,
        innings_pitched,
        strikeouts,
        walks,
        hits,
    ) = parse_pitching_stats(request)

    PitchingStats.update(
        player_id,
        wins,
        losses,
        earned_runs,
        games,
        games_started,
        saves,
        innings_pitched,
        strikeouts,
        walks,
        hits,
    )
    return JsonResponse({}, status=204)


def delete_pitching_stats(request, player_id):
    logger.info(f"handling request for pitching stats with player id: {player_id}")
    if request.method == "DELETE":
        PitchingStats.delete(player_id)
        return JsonResponse({}, status=204)
