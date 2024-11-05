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
            await _teamsService.CreateTeam(req);
            return Created();
        }
        catch (ArgumentException ex)
        {
            return BadRequest(ex.Message);
        }
        catch (Exception ex)
        {
            return StatusCode(500, ex.Message);
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
            return BadRequest(ex.Message);
        }
        catch (KeyNotFoundException ex)
        {
            return NotFound(ex.Message);
        }
        catch (Exception ex)
        {
            return StatusCode(500, ex.Message);
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
            return BadRequest(ex.Message);
        }
        catch (Exception ex)
        {
            return StatusCode(500, ex.Message);
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
            return BadRequest(ex.Message);
        }
        catch (KeyNotFoundException ex)
        {
            return NotFound(ex.Message);
        }
        catch (Exception ex)
        {
            return StatusCode(500, ex.Message);
        }
    }
}
