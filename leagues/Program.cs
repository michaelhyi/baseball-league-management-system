using Daos;
using Data;
using leagues.Controllers;
using Microsoft.EntityFrameworkCore;
using Services;

var builder = WebApplication.CreateBuilder(args);

var connectionString = builder.Configuration.GetConnectionString("DefaultConnection");
builder.Services.AddDbContext<ApplicationDbContext>(options =>
{
    options.UseMySql(connectionString, ServerVersion.AutoDetect(connectionString));
});


// Add services to the container.
builder.Services.AddGrpc();
builder.Services.AddScoped<ILeaguesDao, LeaguesDao>();
builder.Services.AddScoped<ILeaguesService, LeaguesService>();

var app = builder.Build();

// Configure the HTTP request pipeline.
app.MapGrpcService<LeaguesController>();
app.MapGet("/", () => "Communication with gRPC endpoints must be made through a gRPC client. To learn how to create a client, visit: https://go.microsoft.com/fwlink/?linkid=2086909");

app.Run();
