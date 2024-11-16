package main

import (
	"log"
	"net/http"

	"github.com/michaelhyi/baseball-league-management-system/api-gateway/leagues"
	pb "github.com/michaelhyi/baseball-league-management-system/api-gateway/proto"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"

	"github.com/michaelhyi/baseball-league-management-system/api-gateway/games"
	"github.com/michaelhyi/baseball-league-management-system/api-gateway/rest"
)

func main() {
	httpClient := &http.Client{}
	playersController := &rest.RestController{HttpClient: httpClient, DownstreamUrl: "http://localhost:8081"}
	teamsController := &rest.RestController{HttpClient: httpClient, DownstreamUrl: "http://localhost:8082"}

	gamesGrpcConn, err := grpc.NewClient("localhost:8083", grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		log.Fatalf("did not connect to games grpc server: %v", err)
	}
	defer gamesGrpcConn.Close()
	gamesGrpcClient := pb.NewGamesServiceClient(gamesGrpcConn)
	gamesController := &games.GamesController{GamesServiceClient: gamesGrpcClient}

	leaguesGrpcConn, err := grpc.NewClient("localhost:8084", grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		log.Fatalf("did not connect to games grpc server: %v", err)
	}
	defer leaguesGrpcConn.Close()
	leaguesGrpcClient := pb.NewLeaguesServiceClient(leaguesGrpcConn)
	leaguesController := &leagues.LeaguesController{LeaguesServiceClient: leaguesGrpcClient}

	http.HandleFunc("/v1/players", playersController.Handler)
	http.HandleFunc("/v1/players/", playersController.Handler)
	http.HandleFunc("/v1/teams", teamsController.Handler)
	http.HandleFunc("/v1/teams/", teamsController.Handler)
	http.HandleFunc("/v1/games", gamesController.Handler)
	http.HandleFunc("/v1/games/", gamesController.Handler)
	http.HandleFunc("/v1/leagues", leaguesController.Handler)
	http.HandleFunc("/v1/leagues/", leaguesController.Handler)

	log.Printf("Server listening on port 8080")
	err = http.ListenAndServe(":8080", nil)
	if err != nil {
		log.Fatalf("Server failed to start: %v", err)
	}
}
