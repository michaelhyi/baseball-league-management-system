package main

import "testing"

func TestValidatePath(t *testing.T) {
	tests := []struct {
		path          string
		expectedRoute string
		expectedErr   string
	}{
		{"/v1/players", "/v1/players", ""},
		{"/v1/players/123", "/v1/players/{id}", ""},
		{"/v1/players/123/", "", "Route /v1/players/123/ not found"},
		{"/v1/players/123/test", "", "Route /v1/players/123/test not found"},
		{"/v1/teams", "/v1/teams", ""},
		{"/v1/teams/123", "/v1/teams/{id}", ""},
		{"/v1/teams/123/", "", "Route /v1/teams/123/ not found"},
		{"/v1/teams/123/test", "", "Route /v1/teams/123/test not found"},
		{"/v1/games", "/v1/games", ""},
		{"/v1/games/123", "/v1/games/{id}", ""},
		{"/v1/games/123/", "", "Route /v1/games/123/ not found"},
		{"/v1/games/123/test", "", "Route /v1/games/123/test not found"},
		{"/v1/stats", "/v1/stats", ""},
		{"/v1/stats/123", "/v1/stats/{id}", ""},
		{"/v1/stats/123/", "", "Route /v1/stats/123/ not found"},
		{"/v1/stats/123/test", "", "Route /v1/stats/123/test not found"},
		{"/v1/leagues", "/v1/leagues", ""},
		{"/v1/leagues/123", "/v1/leagues/{id}", ""},
		{"/v1/leagues/123/", "", "Route /v1/leagues/123/ not found"},
		{"/v1/leagues/123/test", "", "Route /v1/leagues/123/test not found"},
	}

	for _, test := range tests {
		route, err := ValidatePath(test.path)

		if route != test.expectedRoute {
			t.Errorf("Expected route %v, got %v", test.expectedRoute, route)
		}

		if err != nil && err.Error() != test.expectedErr {
			t.Errorf("Expected error %v, got %v", test.expectedErr, err.Error())
		}
	}
}
