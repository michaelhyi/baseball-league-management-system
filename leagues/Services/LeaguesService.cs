using Daos;
using Models;

namespace Services;

public class LeaguesService : ILeaguesService
{
    private readonly ILogger<LeaguesService> _logger;
    private readonly ILeaguesDao _dao;

    public LeaguesService(ILogger<LeaguesService> logger, ILeaguesDao dao)
    {
        _logger = logger;
        _dao = dao;
    }

    public async Task<int> CreateLeague(string name) {
        _logger.LogInformation("service received request to create league with name {name}", name);

        if (name == null || name.Length == 0) {
            throw new ArgumentException("name cannot be null or empty");
        }

        int id = await _dao.CreateLeagueAsync(name);
        _logger.LogInformation("service created league with id {id}", id);
        return id;
    }

    public async Task<League> GetLeague(int id) {
        _logger.LogInformation("service received request to get league with id {id}", id);

        if (id <= 0) {
            throw new ArgumentException("id cannot be negative or zero");
        }

        League? league = await _dao.GetLeagueAsync(id);
        _logger.LogInformation("service retrieved league with league {league}", league);

        if (league == null) {
            throw new KeyNotFoundException($"league with id {id} not found");
        }

        return league;
    }

    public async Task UpdateLeague(int id, string name) {
        _logger.LogInformation("service received request to update league with id {id} and name {name}", id, name);

        if (id <= 0) {
            throw new ArgumentException("id cannot be negative or zero");
        }

        if (name == null || name.Length == 0) {
            throw new ArgumentException("name cannot be null or empty");
        }

        await _dao.UpdateLeagueAsync(id, name);
        _logger.LogInformation("service updated league with id {id} and name {name}", id, name);
    }

    public async Task DeleteLeague(int id) {
        _logger.LogInformation("service received request to delete league with id {id}", id);

        if (id <= 0) {
            throw new ArgumentException("id cannot be negative or zero");
        }

        await _dao.DeleteLeagueAsync(id);
        _logger.LogInformation("service deleted league with id {id}", id);
    }
}