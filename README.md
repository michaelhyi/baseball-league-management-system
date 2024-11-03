<div align="center">
    <h2>Baseball League and Stats Management System</h2>
</div>

<hr />

## About

This app manages baseball leagues, teams, player profiles, game logs, and stats.
It provides insights into player performance, league standings, and match results, making it suitable for both league management and statistical analysis.

### Tech Stack

- Python
- C#
- Go
- gRPC
- SQL
- Swift
- Kotlin
- Django
- .NET
- MySQL

This project will follow a microservices-based architecture.

## Development

### Requirements

#### API Gateway (Go)

#### Players (Python + Django)

<details>
    <summary>Create Player</summary>
```bash
curl -X POST http://localhost:8000/v1/players \
-d '{}'
```
</details>

<details>
    <summary>Get Player</summary>
```bash
curl http://localhost:8000/v1/players/<id>
```
</details>

<details>
    <summary>Update Player</summary>
```bash
curl -X PATCH http://localhost:8000/v1/players/<id> \
-d '{}'
```
</details>

<details>
    <summary>Delete Player</summary>
```bash
curl -X DELETE http://localhost:8000/v1/players/<id>
```
</details>

#### Teams (C# + .NET)
- [ ] `POST /v1/teams`
- [ ] `GET /v1/teams/{id}`
- [ ] `PATCH /v1/teams/{id}`
- [ ] `DELETE /v1/teams/{id}`

#### Games (Go + gRPC)
- [ ] `POST /v1/games`
- [ ] `GET /v1/games/{id}`
- [ ] `PATCH /v1/games/{id}`
- [ ] `DELETE /v1/games/{id}`

#### Stats (Python + gRPC)
- [ ] `POST /v1/stats`
- [ ] `GET /v1/stats/{id}`
- [ ] `PATCH /v1/stats/{id}`
- [ ] `DELETE /v1/stats/{id}`

#### Leagues (C# + gRPC)
- [ ] `POST /v1/leagues`
- [ ] `GET /v1/leagues/{id}`
- [ ] `PATCH /v1/leagues/{id}`
- [ ] `DELETE /v1/leagues/{id}`

### Backlog
- [ ] Implement gRPC Support for API Gateway
- [ ] Test Downstream Proxy for API Gateway
- [ ] Implement, Refactor, Test Players Service
- [ ] JWT Auth, Rate Limiting, Logging, Monitoring, Data Validation, Tracing, Pagination, Caching
