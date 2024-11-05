using System.Runtime.CompilerServices;
using Data;
using Microsoft.EntityFrameworkCore;
using teams.Models;

namespace Repositories;

public class TeamsRepository : ITeamsRepository
{
    private readonly ApplicationDbContext _ctx;

    public TeamsRepository(ApplicationDbContext ctx)
    {
        _ctx = ctx;
    }

    public async Task<int> CreateTeamAsync(string name, int leagueId)
    {
        return await _ctx.Database.ExecuteSqlRawAsync
        (
            "INSERT INTO teams (name, league_id) VALUES (@p0, @p1); SELECT LAST_INSERT_ID();",
            name,
            leagueId
        );
    }

    public async Task<Team?> GetTeamAsync(int id)
    {
        return await _ctx.Teams
            .FromSqlRaw("SELECT * FROM teams WHERE id = @p0 LIMIT 1", id)
            .FirstOrDefaultAsync();
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
