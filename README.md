<div align="center">
    <h2>Baseball League and Stats Management System</h2>
</div>

<hr />

## About

This app manages baseball leagues, teams, player profiles, game logs, and stats. It provides insights into player performance, league standings, and match results, making it suitable for both league management and statistical analysis.

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

This project will follow a microservices-based architecture. There will be 6 services total, 5 of which are listed below and the 6th being an API Gateway.
The API gateway will be made using Go and another one of the services will be made using Go + gRPC.
Two of the services will be made using C#, .NET, and gRPC, and the remaining two will be made using Python, Django, and gRPC.

## Development

### Requirements

#### Players
- [ ] `POST /v1/players`
- [ ] `GET /v1/players/{id}`
- [ ] `PATCH /v1/players/{id}`
- [ ] `DELETE /v1/players/{id}`

#### Teams
- [ ] `POST /v1/teams`
- [ ] `GET /v1/teams/{id}`
- [ ] `PATCH /v1/teams/{id}`
- [ ] `DELETE /v1/teams/{id}`

#### Games
- [ ] `POST /v1/games`
- [ ] `GET /v1/games/{id}`
- [ ] `PATCH /v1/games/{id}`
- [ ] `DELETE /v1/games/{id}`

#### Stats 
- [ ] `POST /v1/stats`
- [ ] `GET /v1/stats/{id}`
- [ ] `PATCH /v1/stats/{id}`
- [ ] `DELETE /v1/stats/{id}`

#### Leagues
- [ ] `POST /v1/leagues`
- [ ] `GET /v1/leagues/{id}`
- [ ] `PATCH /v1/leagues/{id}`
- [ ] `DELETE /v1/leagues/{id}`

