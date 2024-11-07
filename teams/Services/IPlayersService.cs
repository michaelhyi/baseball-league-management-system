using teams.Models;

namespace teams.Services;

public interface IPlayersService {
    Task<IEnumerable<Player>> GetPlayersByTeamId(int teamId);
}
