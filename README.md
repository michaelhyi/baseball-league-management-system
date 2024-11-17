<div align="center">
    <h2>Baseball League and Stats Management System</h2>
</div>

<hr />

## About

This app manages baseball leagues, teams, player profiles, game logs, and stats.
It provides insights into player performance, league standings, and match results, making it suitable for both league management and statistical analysis.

### Tech Stack

- Python/Django
- Go
- C#/.NET
- SQL
- gRPC
- MySQL
- Redis
- Swift/Kotlin

This project follows a microservices-based architecture.

## Development

### Requirements

<details>
    <summary>API Gateway (Go/HTTP/gRPC)</summary>
</details>

<details>
    <summary>Players (Python/Django)</summary>

##### Endpoints

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

##### Endpoints

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

<details>
    <summary>Games (Go/gRPC)</summary>

##### Endpoints

<details>
    <summary>Create Game</summary>

```bash
curl -i -X POST http://localhost:8080/v1/games \
    -H 'Content-Type: application/json' \
    -d '{
        "homeTeamId": 1,
        "awayTeamId": 2,
        "homeTeamScore": 5,
        "awayTeamScore": 0,
        "date": "2004-12-14 12:00:00",
        "location": "Irvine, CA"
}'
```
</details>

<details>
    <summary>Get Game</summary>

```bash
curl -i http://localhost:8080/v1/games/<id>
```
</details>

<details>
    <summary>Update Game</summary>

```bash
curl -i -X PATCH http://localhost:8080/v1/games/<id> \
    -H 'Content-Type: application/json' \
    -d '{
        "homeTeamId": 1,
        "awayTeamId": 2,
        "homeTeamScore": 5,
        "awayTeamScore": 0,
        "date": "2004-12-14 12:00:00",
        "location": "Irvine, CA"
}'
```
</details>

<details>
    <summary>Delete Game</summary>

```bash
curl -i -X DELETE http://localhost:8080/v1/games/<id>
```
</details>

</details>

<details>
    <summary>Leagues (C#/.NET/gRPC)</summary>

##### Endpoints

<details>
    <summary>Create League</summary>

```bash
curl -i -X POST http://localhost:8080/v1/leagues \
    -H 'Content-Type: application/json' \
    -d '{
        "name": "Athletic Coast Conference"
}'
```
</details>

<details>
    <summary>Get League</summary>

```bash
curl -i http://localhost:8080/v1/leagues/<id>
```
</details>

<details>
    <summary>Update League</summary>

```bash
curl -i -X PATCH http://localhost:8080/v1/leagues/<id> \
    -H 'Content-Type: application/json' \
    -d '{
        "name": "Athletic Coast Conference"
}'
```
</details>

<details>
    <summary>Delete League</summary>

```bash
curl -i -X DELETE http://localhost:8080/v1/leagues/<id>
```
</details>
</details>

<details>
    <summary>Stats (Python/Django)</summary>

##### Endpoints
<details>
    <summary>Create Batting Stats</summary>

```bash
curl -i -X POST http://localhost:8080/v1/stats/batting \
    -H 'Content-Type: application/json' \
    -d '{
        "playerId": 1,
        "atBats": 4,
        "runs": 1,
        "hits": 2,
        "totalBases": 3,
        "doubles": 1,
        "triples": 0,
        "homeRuns": 0,
        "rbi": 1,
        "walks": 1,
        "strikeouts": 1,
        "stolenBases": 1,
        "hitByPitches": 0,
        "sacFlies": 0
    }'
```
</details>

<details>
    <summary>Create Pitching Stats</summary>

```bash
curl -i -X POST http://localhost:8080/v1/stats/pitching \
    -H 'Content-Type: application/json' \
    -d '{
        "playerId": 1,
        "wins": 1,
        "losses": 0,
        "earnedRuns": 1,
        "games": 1,
        "gamesStarted": 1,
        "saves": 0,
        "inningsPitched": 7,
        "strikeouts": 10,
        "walks": 2,
        "hits": 5
    }'
```
</details>

<details>
    <summary>Get Batting Stats</summary>

```bash
curl -i http://localhost:8080/v1/stats/batting/<player-id>
```
</details>

<details>
    <summary>Get Pitching Stats</summary>

```bash
curl -i http://localhost:8080/v1/stats/pitching/<player-id>
```
</details>

<details>
    <summary>Update Batting Stats</summary>

```bash
curl -i -X PATCH http://localhost:8080/v1/stats/batting/<id> \
    -H 'Content-Type: application/json' \
    -d '{
        "playerId": 1,
        "atBats": 4,
        "runs": 1,
        "hits": 2,
        "totalBases": 3,
        "doubles": 1,
        "triples": 0,
        "homeRuns": 0,
        "rbi": 1,
        "walks": 1,
        "strikeouts": 1,
        "stolenBases": 1,
        "hitByPitches": 0,
        "sacFlies": 0
    }'
```
</details>

<details>
    <summary>Update Pitching Stats</summary>

```bash
curl -i -X PATCH http://localhost:8080/v1/stats/pitching/<id> \
    -H 'Content-Type: application/json' \
    -d '{
        "playerId": 1,
        "wins": 1,
        "losses": 0,
        "earnedRuns": 1,
        "games": 1,
        "gamesStarted": 1,
        "saves": 0,
        "inningsPitched": 7,
        "strikeouts": 10,
        "walks": 2,
        "hits": 5
    }'
```
</details>

<details>
    <summary>Delete Batting Stats</summary>

```bash
curl -i -X DELETE http://localhost:8080/v1/stats/batting/<id>
```
</details>

<details>
    <summary>Delete Pitching Stats</summary>

```bash
curl -i -X DELETE http://localhost:8080/v1/stats/pitching/<id>
```
</details>

</details>

### Backlog
- [ ] API Gateway
    - [ ] gRPC Error Handling
    - [ ] Unit Tests
    - [ ] JWT Auth, Rate Limiting, Logging, Monitoring, Data Validation, Pagination, Caching
- [ ] Players Service
    - [ ] Use Django's Model Submodule?
    - [ ] Resolve TODO's
- [ ] Teams Service
    - [ ] Unit Tests
- [ ] Games Service
    - [ ] Unit Tests
- [ ] Leagues Service
    - [ ] Unit Tests
- [ ] Stats Service
    - [ ] Setup Django App
    - [ ] Basic CRUD for Stats
    - [ ] Unit Tests
- [ ] Setup Complex Queries
- [ ] Distributed MySQL Databases? Sharding / Replication
- [ ] System Design

