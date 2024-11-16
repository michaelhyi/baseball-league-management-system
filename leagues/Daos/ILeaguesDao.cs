using Models;

namespace Daos;
public interface ILeaguesDao
{
    public Task<int> CreateLeagueAsync(string name);
    public Task<League?> GetLeagueAsync(int id);
    public Task UpdateLeagueAsync(int id, string name);
    public Task DeleteLeagueAsync(int id);
}