namespace teams.Models;

public class Team
{
    public int Id { get; set; }
    public required string Name { get; set; }
    public int LeagueId { get; set; }
    public DateOnly CreatedAt { get; set; }
    public DateOnly UpdatedAt { get; set; }
}