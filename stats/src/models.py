import logging
from datetime import datetime
from django.db import connection

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def validate_args_are_zero_or_pos(*args):
    for arg in args:
        if not isinstance(arg, int) and not isinstance(arg, float):
            raise ValueError(f"argument {arg} must be an int or float")
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
        created_at: datetime,
        updated_at: datetime,
        batting_average: float,
        on_base_percentage: float,
        slugging_percentage: float,
        on_base_plus_slugging: float,
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
        self.created_at = created_at
        self.updated_at = updated_at
        self.batting_average = batting_average
        self.on_base_percentage = on_base_percentage
        self.slugging_percentage = slugging_percentage
        self.on_base_plus_slugging = on_base_plus_slugging

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
        created_at: datetime,
        updated_at: datetime,
        earned_run_average: float,
        walks_and_hits_per_inning_pitched: float,
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
        self.created_at = created_at
        self.updated_at = updated_at
        self.earned_run_average = earned_run_average
        self.walks_and_hits_per_inning_pitched = walks_and_hits_per_inning_pitched

    @staticmethod
    def create(
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
    ):
        logger.info(f"creating PitchingStats for player_id {player_id}")

        if player_id <= 0:
            raise ValueError("playerId must be a positive int")
        validate_args_are_zero_or_pos(
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

        sql = """
        INSERT INTO pitching_stats (player_id, wins, losses, earned_runs, games, games_started, saves, innings_pitched, strikeouts, walks, hits)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """

        with connection.cursor() as cursor:
            cursor.execute(
                sql,
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
                ),
            )
            cursor.execute("SELECT LAST_INSERT_ID() AS id;")
            row = cursor.fetchone()
            id = row[0]
            logger.info(f"created PitchingStats with id {id}")

            return id

    @staticmethod
    def get(player_id: int):
        logger.info(f"getting pitching stats for player id {player_id}")
        if player_id <= 0:
            raise ValueError("playerId must be a positive int")

        sql = """
        SELECT *,
        ROUND(earned_runs / innings_pitched * 9, 3) AS earned_run_average, 
        ROUND((walks + hits) / innings_pitched), 3) AS walks_and_hits_per_innings_pitched
        FROM pitching_stats
        WHERE player_id = %s;
        """

        with connection.cursor() as cursor:
            cursor.execute(sql, [player_id])
            row = cursor.fetchone()

            if not row:
                raise StatsNotFoundError(
                    f"pitching stats for player id {player_id} not found"
                )
            logger.info(f"found pitching stats for player id {player_id}")
            return PitchingStats(*row)

    @staticmethod
    def update(
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
    ):
        logger.info(f"updating PitchingStats with player_id {player_id}")

        if player_id <= 0:
            raise ValueError("playerId must be a positive int")
        validate_args_are_zero_or_pos(
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

        sql = """
        UPDATE pitching_stats SET wins=%s, losses=%s, earned_runs=%s, games=%s, games_started=%s, saves=%s, innings_pitched=%s, strikeouts=%s, walks=%s, hits=%s
        WHERE player_id=%s;
        """

        with connection.cursor() as cursor:
            cursor.execute(
                sql,
                (
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
                    player_id,
                ),
            )
            logger.info(f"updated PitchingStats with player_id {player_id}")

    @staticmethod
    def delete(player_id: int):
        logger.info(f"deleting PitchingStats with player_id {player_id}")
        if player_id <= 0:
            raise ValueError("playerId must be a positive int")

        sql = "DELETE FROM pitching_stats WHERE player_id=%s;"
        with connection.cursor() as cursor:
            cursor.execute(sql, [player_id])
            logger.info(f"deleted PitchingStats with player_id {player_id}")
