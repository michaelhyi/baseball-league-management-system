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
- Redis

This project follows a microservices-based architecture.

## Development

### Requirements

<details>
    <summary>API Gateway (Go/HTTP/gRPC)</summary>
</details>

<details>
    <summary>Players (Python/Django)</summary>

<details>
    <summary>Create Player</summary>

```bash
curl -i -X POST http://localhost:8080/v1/players \
    -H 'Content-Type: application/json' \
    -d '{
        "name": "Michael Yi",
        "jerseyNumber": "14",
        "dob": "2004-12-14",
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
    <summary>Update Player</summary>

```bash
curl -i -X PATCH http://localhost:8080/v1/players/<id> \
    -H 'Content-Type: application/json' \
    -d '{
        "name": "Michael Yi",
        "jerseyNumber": "14",
        "dob": "2004-12-14",
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

<br/>
</details>

<details>
    <summary>Teams (C#/.NET)</summary>

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
- [ ] API Gateway
    - [ ] Unit Tests
    - [ ] JWT Auth, Rate Limiting, Logging, Monitoring, Data Validation, Tracing, Pagination, Caching
- [ ] Players Service
    - [ ] Use Django's Model Submodule?
    - [ ] Resolve TODO's
- [ ] Teams Service
    - [ ] Unit Tests
- [ ] Games Service
- [ ] Stats Service
- [ ] Leagues Service
- [ ] System Design

