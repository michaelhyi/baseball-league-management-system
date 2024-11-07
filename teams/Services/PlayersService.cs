using System.Net.Http.Headers;
using System.Text;
using System.Text.Json;
using teams.Constants;
using teams.Models;

namespace teams.Services;

public class PlayersService : IPlayersService
{
    private readonly ILogger<PlayersService> _logger;
    private readonly HttpClient _httpClient;

    public PlayersService(ILogger<PlayersService> logger, HttpClient httpClient)
    {
        _logger = logger;
        _httpClient = httpClient;
    }

    public async Task<IEnumerable<Player>> GetPlayersByTeamId(int teamId)
    {
        _httpClient.DefaultRequestHeaders.Accept.Clear();
        _httpClient.DefaultRequestHeaders.Accept.Add
        (
            new MediaTypeWithQualityHeaderValue("application/json")
        );

        await using Stream response = await _httpClient.GetStreamAsync
        (
            ApiConstants.PlayersApiUrl + "?teamId=" + teamId
        );

        GetPlayersByTeamIdResponse? wrapperResponse = await JsonSerializer
                .DeserializeAsync<GetPlayersByTeamIdResponse>(response);

        if (wrapperResponse == null)
        {
            throw new Exception("failed to retrieve players");
        }

        IEnumerable<Player> players = wrapperResponse.Players.Select
        (
            playerJson => JsonSerializer.Deserialize<Player>(playerJson)
        )
        .OfType<Player>().ToList();

        return players;
    }
}
