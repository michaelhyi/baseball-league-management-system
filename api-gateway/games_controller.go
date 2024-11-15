package main

import (
	"context"
	"encoding/json"
	"io"
	"log"
	"net/http"
	"strconv"
	"strings"
	"time"

	pb "github.com/michaelhyi/baseball-league-management-system/api-gateway/proto"
	emptypb "google.golang.org/protobuf/types/known/emptypb"
)

type GamesController struct {
	GamesServiceClient pb.GamesServiceClient
}

func (c *GamesController) Handler(w http.ResponseWriter, r *http.Request) {
	log.Printf("%s %s\n", r.Method, r.URL.Path)
	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	if r.Method == http.MethodPost && r.URL.Path == "/v1/games" {
		body, err := io.ReadAll(r.Body)
		defer r.Body.Close()
		if err != nil {
			log.Printf("error parsing http request body: %v", err)
			w.WriteHeader(http.StatusInternalServerError)
			return
		}

		req := &pb.CreateGameRequest{}
		if err := json.Unmarshal(body, req); err != nil {
			log.Printf("error parsing http request body json: %v", err)
            log.Printf("body: %s", body)
			w.WriteHeader(http.StatusInternalServerError)
			return
		}

		resp, err := c.SendCreateGameRequest(ctx, req)
		if err != nil {
			log.Printf("error sending create game request: %v", err)
			w.WriteHeader(http.StatusInternalServerError)
			return
		}

		b, err := json.Marshal(resp)
		if err != nil {
			log.Printf("error converting grpc res to json: %v", err)
			w.WriteHeader(http.StatusInternalServerError)
			return
		}

		w.WriteHeader(http.StatusCreated)
		w.Header().Set("Content-Type", "application/json")
		w.Write(b)
		return
	}

	if r.Method == http.MethodGet && strings.HasPrefix(r.URL.Path, "/v1/games/") {
		id, err := strconv.Atoi(strings.TrimPrefix(r.URL.Path, "/v1/games/"))
		if err != nil {
			log.Printf("error parsing game id: %v", err)
			w.WriteHeader(http.StatusInternalServerError)
			return
		}

		resp, err := c.SendGetGameRequest(ctx, &pb.GameId{Id: int32(id)})
		if err != nil {
			log.Printf("error sending get game request: %v", err)
			w.WriteHeader(http.StatusInternalServerError)
			return
		}

		b, err := json.Marshal(resp)
		if err != nil {
			log.Printf("error converting grpc res to json: %v", err)
			w.WriteHeader(http.StatusInternalServerError)
			return
		}

		w.WriteHeader(http.StatusOK)
		w.Header().Set("Content-Type", "application/json")
		w.Write(b)
		return
	}

	if r.Method == http.MethodPatch && strings.HasPrefix(r.URL.Path, "/v1/games/") {
        id, err := strconv.Atoi(strings.TrimPrefix(r.URL.Path, "/v1/games/"))
		if err != nil {
			log.Printf("error parsing game id: %v", err)
			w.WriteHeader(http.StatusInternalServerError)
			return
		}

		body, err := io.ReadAll(r.Body)
		defer r.Body.Close()
		if err != nil {
			log.Printf("error parsing http request body: %v", err)
			w.WriteHeader(http.StatusInternalServerError)
			return
		}

		req := &pb.UpdateGameRequest{}
		if err := json.Unmarshal(body, req); err != nil {
			log.Printf("error parsing http request body json: %v", err)
			w.WriteHeader(http.StatusInternalServerError)
			return
		}
        req.Id = int32(id)

		_, err = c.SendUpdateGameRequest(ctx, req)
		if err != nil {
			log.Printf("error sending update game request: %v", err)
			w.WriteHeader(http.StatusInternalServerError)
			return
		}

		w.WriteHeader(http.StatusNoContent)
		return
	}

	if r.Method == http.MethodDelete && strings.HasPrefix(r.URL.Path, "/v1/games/") {
		id, err := strconv.Atoi(strings.TrimPrefix(r.URL.Path, "/v1/games/"))
		if err != nil {
			log.Printf("error parsing game id: %v", err)
			w.WriteHeader(http.StatusInternalServerError)
			return
		}

		_, err = c.SendDeleteGameRequest(ctx, &pb.GameId{Id: int32(id)})
		if err != nil {
			log.Printf("error sending delete game request: %v", err)
			w.WriteHeader(http.StatusInternalServerError)
			return
		}

		w.WriteHeader(http.StatusNoContent)
		return
	}

	// TODO: throw 404
	w.WriteHeader(http.StatusNotFound)
}

func (c *GamesController) SendCreateGameRequest(ctx context.Context, req *pb.CreateGameRequest) (*pb.GameId, error) {
	r, err := c.GamesServiceClient.CreateGame(ctx, req)
	return r, err
}

func (c *GamesController) SendGetGameRequest(ctx context.Context, req *pb.GameId) (*pb.GetGameResponse, error) {
	r, err := c.GamesServiceClient.GetGame(ctx, req)
	return r, err
}

func (c *GamesController) SendUpdateGameRequest(ctx context.Context, req *pb.UpdateGameRequest) (*emptypb.Empty, error) {
	r, err := c.GamesServiceClient.UpdateGame(ctx, req)
	return r, err
}

func (c *GamesController) SendDeleteGameRequest(ctx context.Context, req *pb.GameId) (*emptypb.Empty, error) {
	r, err := c.GamesServiceClient.DeleteGame(ctx, req)
	return r, err
}
