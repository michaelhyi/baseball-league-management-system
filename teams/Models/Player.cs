using System.Text.Json.Serialization;

namespace teams.Models;

public class Player
{
    [property: JsonPropertyName("id")]
    public int Id { get; set; }
    [property: JsonPropertyName("name")]
    public string Name { get; set; }
    [property: JsonPropertyName("age")]
    public int Age { get; set; }
    [property: JsonPropertyName("height")]
    public string Height { get; set; }
    [property: JsonPropertyName("weight")]
    public int Weight { get; set; }
    [property: JsonPropertyName("position")]
    public string Position { get; set; }
    [property: JsonPropertyName("teamId")]
    public int TeamId { get; set; }
    [property: JsonPropertyName("createdAt")]
    public string CreatedAt { get; set; }
    [property: JsonPropertyName("updatedAt")]
    public string UpdatedAt { get; set; }

    public Player
    (
        int id,
        string name,
        int age,
        string height,
        int weight,
        string position,
        int teamId,
        string createdAt,
        string updatedAt
    )
    {
        Id = id;
        Name = name;
        Age = age;
        Height = height;
        Weight = weight;
        Position = position;
        TeamId = teamId;
        CreatedAt = createdAt;
        UpdatedAt = updatedAt;
    }
}