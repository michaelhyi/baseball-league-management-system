using System.Text.Json.Serialization;

namespace teams.Models;

public class GetPlayersByTeamIdResponse
{
    [property: JsonPropertyName("players")]
    public IEnumerable<string> Players { get; set; }

    public GetPlayersByTeamIdResponse(IEnumerable<string> players)
    {
        Players = players;
    }
}