<div align="center">
    <h2>Baseball League and Stats Management System</h2>
</div>

<hr />

## About

This app manages baseball leagues, teams, player profiles, game logs, and stats.
It provides insights into player performance, league standings, and match results, making it suitable for both league management and statistical analysis.

### Tech Stack

- Python/Django
- C#/.NET
- Go/HTTP/gRPC
- SQL
- Swift/Kotlin
- MySQL

This project will follow a microservices-based architecture.

## Development

### Requirements

#### API Gateway (Go/HTTP)

#### Players (Python/Django)

<details>
    <summary>Create Player</summary>

```bash
curl -i -X POST http://localhost:8080/v1/players \
    -H 'Content-Type: application/json' \
    -d '{
            "name": "Michael Yi",
            "age": 19,
            "height": "5\u0027 10\"",
            "weight": 140,
            "position": "Shortstop",
            "teamId": 1
    }'
```

</details>

<details>
    <summary>Get Player</summary>

```bash
curl -i http://localhost:8080/v1/players/<id>
```

</details>

<details>
    <summary>Get Players by Team ID</summary>

```bash
curl -i http://localhost:8080/v1/players?teamId=<id>
```

</details>


<details>
    <summary>Update Player</summary>

```bash
curl -i -X PATCH http://localhost:8080/v1/players/<id> \
    -H 'Content-Type: application/json' \
    -d '{
            "name": "Michael Yi",
            "age": 19,
            "height": "5\u0027 10\"",
            "weight": 140,
            "position": "Shortstop",
            "teamId": 1
    }'
```

</details>

<details>
    <summary>Delete Player</summary>

```bash
curl -i -X DELETE http://localhost:8080/v1/players/<id>
```

</details>

#### Teams (C#/.NET)

<details>
    <summary>Create Team</summary>

```bash
curl -i -X POST http://localhost:8080/v1/teams \
    -H 'Content-Type: application/json' \
    -d '{
        "name": "Los Angeles Dodgers",
        "leagueId": 1
    }'
```

</details>

<details>
    <summary>Get Team</summary>

```bash
curl -i http://localhost:8080/v1/teams/<id>
```

</details>

<details>
    <summary>Get Team With Roster</summary>

```bash
curl -i http://localhost:8080/v1/teams/with-roster/<id>
```

</details>

<details>
    <summary>Update Team</summary>

```bash
curl -i -X PATCH http://localhost:8080/v1/teams/<id> \
    -H 'Content-Type: application/json' \
    -d '{
        "name": "New York Yankees",
        "leagueId": 2
    }'
```

</details>

<details>
    <summary>Delete Team</summary>

```bash
curl -i -X DELETE http://localhost:8080/v1/teams/<id>
```

</details>

#### Games (Go + gRPC)
- [ ] `POST /v1/games`
- [ ] `GET /v1/games/{id}`
- [ ] `PATCH /v1/games/{id}`
- [ ] `DELETE /v1/games/{id}`

#### Stats (Python/Django)
- [ ] `POST /v1/stats`
- [ ] `GET /v1/stats/{id}`
- [ ] `PATCH /v1/stats/{id}`
- [ ] `DELETE /v1/stats/{id}`

#### Leagues (C#/.NET)
- [ ] `POST /v1/leagues`
- [ ] `GET /v1/leagues/{id}`
- [ ] `PATCH /v1/leagues/{id}`
- [ ] `DELETE /v1/leagues/{id}`

### Backlog
- [ ] Refactor Django Design Patterns
- [ ] Resolve TODO's
- [ ] Return ID When Created Entity (also update)
- [ ] Consistent Naming Conventions Across Tables
- [ ] Player # Column for Players
- [ ] DOB Column for Players
- [ ] Use Django's ORM or Raw Feature?
- [ ] Implement Games Service
    - [ ] CRUD for Games
- [ ] Implement Stats Service
- [ ] Implement Leagues Service
- [ ] Unit Test Teams Service
- [ ] Finish Unit Tests for Players Service
- [ ] Test API Gateway
- [ ] Test Downstream Proxy for API Gateway
- [ ] Implement & Test gRPC Support for API Gateway
- [ ] JWT Auth, Rate Limiting, Logging, Monitoring, Data Validation, Tracing, Pagination, Caching

