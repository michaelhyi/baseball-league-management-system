namespace teams.Models;

public class CreateTeamResponse
{
    public int Id { get; set; }

    public CreateTeamResponse(int id)
    {
        Id = id;
    }
}