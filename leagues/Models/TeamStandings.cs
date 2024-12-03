using System.ComponentModel.DataAnnotations.Schema;

namespace Models;

public class TeamStandings
{
    public int Id { get; set; }
    public required string Name { get; set; }
    public uint Wins { get; set; }
    public uint Losses { get; set; }

    [Column("winning_percentage")]
    public float WinningPercentage { get; set; }

    [Column("runs_scored")]
    public int RunsScored { get; set; }

    [Column("runs_allowed")]
    public int RunsAllowed { get; set; }

    [Column("run_differential")]
    public int RunDifferential { get; set; }

    [Column("home_record")]
    public string HomeRecord { get; set; }

    [Column("away_record")]
    public string AwayRecord { get; set; }
}