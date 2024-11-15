package main

import (
	"database/sql"
	"fmt"
	"log"
	"time"
)

type DbAccessor interface {
	CreateGame(homeTeamId int32, awayTeamId int32, homeTeamScore int32, awayTeamScore int32, date time.Time, location string) (int32, error)
	GetGame(id int32) (Game, error)
	UpdateGame(id int32, homeTeamId int32, awayTeamId int32, homeTeamScore int32, awayTeamScore int32, date time.Time, location string) error
	DeleteGame(id int32) error
}

type Dao struct {
	db *sql.DB
}

type Game struct {
	ID            int32
	HomeTeamID    int32
	AwayTeamID    int32
	HomeTeamScore int32
	AwayTeamScore int32
	Date          time.Time
	Location      string
	CreatedAt     time.Time
	UpdatedAt     time.Time
}

func (d *Dao) CreateGame(
	homeTeamId int32,
	awayTeamId int32,
	homeTeamScore int32,
	awayTeamScore int32,
	date time.Time,
	location string,
) (int32, error) {
	log.Printf(`dao received CreateGame request with
        homeTeamId %d, awayTeamId %d, homeTeamScore %d, awayTeamScore %d, date %v, location %s\n`,
		homeTeamId, awayTeamId, homeTeamScore, awayTeamScore, date, location,
	)

	result, err := d.db.Exec(
		`INSERT INTO games (home_team_id, away_team_id, home_team_score, away_team_score, date, location)
        VALUES (?, ?, ?, ?, ?, ?)`,
		homeTeamId, awayTeamId, homeTeamScore, awayTeamScore, date, location,
	)

	if err != nil {
		return 0, fmt.Errorf("error trying to insert into games table: %v", err)
	}

	id, err := result.LastInsertId()

	if err != nil {
		return 0, fmt.Errorf("error getting last inserted id: %v", err)
	}

	return int32(id), nil
}

func (d *Dao) GetGame(id int32) (Game, error) {
	log.Printf("dao received GetGame request with id %d\n", id)

	var game Game

	row := d.db.QueryRow("SELECT * FROM games WHERE id = ? LIMIT 1", id)

	if err := row.Scan(
		&game.ID,
		&game.HomeTeamID,
		&game.AwayTeamID,
		&game.HomeTeamScore,
		&game.HomeTeamScore,
		&game.Date,
		&game.Location,
		&game.CreatedAt,
		&game.UpdatedAt,
	); err != nil {
		if err == sql.ErrNoRows {
			return game, fmt.Errorf("game not found")
		}

		return game, fmt.Errorf("error when fetching game %v", err)
	}

	return game, nil
}

func (d *Dao) UpdateGame(
	id int32,
	homeTeamId int32,
	awayTeamId int32,
	homeTeamScore int32,
	awayTeamScore int32,
	date time.Time,
	location string,
) error {
	log.Printf(
		`dao received UpdateGame request with
        id %d, homeTeamId %d, awayTeamId %d, homeTeamScore %d,
        awayTeamScore %d, date %v, location %s\n`,
		id, homeTeamId, awayTeamId, homeTeamScore, awayTeamScore, date, location,
	)

	_, err := d.db.Exec(
		`UPDATE games SET home_team_id=?, away_team_id=?,
        home_team_score=?, away_team_score=?, date=?, location=?
        WHERE id=?`,
		homeTeamId, awayTeamId, homeTeamScore, awayTeamScore, date, location, id,
	)

	if err != nil {
		return fmt.Errorf("error trying to update games table: %v", err)
	}

	return nil
}

func (d *Dao) DeleteGame(id int32) error {
	log.Printf("dao received DeleteGame request with id %d\n", id)

	_, err := d.db.Exec(`DELETE FROM games WHERE id=?`, id)

	if err != nil {
		return fmt.Errorf("error trying to delete from games table: %v", err)
	}

	return nil
}
