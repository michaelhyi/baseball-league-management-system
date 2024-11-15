package main

import (
	"context"
	"fmt"
	"log"

	pb "github.com/michaelhyi/baseball-league-management-system/games/proto"
	"google.golang.org/protobuf/types/known/emptypb"
)

func (s *server) CreateGame(_ context.Context, in *pb.CreateGameRequest) (*pb.GameId, error) {
	log.Printf("gRPC server received CreateGame request: %v", in)

	date, err := validateCreateGameRequest(in)
	if err != nil {
		return nil, err
	}

	id, err := s.dao.CreateGame(
		in.GetHomeTeamId(),
		in.GetAwayTeamId(),
		in.GetHomeTeamScore(),
		in.GetAwayTeamScore(),
		date,
		in.GetLocation(),
	)

	if err != nil {
		return nil, fmt.Errorf("error creating game: %v", err)
	}

	return &pb.GameId{Id: id}, nil
}

func (s *server) GetGame(_ context.Context, in *pb.GameId) (*pb.GetGameResponse, error) {
	log.Printf("gRPC server received GetGame request: %v", in)

	if in.GetId() <= 0 {
		return nil, fmt.Errorf("invalid game id: cannot be negative or 0")
	}

	game, err := s.dao.GetGame(in.GetId())
	if err != nil {
		return nil, fmt.Errorf("error getting game: %v", err)
	}

	return &pb.GetGameResponse{
		Id:            game.ID,
		HomeTeamId:    game.HomeTeamID,
		AwayTeamId:    game.AwayTeamID,
		HomeTeamScore: game.HomeTeamScore,
		AwayTeamScore: game.AwayTeamScore,
		Date:          game.Date.Format("2006-01-02 15:04:05"),
		Location:      game.Location,
	}, nil
}

func (s *server) UpdateGame(_ context.Context, in *pb.UpdateGameRequest) (*emptypb.Empty, error) {
	log.Printf("gRPC server received UpdateGame request: %v", in)

	date, err := validateUpdateGameRequest(in)
	if err != nil {
		return nil, err
	}

	err = s.dao.UpdateGame(
		in.GetId(),
		in.GetHomeTeamId(),
		in.GetAwayTeamId(),
		in.GetHomeTeamScore(),
		in.GetAwayTeamScore(),
		date,
		in.GetLocation(),
	)

	if err != nil {
		return nil, fmt.Errorf("error updating game: %v", err)
	}

	return &emptypb.Empty{}, nil
}

func (s *server) DeleteGame(_ context.Context, in *pb.GameId) (*emptypb.Empty, error) {
	log.Printf("gRPC server received DeleteGame request: %v", in)

	if in.GetId() <= 0 {
		return nil, fmt.Errorf("invalid game id: cannot be negative or 0")
	}

	err := s.dao.DeleteGame(in.GetId())
	if err != nil {
		return nil, fmt.Errorf("error deleting game: %v", err)
	}

	return &emptypb.Empty{}, nil
}
