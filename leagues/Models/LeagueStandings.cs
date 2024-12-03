namespace Models;

public class LeagueStandings
{
    public int Id { get; set; }
    public string Name { get; set; }
    public IEnumerable<TeamStandings> Standings { get; set; }

    public LeagueStandings(
        int leagueId,
        string leagueName,
        IEnumerable<TeamStandings> leagueStandings
    )
    {
        Id = leagueId;
        Name = leagueName;
        Standings = leagueStandings;
    }
}