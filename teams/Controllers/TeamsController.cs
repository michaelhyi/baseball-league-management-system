using Microsoft.AspNetCore.Mvc;
using teams.Models;
using teams.Services;

namespace teams.Controllers;

[ApiController]
[Route("/v1/teams")]
public class TeamsController : ControllerBase
{
    private readonly ILogger<TeamsController> _logger;
    private readonly ITeamsService _teamsService;

    public TeamsController(ILogger<TeamsController> logger, ITeamsService teamsService)
    {
        _logger = logger;
        _teamsService = teamsService;
    }

    [HttpPost]
    public async Task<IActionResult> CreateTeam([FromBody] TeamRequest req)
    {
        try
        {
            int id = await _teamsService.CreateTeam(req);
            return StatusCode(201, new CreateTeamResponse(id));
        }
        catch (ArgumentException ex)
        {
            return BadRequest(new ErrorResponse(ex.Message));
        }
        catch (Exception ex)
        {
            return StatusCode(500, new ErrorResponse(ex.Message));
        }
    }

    [HttpGet("{id}")]
    public async Task<IActionResult> GetTeam([FromRoute] int id)
    {
        try
        {
            Team team = await _teamsService.GetTeam(id);
            return Ok(team);
        }
        catch (ArgumentException ex)
        {
            return BadRequest(new ErrorResponse(ex.Message));
        }
        catch (KeyNotFoundException ex)
        {
            return NotFound(new ErrorResponse(ex.Message));
        }
        catch (Exception ex)
        {
            return StatusCode(500, new ErrorResponse(ex.Message));
        }
    }

    [HttpPatch("{id}")]
    public async Task<IActionResult> UpdateTeam([FromRoute] int id, [FromBody] TeamRequest req)
    {
        try
        {
            await _teamsService.UpdateTeam(id, req);
            return Ok();
        }
        catch (ArgumentException ex)
        {
            return BadRequest(new ErrorResponse(ex.Message));
        }
        catch (Exception ex)
        {
            return StatusCode(500, new ErrorResponse(ex.Message));
        }
    }

    [HttpDelete("{id}")]
    public async Task<IActionResult> DeleteTeam([FromRoute] int id)
    {
        try
        {
            await _teamsService.DeleteTeam(id);
            return NoContent();
        }
        catch (ArgumentException ex)
        {
            return BadRequest(new ErrorResponse(ex.Message));
        }
        catch (KeyNotFoundException ex)
        {
            return NotFound(new ErrorResponse(ex.Message));
        }
        catch (Exception ex)
        {
            return StatusCode(500, new ErrorResponse(ex.Message));
        }
    }
}
