using teams.Models;

namespace Repositories;

public interface ITeamsRepository
{
    Task<int> CreateTeamAsync(string name, int leagueId);
    Task<Team?> GetTeamAsync(int id);
    Task UpdateTeamAsync(Team team);
    Task DeleteTeamAsync(int id);
}