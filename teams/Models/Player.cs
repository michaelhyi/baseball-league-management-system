using System.ComponentModel.DataAnnotations.Schema;

namespace teams.Models;

public class Player
{
    public int Id { get; set; }
    public string Name { get; set; }
    public int Age { get; set; }
    public string Height { get; set; }
    public int Weight { get; set; }
    public string Position { get; set; }
    [Column("team_id")]
    public int TeamId { get; set; }
    [Column("created_at")]
    public DateTime CreatedAt { get; set; }
    [Column("updated_at")]
    public DateTime UpdatedAt { get; set; }

    public Player
    (
        int id,
        string name,
        int age,
        string height,
        int weight,
        string position,
        int teamId,
        DateTime createdAt,
        DateTime updatedAt
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