using Google.Protobuf.WellKnownTypes;
using Grpc.Core;
using Leagues.GrpcModels;
using Models;
using Services;

namespace leagues.Controllers;

public class LeaguesController : Leagues.GrpcModels.LeaguesService.LeaguesServiceBase
{
    private readonly ILogger<LeaguesController> _logger;
    private readonly ILeaguesService _service;

    public LeaguesController(ILogger<LeaguesController> logger, ILeaguesService service)
    {
        _logger = logger;
        _service = service;
    }

    public override async Task<LeagueId> CreateLeague(CreateLeagueRequest req, ServerCallContext context)
    {
        _logger.LogInformation("controller received request to create league with name {name}", req.Name);
        try
        {
            int id = await _service.CreateLeague(req.Name);
            _logger.LogInformation("controller created league with id {id}", id);
            return new LeagueId { Id = id };
        }
        catch (ArgumentException ex)
        {
            _logger.LogError("error creating league with name {name}: {message}", req.Name, ex.Message);
            throw new RpcException(new Status(StatusCode.InvalidArgument, ex.Message));
        }
        catch (Exception ex)
        {
            _logger.LogError("error creating league with name {name}: {message}", req.Name, ex.Message);
            throw new RpcException(new Status(StatusCode.Unknown, ex.Message));
        }
    }

    public override async Task<GetLeagueResponse> GetLeague(LeagueId req, ServerCallContext context)
    {
        _logger.LogInformation("controller received request to get league with id {leagueId}", req.Id);
        try
        {
            League league = await _service.GetLeague(req.Id);
            _logger.LogInformation("controller retrieved league with id {leagueId}", req.Id);
            return new GetLeagueResponse
            {
                Id = league.Id,
                Name = league.Name
            };
        }
        catch (ArgumentException ex)
        {
            _logger.LogError("error finding league with id {leagueId}: {message}", req.Id, ex.Message);
            throw new RpcException(new Status(StatusCode.InvalidArgument, ex.Message));
        }
        catch (KeyNotFoundException ex)
        {
            _logger.LogError("error finding league with id {leagueId}: {message}", req.Id, ex.Message);
            throw new RpcException(new Status(StatusCode.NotFound, ex.Message));
        }
        catch (Exception ex)
        {
            _logger.LogError("error finding league with id {leagueId}: {message}", req.Id, ex.Message);
            throw new RpcException(new Status(StatusCode.Unknown, ex.Message));
        }
    }

    public override async Task<GetLeagueStandingsResponse> GetLeagueStandings(
        LeagueId req, ServerCallContext context)
    {
        _logger.LogInformation("controller received request to get standings for league with id {leagueId}", req.Id);
        try
        {
            LeagueStandings leagueStandings = await _service.GetLeagueStandings(req.Id);
            _logger.LogInformation("controller retrieved standings for league with id {leagueId}", req.Id);
            GetLeagueStandingsResponse res = new GetLeagueStandingsResponse
            {
                Id = leagueStandings.Id,
                Name = leagueStandings.Name,
            };

            foreach (Models.TeamStandings team in leagueStandings.Standings)
            {
                res.Standings.Add(
                    new Leagues.GrpcModels.TeamStandings
                    {
                        Id = team.Id,
                        Name = team.Name,
                        Wins = team.Wins,
                        Losses = team.Losses,
                        WinningPercentage = team.WinningPercentage,
                        RunsScored = team.RunsScored,
                        RunsAllowed = team.RunsAllowed,
                        RunDifferential = team.RunDifferential,
                        HomeRecord = team.HomeRecord,
                        AwayRecord = team.AwayRecord
                    }
                );
            }

            return res;
        }
        catch (ArgumentException ex)
        {
            _logger.LogError("error finding standings for league with id {leagueId}: {message}", req.Id, ex.Message);
            throw new RpcException(new Status(StatusCode.InvalidArgument, ex.Message));
        }
        catch (KeyNotFoundException ex)
        {
            _logger.LogError("error finding standings for league with id {leagueId}: {message}", req.Id, ex.Message);
            throw new RpcException(new Status(StatusCode.NotFound, ex.Message));
        }
        catch (Exception ex)
        {
            _logger.LogError("error finding standings for league with id {leagueId}: {message}", req.Id, ex.Message);
            throw new RpcException(new Status(StatusCode.Unknown, ex.Message));
        }
    }

    public override async Task<Empty> UpdateLeague(UpdateLeagueRequest req, ServerCallContext context)
    {
        _logger.LogInformation("controller received update request for league with id {leagueId} and name {name}", req.Id, req.Name);
        try
        {
            await _service.UpdateLeague(req.Id, req.Name);
            _logger.LogInformation("controller updated league with id {leagueId} and name {name}", req.Id, req.Name);
            return new Empty();
        }
        catch (ArgumentException ex)
        {
            _logger.LogError("error updating league with id {leagueId}: {message}", req.Id, ex.Message);
            throw new RpcException(new Status(StatusCode.InvalidArgument, ex.Message));
        }
        catch (KeyNotFoundException ex)
        {
            _logger.LogError("error updating league with id {leagueId}: {message}", req.Id, ex.Message);
            throw new RpcException(new Status(StatusCode.NotFound, ex.Message));
        }
        catch (Exception ex)
        {
            _logger.LogError("error updating league with id {leagueId}: {message}", req.Id, ex.Message);
            throw new RpcException(new Status(StatusCode.Unknown, ex.Message));
        }
    }

    public override async Task<Empty> DeleteLeague(LeagueId req, ServerCallContext context)
    {
        _logger.LogInformation("controller received delete request for league with id {leagueId}", req.Id);
        try
        {
            await _service.DeleteLeague(req.Id);
            _logger.LogInformation("controller deleted league with id {leagueId}", req.Id);
            return new Empty();
        }
        catch (ArgumentException ex)
        {
            _logger.LogError("error deleting league with id {leagueId}: {message}", req.Id, ex.Message);
            throw new RpcException(new Status(StatusCode.InvalidArgument, ex.Message));
        }
        catch (KeyNotFoundException ex)
        {
            _logger.LogError("error deleting league with id {leagueId}: {message}", req.Id, ex.Message);
            throw new RpcException(new Status(StatusCode.NotFound, ex.Message));
        }
        catch (Exception ex)
        {
            _logger.LogError("error deleting league with id {leagueId}: {message}", req.Id, ex.Message);
            throw new RpcException(new Status(StatusCode.Unknown, ex.Message));
        }
    }
}
