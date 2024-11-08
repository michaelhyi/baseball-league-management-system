using teams.Models;

public class TeamWithRoster
{
    public Team Team { get; set; }
    public IEnumerable<Player> Roster { get; set; }

    public TeamWithRoster(Team team, IEnumerable<Player> roster)
    {
        Team = team;
        Roster = roster;
    }
}