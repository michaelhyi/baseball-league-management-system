package games

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
)

type GamesController struct {
	GamesServiceClient pb.GamesServiceClient
}

func (c *GamesController) Handler(w http.ResponseWriter, r *http.Request) {
	log.Printf("%s %s\n", r.Method, r.URL.Path)
	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	if r.Method == http.MethodPost && r.URL.Path == "/v1/games" {
		c.handleCreateGame(w, r, ctx)
		return
	}

	if r.Method == http.MethodGet && strings.HasPrefix(r.URL.Path, "/v1/games/") {
		c.handleGetGame(w, r, ctx)
		return
	}

	if r.Method == http.MethodPatch && strings.HasPrefix(r.URL.Path, "/v1/games/") {
		c.handleUpdateGame(w, r, ctx)
		return
	}

	if r.Method == http.MethodDelete && strings.HasPrefix(r.URL.Path, "/v1/games/") {
		c.handleDeleteGame(w, r, ctx)
		return
	}

	// TODO: throw 404
	w.WriteHeader(http.StatusNotFound)
}

func (c *GamesController) handleCreateGame(w http.ResponseWriter, r *http.Request, ctx context.Context) {
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

	resp, err := c.GamesServiceClient.CreateGame(ctx, req)
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

func (c *GamesController) handleGetGame(w http.ResponseWriter, r *http.Request, ctx context.Context) {
	id, err := strconv.Atoi(strings.TrimPrefix(r.URL.Path, "/v1/games/"))
	if err != nil {
		log.Printf("error parsing game id: %v", err)
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	resp, err := c.GamesServiceClient.GetGame(ctx, &pb.GameId{Id: int32(id)})
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

func (c *GamesController) handleUpdateGame(w http.ResponseWriter, r *http.Request, ctx context.Context) {
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

	_, err = c.GamesServiceClient.UpdateGame(ctx, req)
	if err != nil {
		log.Printf("error sending update game request: %v", err)
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	w.WriteHeader(http.StatusNoContent)
	return
}

func (c *GamesController) handleDeleteGame(w http.ResponseWriter, r *http.Request, ctx context.Context) {
	id, err := strconv.Atoi(strings.TrimPrefix(r.URL.Path, "/v1/games/"))
	if err != nil {
		log.Printf("error parsing game id: %v", err)
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	_, err = c.GamesServiceClient.DeleteGame(ctx, &pb.GameId{Id: int32(id)})
	if err != nil {
		log.Printf("error sending delete game request: %v", err)
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	w.WriteHeader(http.StatusNoContent)
	return
}
