using Data;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Storage;
using Models;

namespace Daos;

public class LeaguesDao : ILeaguesDao
{
    private readonly ILogger<LeaguesDao> _logger;
    private readonly ApplicationDbContext _dbCtx;

    public LeaguesDao(ILogger<LeaguesDao> logger, ApplicationDbContext dbCtx)
    {
        _logger = logger;
        _dbCtx = dbCtx;
    }

    public async Task<int> CreateLeagueAsync(string name)
    {
        _logger.LogInformation("dao received request to create league {name}", name);
        IDbContextTransaction transaction = await _dbCtx.Database.BeginTransactionAsync();

        try
        {
            await _dbCtx.Database.ExecuteSqlRawAsync
            (
                "INSERT INTO leagues (name) VALUES (@p0)",
                name
            );
            int id = await _dbCtx.Leagues.FromSqlRaw("SELECT LAST_INSERT_ID() as id").Select(l => l.Id).FirstOrDefaultAsync();
            await transaction.CommitAsync();
            _logger.LogInformation("inserted team with id {id}", id);

            return id;
        }
        catch
        {
            _logger.LogError("error inserting league");
            await transaction.RollbackAsync();
            throw;
        }
        finally
        {
            await transaction.DisposeAsync();
        }
    }

    public async Task<League?> GetLeagueAsync(int id)
    {
        _logger.LogInformation("dao received request to get league with id {id}", id);
        return await _dbCtx.Leagues
            .FromSqlRaw("SELECT * FROM leagues WHERE id = @p0 LIMIT 1", id)
            .FirstOrDefaultAsync();
    }

    public async Task<IEnumerable<TeamStandings>> GetTeamStandingsAsync(int leagueId)
    {
        _logger.LogInformation("dao received request to get team standings with leagueId {leagueId}", leagueId);
        return await _dbCtx.TeamStandings
            .FromSqlRaw(
                @"
                WITH team_standings_sub AS (
                    SELECT teams.id, teams.name, SUM(
                        CASE
                            WHEN games.home_team_id=teams.id AND games.home_team_score > games.away_team_score THEN 1
                            WHEN games.away_team_id=teams.id AND games.away_team_score > games.home_team_score THEN 1
                            ELSE 0
                        END
                    ) AS wins,
                    SUM(
                        CASE
                            WHEN games.home_team_id=teams.id AND games.home_team_score < games.away_team_score THEN 1
                            WHEN games.away_team_id=teams.id AND games.away_team_score < games.home_team_score THEN 1
                            ELSE 0
                        END
                    ) AS losses,
                    SUM(
                        CASE
                            WHEN games.home_team_id=teams.id THEN games.home_team_score
                            ELSE games.away_team_score
                        END
                    ) AS runs_scored, 
                    SUM(
                        CASE
                            WHEN games.home_team_id=teams.id THEN games.away_team_score
                            ELSE games.home_team_score
                        END
                    ) AS runs_allowed,
                    CONCAT(
                        SUM(
                            CASE
                                WHEN games.home_team_id=teams.id AND games.home_team_score > games.away_team_score THEN 1
                                ELSE 0
                            END
                        ),
                        '-',
                        SUM(
                            CASE
                                WHEN games.home_team_id=teams.id AND games.home_team_score < games.away_team_score THEN 1
                                ELSE 0
                            END
                        )
                    ) AS home_record,
                    CONCAT(
                        SUM(
                            CASE
                                WHEN games.away_team_id=teams.id AND games.home_team_score < games.away_team_score THEN 1
                                ELSE 0
                            END
                        ),
                        '-',
                        SUM(
                            CASE
                                WHEN games.away_team_id=teams.id AND games.home_team_score > games.away_team_score THEN 1
                                ELSE 0
                            END
                        )
                    ) AS away_record
                    FROM teams
                    LEFT JOIN games ON games.home_team_id=teams.id OR games.away_team_id=teams.id
                    WHERE league_id = @p0
                    GROUP BY teams.id, teams.name
                )

                SELECT *,
                (
                    CASE
                        WHEN wins + losses = 0 THEN 0.000
                        ELSE ROUND(wins / (wins + losses), 3)
                    END
                ) AS winning_percentage,
                runs_scored - runs_allowed AS run_differential
                FROM team_standings_sub;",
                leagueId
            ).ToListAsync();
    }

    public async Task UpdateLeagueAsync(int id, string name)
    {
        _logger.LogInformation("dao received request to update league with id {id} to name {name}", id, name);
        await _dbCtx.Database.ExecuteSqlRawAsync
        (
            "UPDATE leagues SET name = @p0 WHERE id = @p1",
            name,
            id
        );
    }

    public async Task DeleteLeagueAsync(int id)
    {
        _logger.LogInformation("dao received request to delete league with id {id}", id);
        await _dbCtx.Database.ExecuteSqlRawAsync
        (
            "DELETE from leagues WHERE id = @p0", id
        );
    }
}