using System.ComponentModel.DataAnnotations.Schema;

namespace teams.Models;

public class Team
{
    public int Id { get; set; }
    public string Name { get; set; }
    [Column("league_id")]
    public int LeagueId { get; set; }
    [Column("created_at")]
    public DateTime CreatedAt { get; set; }
    [Column("updated_at")]
    public DateTime UpdatedAt { get; set; }
}