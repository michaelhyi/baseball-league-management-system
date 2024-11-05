using teams.Models;

namespace teams.Services;
public interface ITeamsService
{
    Task CreateTeam(TeamRequest req);
    Task<Team> GetTeam(int id);
    Task UpdateTeam(int id, TeamRequest req);
    Task DeleteTeam(int id);
}