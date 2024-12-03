using Models;

namespace Services;

public interface ILeaguesService
{
    Task<int> CreateLeague(string name);
    Task<League> GetLeague(int id);
    Task<LeagueStandings> GetLeagueStandings(int id);
    Task UpdateLeague(int id, string name);
    Task DeleteLeague(int id);
}