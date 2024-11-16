using Data;
using Microsoft.EntityFrameworkCore;
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
        int id = await _dbCtx.Leagues
                .FromSqlRaw(@"START TRANSACTION;
                            INSERT INTO leagues (name) VALUES (@p0);
                            SELECT LAST_INSERT_ID() as id;
                            COMMIT;", name)
                .Select(t => t.Id).FirstOrDefaultAsync();

        _logger.LogInformation("inserted team with id {id}", id);
        return id;
    }

    public async Task<League?> GetLeagueAsync(int id)
    {
        _logger.LogInformation("dao received request to get league with id {id}", id);
        return await _dbCtx.Leagues
            .FromSqlRaw("SELECT * FROM leagues WHERE id = @p0 LIMIT 1", id)
            .FirstOrDefaultAsync();
    }

    public async Task UpdateLeagueAsync(int id, string name)
    {
        _logger.LogInformation("dao received request to update league with id {id} to name {name}", id, name);
        await _dbCtx.Database.ExecuteSqlRawAsync
        (
            "UPDATE leagues SET name = @p0 WHERE id = @p2",
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