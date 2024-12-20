using System.Text.Json;
using Daos;
using teams.Models;

namespace teams.Services;

public class TeamsService : ITeamsService
{
    private readonly ILogger<TeamsService> _logger;
    private readonly ITeamsDao _teamsDao;

    public TeamsService
    (
        ILogger<TeamsService> logger,
        ITeamsDao teamsDao
    )
    {
        _logger = logger;
        _teamsDao = teamsDao;
    }

    public async Task<int> CreateTeam(TeamRequest req)
    {
        _logger.LogInformation("Creating team");
        _logger.LogInformation("Request: {0}", JsonSerializer.Serialize(req));

        if (string.IsNullOrEmpty(req.Name) || string.IsNullOrWhiteSpace(req.Name))
        {
            throw new ArgumentException("name must not be empty");
        }

        if (req.LeagueId <= 0)
        {
            throw new ArgumentException("leagueId must be positive");
        }

        return await _teamsDao.CreateTeamAsync(req.Name, req.LeagueId);
    }

    public async Task<Team> GetTeam(int id)
    {
        _logger.LogInformation("Getting team with id {0}", id);

        if (id <= 0)
        {
            throw new ArgumentException("id must be positive");
        }

        Team? team = await _teamsDao.GetTeamAsync(id);

        if (team == null)
        {
            throw new KeyNotFoundException("team not found");
        }

        return team;
    }

    public async Task<TeamWithRoster> GetTeamWithRoster(int id)
    {
        _logger.LogInformation("Getting roster for team with id {0}", id);

        if (id <= 0)
        {
            throw new ArgumentException("id must be positive");
        }

        Team? team = await _teamsDao.GetTeamAsync(id);

        if (team == null)
        {
            throw new KeyNotFoundException("team not found");
        }

        IEnumerable<Player> roster = await _teamsDao.GetRosterAsync(id);

        return new TeamWithRoster(team, roster);
    }

    public async Task UpdateTeam(int id, TeamRequest req)
    {
        _logger.LogInformation("Updating team with id {0}", id);
        _logger.LogInformation("Request: {0}", JsonSerializer.Serialize(req));

        if (id <= 0)
        {
            throw new ArgumentException("id must be positive");
        }

        if (string.IsNullOrEmpty(req.Name) && string.IsNullOrWhiteSpace(req.Name) && req.LeagueId <= 0)
        {
            throw new ArgumentException("at least one valid field must be provided");
        }

        Team? team = await _teamsDao.GetTeamAsync(id);

        if (team == null)
        {
            throw new KeyNotFoundException("team not found");
        }

        if (!string.IsNullOrEmpty(req.Name) && !string.IsNullOrWhiteSpace(req.Name))
        {
            team.Name = req.Name;
        }

        if (req.LeagueId > 0)
        {
            team.LeagueId = req.LeagueId;
        }

        await _teamsDao.UpdateTeamAsync(team);
    }

    public async Task DeleteTeam(int id)
    {
        _logger.LogInformation("Deleting team with id {0}", id);

        if (id <= 0)
        {
            throw new ArgumentException("id must be positive");
        }

        Team? team = await _teamsDao.GetTeamAsync(id);
        if (team == null)
        {
            throw new KeyNotFoundException("team not found");
        }

        await _teamsDao.DeleteTeamAsync(id);
    }
}