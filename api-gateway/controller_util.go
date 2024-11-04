package main

import (
	"fmt"
	"regexp"
	"slices"
)


var REGEXPS_TO_ROUTES = map[*regexp.Regexp]string{
    regexp.MustCompile(`^/v1/players$`): "/v1/players",
    regexp.MustCompile(`^/v1/players/([a-zA-Z0-9-]+)$`): "/v1/players/{id}",
    regexp.MustCompile(`^/v1/teams$`): "/v1/teams",
    regexp.MustCompile(`^/v1/teams/([a-zA-Z0-9-]+)$`): "/v1/teams/{id}",
    regexp.MustCompile(`^/v1/games$`): "/v1/games",
    regexp.MustCompile(`^/v1/games/([a-zA-Z0-9-]+)$`): "/v1/games/{id}",
    regexp.MustCompile(`^/v1/stats$`): "/v1/stats",
    regexp.MustCompile(`^/v1/stats/([a-zA-Z0-9-]+)$`): "/v1/stats/{id}",
    regexp.MustCompile(`^/v1/leagues$`): "/v1/leagues",
    regexp.MustCompile(`^/v1/leagues/([a-zA-Z0-9-]+)$`): "/v1/leagues/{id}",
}

var ROUTES_TO_ALLOWED_METHODS = map[string][]string{
    "/v1/players": {"POST"},
    "/v1/players/{id}": {"GET", "PATCH", "DELETE"},
    "/v1/teams": {"POST"},
    "/v1/teams/{id}": {"GET", "PATCH", "DELETE"},
    "/v1/games": {"POST"},
    "/v1/games/{id}": {"GET", "PATCH", "DELETE"},
    "/v1/stats": {"POST"},
    "/v1/stats/{id}": {"GET", "PATCH", "DELETE"},
    "/v1/leagues": {"POST"},
    "/v1/leagues/{id}": {"GET", "PATCH", "DELETE"},
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

func ValidatePath(path string) (string, error) {
    var noop string

    for regexp, route := range REGEXPS_TO_ROUTES {
        if regexp.MatchString(path) {
            return route, nil
        }
    }

    return noop, fmt.Errorf("Route %v not found", path)
}

func ValidateMethod(route string, method string) error {
    if slices.Contains(ROUTES_TO_ALLOWED_METHODS[route], method) {
        return nil
    }

    return fmt.Errorf("Method %v not allowed for route %v", method, route)
}

func GetDownstreamUrl(route string, path string) string {
    return ROUTES_TO_URLS[route] + path
}

