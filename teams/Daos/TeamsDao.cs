using Data;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Storage;
using teams.Models;

namespace Daos;

public class TeamsDao : ITeamsDao
{
    private readonly ILogger<TeamsDao> _logger;
    private readonly ApplicationDbContext _ctx;

    public TeamsDao(ILogger<TeamsDao> logger, ApplicationDbContext ctx)
    {
        _logger = logger;
        _ctx = ctx;
    }

    public async Task<int> CreateTeamAsync(string name, int leagueId)
    {
        IDbContextTransaction transaction = await _ctx.Database.BeginTransactionAsync();

        try
        {
            await _ctx.Database.ExecuteSqlRawAsync
            (
                    "INSERT INTO teams (name, league_id) VALUES (@p0, @p1)",
                    name,
                    leagueId
            );

            int id = await _ctx.Teams
                    .FromSqlRaw("SELECT LAST_INSERT_ID() as id")
                    .Select(t => t.Id).FirstOrDefaultAsync();

            await transaction.CommitAsync();

            _logger.LogInformation("Created team with id {id}", id);
            return id;
        }

        catch
        {
            await transaction.RollbackAsync();
            throw;
        }

        finally
        {
            await transaction.DisposeAsync();
        }
    }

    public async Task<Team?> GetTeamAsync(int id)
    {
        return await _ctx.Teams
            .FromSqlRaw("SELECT * FROM teams WHERE id = @p0 LIMIT 1", id)
            .FirstOrDefaultAsync();
    }

    public async Task<IEnumerable<Player>> GetRosterAsync(int teamId) {
        return await _ctx.Players
            .FromSqlRaw("SELECT * FROM player WHERE team_id = @p0", teamId)
            .ToListAsync();
    }

    public async Task UpdateTeamAsync(Team team)
    {
        await _ctx.Database.ExecuteSqlRawAsync
        (
            "UPDATE teams SET name = @p0, league_id = @p1 WHERE id = @p2",
            team.Name,
            team.LeagueId,
            team.Id
        );
    }

    public async Task DeleteTeamAsync(int id)
    {
        await _ctx.Database.ExecuteSqlRawAsync
        (
            "DELETE from teams WHERE id = @p0", id
        );
    }
}
