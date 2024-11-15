package games

import (
	"context"
	"log"
	"net/http"
	"strconv"
	"strings"
	"time"

	pb "github.com/michaelhyi/baseball-league-management-system/api-gateway/proto"
	"github.com/michaelhyi/baseball-league-management-system/api-gateway/rest"
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
	req := &pb.CreateGameRequest{}
	rest.ConvertHttpRequestBodyToObject(w, r, req)

	resp, err := c.GamesServiceClient.CreateGame(ctx, req)
	if err != nil {
		log.Printf("error sending create game request: %v", err)
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	rest.ConvertObjectToHttpResponse(w, resp)
	w.WriteHeader(http.StatusCreated)
	return
}

func (c *GamesController) handleGetGame(w http.ResponseWriter, r *http.Request, ctx context.Context) {
	id, err := rest.GetPathVariableAsInt(r, "/v1/games/")
	if err != nil {
		log.Printf("error parsing game id: %v", err)
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	req := &pb.GameId{Id: int32(id)}
	resp, err := c.GamesServiceClient.GetGame(ctx, req)
	if err != nil {
		log.Printf("error sending get game request: %v", err)
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	rest.ConvertObjectToHttpResponse(w, resp)
	w.WriteHeader(http.StatusOK)
	return
}

func (c *GamesController) handleUpdateGame(w http.ResponseWriter, r *http.Request, ctx context.Context) {
	id, err := rest.GetPathVariableAsInt(r, "/v1/games/")
	if err != nil {
		log.Printf("error parsing game id: %v", err)
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	req := &pb.UpdateGameRequest{}
	rest.ConvertHttpRequestBodyToObject(w, r, req)
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
	id, err := rest.GetPathVariableAsInt(r, "/v1/games/")
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
