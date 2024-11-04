package main

import (
	"bytes"
	"io"
	"net/http"
)

var ROUTES = map[string]bool {
    "/v1/players": true,
    "/v1/players/{id}": true,
    "/v1/teams": true,
    "/v1/teams/{id}": true,
    "/v1/games": true,
    "/v1/games/{id}": true,
    "/v1/stats": true,
    "/v1/stats/{id}": true,
    "/v1/leagues": true,
    "/v1/leagues/{id}": true,
}

var ROUTES_TO_METHODS = map[string]map[string]bool{
    "/v1/players": {
        "POST": true,
    },
    "/v1/players/{id}": {
        "GET":    true,
        "PATCH":  true,
        "DELETE": true,
    },

    "/v1/teams": {
        "POST": true,
    },
    "/v1/teams/{id}": {
        "GET":    true,
        "PATCH":  true,
        "DELETE": true,
    },

    "/v1/games": {
        "POST": true,
    },
    "/v1/games/{id}": {
        "GET":    true,
        "PATCH":  true,
        "DELETE": true,
    },

    "/v1/stats": {
        "POST": true,
    },
    "/v1/stats/{id}": {
        "GET":    true,
        "PATCH":  true,
        "DELETE": true,
    },

    "/v1/leagues": {
        "POST": true,
    },
    "/v1/leagues/{id}": {
        "GET":    true,
        "PATCH":  true,
        "DELETE": true,
    },
}

var ROUTES_TO_URLS = map[string]string{
    "/v1/players": "http://localhost:8081",
    "/v1/players/{id}": "http://localhost:8081",
    "/v1/teams": "http://localhost:8082",
    "/v1/teams/{id}": "http://localhost:8082",
    "/v1/games": "http://localhost:8083",
    "/v1/games/{id}": "http://localhost:8083",
    "/v1/stats": "http://localhost:8084",
    "/v1/stats/{id}": "http://localhost:8084",
    "/v1/leagues": "http://localhost:8085",
    "/v1/leagues/{id}": "http://localhost:8085",
}

func Controller() *http.ServeMux {
    mux := http.NewServeMux()
    mux.HandleFunc("/", handler)

    return mux
}

func handler(w http.ResponseWriter, r *http.Request) {
    route := r.URL.Path
    method := r.Method

    if _, ok := ROUTES[route]; !ok {
        w.WriteHeader(http.StatusNotFound)
        w.Write([]byte("404 - Not Found"))
        return
    }

    if _, ok := ROUTES_TO_METHODS[route][method]; !ok {
        w.WriteHeader(http.StatusMethodNotAllowed)
        w.Write([]byte("405 - Method Not Allowed"))
        return
    }

    url, ok := ROUTES_TO_URLS[route]

    if !ok {
        w.WriteHeader(http.StatusInternalServerError)
        w.Write([]byte("500 - Internal Server Error"))
        return
    }

    client := &http.Client{}
    body, err := io.ReadAll(r.Body)

    defer r.Body.Close()

    if err != nil {
        w.WriteHeader(http.StatusInternalServerError)
        w.Write([]byte("500 - Internal Server Error"))
        return
    }

    req, err := http.NewRequest(method, url+route, bytes.NewBuffer(body))

    if err != nil {
        w.WriteHeader(http.StatusInternalServerError)
        w.Write([]byte("500 - Internal Server Error"))
        return
    }
    
    resp, err := client.Do(req)

    if err != nil {
        w.WriteHeader(http.StatusInternalServerError)
        w.Write([]byte("500 - Internal Server Error"))
        return
    }

    for header, value := range resp.Header {
        w.Header().Set(header, value[0])
    }
    w.WriteHeader(resp.StatusCode)

    body, err = io.ReadAll(resp.Body)

    if err != nil {
        w.WriteHeader(http.StatusInternalServerError)
        w.Write([]byte("500 - Internal Server Error"))
        return
    }

    w.Write(body)
}

