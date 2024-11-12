package main

import (
	"errors"
	"fmt"
	"time"

	pb "github.com/michaelhyi/baseball-league-management-system/games/proto"
)

func validateCreateGameRequest(in *pb.CreateGameRequest) (time.Time, error) {
	var noop time.Time

	if in.GetHomeTeamId() <= 0 {
		return noop, errors.New("invalid home team id: cannot be negative or 0")
	}

	if in.GetAwayTeamId() <= 0 {
		return noop, errors.New("invalid away team id: cannot be negative or 0")
	}

	if in.GetHomeTeamScore() < 0 {
		return noop, errors.New("invalid home team score: cannot be negative")
	}

	if in.GetAwayTeamScore() < 0 {
		return noop, errors.New("invalid away team score: cannot be negative")
	}

	if len(in.GetDate()) == 0 {
		return noop, errors.New("invalid date: cannot be empty")
	}

	date, err := parseStringToTime(in.GetDate())

	if err != nil {
		return noop, fmt.Errorf("error parsing date: %v", err)
	}

	if len(in.GetLocation()) == 0 {
		return noop, errors.New("invalid location: cannot be empty")
	}

	return date, nil
}

func validateUpdateGameRequest(in *pb.UpdateGameRequest) (time.Time, error) {
	var noop time.Time

	if in.GetId() <= 0 {
		return noop, fmt.Errorf("invalid game id: cannot be negative or 0")
	}

	date, err := validateCreateGameRequest(&pb.CreateGameRequest{
		HomeTeamId:    in.GetHomeTeamId(),
		AwayTeamId:    in.GetAwayTeamId(),
		HomeTeamScore: in.GetHomeTeamScore(),
		AwayTeamScore: in.GetAwayTeamScore(),
		Date:          in.GetDate(),
		Location:      in.GetLocation(),
	})

	if err != nil {
		return noop, err
	}

	return date, nil
}

func parseStringToTime(s string) (time.Time, error) {
	format := "DD-MM-YYYY HH:mm:ss"
	return time.Parse(format, s)
}
