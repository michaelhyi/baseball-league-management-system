using teams.Models;

namespace Daos;

public interface ITeamsDao
{
    Task<int> CreateTeamAsync(string name, int leagueId);
    Task<Team?> GetTeamAsync(int id);
    Task<IEnumerable<Player>> GetRosterAsync(int teamId);
    Task UpdateTeamAsync(Team team);
    Task DeleteTeamAsync(int id);
}