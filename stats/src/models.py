import logging
from datetime import datetime
from django.db import connection

logger = logging.getLogger(__name__)


def validate_args_are_zero_or_pos(*args):
    for arg in args:
        if not isinstance(arg, int):
            raise ValueError(f"argument {arg} must be an int")
        if arg < 0:
            raise ValueError(f"argument {arg} cannot be negative")


class StatsNotFoundError(Exception):
    pass


class BattingStats:
    def __init__(
        self,
        id: int,
        player_id: int,
        at_bats: int,
        runs: int,
        hits: int,
        total_bases: int,
        doubles: int,
        triples: int,
        home_runs: int,
        runs_batted_in: int,
        walks: int,
        strikeouts: int,
        stolen_bases: int,
        hit_by_pitch: int,
        sacrifice_flies: int,
        batting_average: float,
        on_base_percentage: float,
        slugging_percentage: float,
        on_base_plus_slugging: float,
        created_at: datetime,
        updated_at: datetime,
    ):
        self.id = id
        self.player_id = player_id
        self.at_bats = at_bats
        self.runs = runs
        self.hits = hits
        self.total_bases = total_bases
        self.doubles = doubles
        self.triples = triples
        self.home_runs = home_runs
        self.runs_batted_in = runs_batted_in
        self.walks = walks
        self.strikeouts = strikeouts
        self.stolen_bases = stolen_bases
        self.hit_by_pitch = hit_by_pitch
        self.sacrifice_flies = sacrifice_flies
        self.batting_average = batting_average
        self.on_base_percentage = on_base_percentage
        self.slugging_percentage = slugging_percentage
        self.on_base_plus_slugging = on_base_plus_slugging
        self.created_at = created_at
        self.updated_at = updated_at

    @staticmethod
    def create(
        player_id: int,
        at_bats: int,
        runs: int,
        hits: int,
        total_bases: int,
        doubles: int,
        triples: int,
        home_runs: int,
        runs_batted_in: int,
        walks: int,
        strikeouts: int,
        stolen_bases: int,
        hit_by_pitch: int,
        sacrifice_flies: int,
    ):
        logger.info("Creating BattingStats")

        if player_id <= 0:
            raise ValueError("playerId must be a positive int")
        validate_args_are_zero_or_pos(
            at_bats,
            runs,
            hits,
            total_bases,
            doubles,
            triples,
            home_runs,
            runs_batted_in,
            walks,
            strikeouts,
            stolen_bases,
            hit_by_pitch,
            sacrifice_flies,
        )

        sql = """
        INSERT INTO batting_stats (player_id, at_bats, runs, hits, total_bases, doubles, triples, home_runs, runs_batted_in, walks, strikeouts, stolen_bases, hit_by_pitch, sacrifice_flies)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """

        with connection.cursor() as cursor:
            cursor.execute(
                sql,
                (
                    player_id,
                    at_bats,
                    runs,
                    hits,
                    total_bases,
                    doubles,
                    triples,
                    home_runs,
                    runs_batted_in,
                    walks,
                    strikeouts,
                    stolen_bases,
                    hit_by_pitch,
                    sacrifice_flies,
                ),
            )
            cursor.execute("SELECT LAST_INSERT_ID() AS id;")
            row = cursor.fetchone()
            id = row[0]
            logger.info(f"Created BattingStats with id {id}")

            return id

    @staticmethod
    def get(player_id: int):
        logger.info(f"getting batting stats for player id {player_id}")
        if player_id <= 0:
            raise ValueError("playerId must be a positive int")

        sql = """
        SELECT *,
        (on_base_percentage + slugging_percentage) AS on_base_plus_slugging_percentage FROM
        (
            SELECT *,
            ROUND(hits / at_bats, 3) AS batting_average,
            ROUND((hits + walks + hit_by_pitch) / (at_bats + walks + hit_by_pitch + sacrifice_flies), 3) AS on_base_percentage,
            ROUND(total_bases / at_bats, 3) AS slugging_percentage
            FROM batting_stats WHERE player_id = %s
        ) AS subquery;
        """

        with connection.cursor() as cursor:
            cursor.execute(sql, [id])
            row = cursor.fetchone()

            if not row:
                raise StatsNotFoundError(
                    f"batting stats for player id {player_id} not found"
                )
            logger.info(f"found batting stats for player id {player_id}")
            return BattingStats(*row)

    @staticmethod
    def update(
        player_id: int,
        at_bats: int,
        runs: int,
        hits: int,
        total_bases: int,
        doubles: int,
        triples: int,
        home_runs: int,
        runs_batted_in: int,
        walks: int,
        strikeouts: int,
        stolen_bases: int,
        hit_by_pitch: int,
        sacrifice_flies: int,
    ):
        logger.info(f"updating BattingStats with player_id {player_id}")

        if player_id <= 0:
            raise ValueError("playerId must be a positive int")
        validate_args_are_zero_or_pos(
            at_bats,
            runs,
            hits,
            total_bases,
            doubles,
            triples,
            home_runs,
            runs_batted_in,
            walks,
            strikeouts,
            stolen_bases,
            hit_by_pitch,
            sacrifice_flies,
        )

        sql = """
        UPDATE batting_stats SET at_bats=%s, runs=%s, hits=%s, total_bases=%s, doubles=%s, triples=%s, home_runs=%s, runs_batted_in=%s, walks=%s, strikeouts=%s, stolen_bases=%s, hit_by_pitch=%s, sacrifice_flies=%s
        WHERE player_id=%s;
        """

        with connection.cursor() as cursor:
            cursor.execute(
                sql,
                (
                    at_bats,
                    runs,
                    hits,
                    total_bases,
                    doubles,
                    triples,
                    home_runs,
                    runs_batted_in,
                    walks,
                    strikeouts,
                    stolen_bases,
                    hit_by_pitch,
                    sacrifice_flies,
                    player_id,
                ),
            )
            logger.info(f"updated BattingStats with player_id {player_id}")

    @staticmethod
    def delete(player_id: int):
        logger.info(f"deleting BattingStats with player_id {player_id}")
        if player_id <= 0:
            raise ValueError("playerId must be a positive int")

        sql = "DELETE FROM batting_stats WHERE player_id=%s;"
        with connection.cursor() as cursor:
            cursor.execute(sql, [player_id])
            logger.info(f"deleted BattingStats with player_id {player_id}")


class PitchingStats:
    def __init__(
        self,
        id: int,
        player_id: int,
        wins: int,
        losses: int,
        earned_runs: int,
        games: int,
        games_started: int,
        saves: int,
        innings_pitched: float,
        strikeouts: int,
        walks: int,
        hits: int,
        earned_run_average: float,
        walks_and_hits_per_inning_pitched: float,
        created_at: datetime,
        updated_at: datetime,
    ):
        self.id = id
        self.player_id = player_id
        self.wins = wins
        self.losses = losses
        self.earned_runs = earned_runs
        self.games = games
        self.games_started = games_started
        self.saves = saves
        self.innings_pitched = innings_pitched
        self.strikeouts = strikeouts
        self.walks = walks
        self.hits = hits
        self.earned_run_average = earned_run_average
        self.walks_and_hits_per_inning_pitched = walks_and_hits_per_inning_pitched
        self.created_at = created_at
        self.updated_at = updated_at
