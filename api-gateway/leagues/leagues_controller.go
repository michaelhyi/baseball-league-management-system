package leagues

import (
	"context"
	"log"
	"net/http"
	"strings"
	"time"

	pb "github.com/michaelhyi/baseball-league-management-system/api-gateway/proto"
	"github.com/michaelhyi/baseball-league-management-system/api-gateway/rest"
)

type LeaguesController struct {
	LeaguesServiceClient pb.LeaguesServiceClient
}

func (c *LeaguesController) Handler(w http.ResponseWriter, r *http.Request) {
	log.Printf("%s %s\n", r.Method, r.URL.Path)
	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	if r.Method == http.MethodPost && r.URL.Path == "/v1/leagues" {
		c.handleCreateLeague(w, r, ctx)
		return
	}

	if r.Method == http.MethodGet && !strings.HasPrefix(r.URL.Path, "/v1/leagues/standings/") && strings.HasPrefix(r.URL.Path, "/v1/leagues/") {
		c.handleGetLeague(w, r, ctx)
		return
	}

	if r.Method == http.MethodGet && strings.HasPrefix(r.URL.Path, "/v1/leagues/standings/") {
		c.handleGetLeagueStandings(w, r, ctx)
		return
	}

	if r.Method == http.MethodPatch && strings.HasPrefix(r.URL.Path, "/v1/leagues/") {
		c.handleUpdateLeague(w, r, ctx)
		return
	}

	if r.Method == http.MethodDelete && strings.HasPrefix(r.URL.Path, "/v1/leagues/") {
		c.handleDeleteLeague(w, r, ctx)
		return
	}

	// TODO: throw 404
	w.WriteHeader(http.StatusNotFound)
}

func (c *LeaguesController) handleCreateLeague(w http.ResponseWriter, r *http.Request, ctx context.Context) {
	req := &pb.CreateLeagueRequest{}
	rest.ConvertHttpRequestBodyToObject(w, r, req)

	resp, err := c.LeaguesServiceClient.CreateLeague(ctx, req)
	if err != nil {
		log.Printf("error sending create league request: %v", err)
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	rest.ConvertObjectToHttpResponse(w, resp)
	w.WriteHeader(http.StatusCreated)
	return
}

func (c *LeaguesController) handleGetLeague(w http.ResponseWriter, r *http.Request, ctx context.Context) {
	id, err := rest.GetPathVariableAsInt(w, r, "/v1/leagues/")
	if err != nil {
		return
	}

	req := &pb.LeagueId{Id: id}
	resp, err := c.LeaguesServiceClient.GetLeague(ctx, req)
	if err != nil {
		log.Printf("error sending get league request: %v", err)
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	rest.ConvertObjectToHttpResponse(w, resp)
	w.WriteHeader(http.StatusOK)
	return
}

func (c *LeaguesController) handleGetLeagueStandings(w http.ResponseWriter, r *http.Request, ctx context.Context) {
	id, err := rest.GetPathVariableAsInt(w, r, "/v1/leagues/standings/")
	if err != nil {
		return
	}

	req := &pb.LeagueId{Id: id}
	resp, err := c.LeaguesServiceClient.GetLeagueStandings(ctx, req)
	if err != nil {
		log.Printf("error sending get league standings request: %v", err)
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	rest.ConvertObjectToHttpResponse(w, resp)
	w.WriteHeader(http.StatusOK)
	return
}

func (c *LeaguesController) handleUpdateLeague(w http.ResponseWriter, r *http.Request, ctx context.Context) {
	id, err := rest.GetPathVariableAsInt(w, r, "/v1/leagues/")
	if err != nil {
		return
	}

	req := &pb.UpdateLeagueRequest{}
	rest.ConvertHttpRequestBodyToObject(w, r, req)
	req.Id = id

	_, err = c.LeaguesServiceClient.UpdateLeague(ctx, req)
	if err != nil {
		log.Printf("error sending update league request: %v", err)
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	w.WriteHeader(http.StatusNoContent)
	return
}

func (c *LeaguesController) handleDeleteLeague(w http.ResponseWriter, r *http.Request, ctx context.Context) {
	id, err := rest.GetPathVariableAsInt(w, r, "/v1/leagues/")
	if err != nil {
		return
	}

	req := &pb.LeagueId{Id: id}
	_, err = c.LeaguesServiceClient.DeleteLeague(ctx, req)
	if err != nil {
		log.Printf("error sending delete league request: %v", err)
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	w.WriteHeader(http.StatusNoContent)
	return
}
