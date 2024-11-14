package main

import (
	"log"
	"net/http"
	// "google.golang.org/grpc"
	// "google.golang.org/grpc/credentials/insecure"
	// pb "github.com/michaelhyi/baseball-league-management-system/api-gateway/proto"
)

func main() {
	httpClient := &http.Client{}
	playersController := &HttpController{HttpClient: httpClient, DownstreamUrl: "http://localhost:8081"}
	teamsController := &HttpController{HttpClient: httpClient, DownstreamUrl: "http://localhost:8082"}

	//    gamesGrpcConn, err := grpc.NewClient("localhost:8083", grpc.WithTransportCredentials(insecure.NewCredentials()))
	// if err != nil {
	// 	log.Fatalf("did not connect to games grpc server: %v", err)
	// }
	// defer gamesGrpcConn.Close()
	// gamesGrpcClient := pb.NewGamesServiceClient(gamesGrpcConn)

	http.HandleFunc("/v1/players", playersController.Handler)
	http.HandleFunc("/v1/players/", playersController.Handler)
	http.HandleFunc("/v1/teams", teamsController.Handler)
	http.HandleFunc("/v1/teams/", teamsController.Handler)
	// http.HandleFunc("/v1/games", PlayersController)

	log.Printf("Server listening on port 8080")
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		log.Fatalf("Server failed to start: %v", err)
	}
}
