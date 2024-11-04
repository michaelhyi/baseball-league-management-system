package main

import (
	"net/http"
	"net/http/httptest"
	"testing"
)

func TestRouteNotFound(t *testing.T) {
    req, err := http.NewRequest("GET", "/notfound", nil)

    if err != nil {
        t.Errorf("Error creating request: %v\n", err)
        return
    }

    res := httptest.NewRecorder()

    Controller().ServeHTTP(res, req)

    expectedStatusCode := http.StatusNotFound
    expectedBody := "Route /notfound not found"

    if expectedStatusCode != res.Code {
        t.Errorf("Expected status code %d, got %d\n", expectedStatusCode, res.Code)
    }

    if expectedBody != res.Body.String() {
        t.Errorf("Expected body %s, got %s\n", expectedBody, res.Body.String())
    }
}

func TestMethodNotAllowed(t *testing.T) {
    req, err := http.NewRequest("PUT", "/v1/players", nil)

    if err != nil {
        t.Errorf("Error creating request: %v\n", err)
        return
    }

    res := httptest.NewRecorder()

    Controller().ServeHTTP(res, req)

    expectedStatusCode := http.StatusMethodNotAllowed
    expectedBody := "Method PUT not allowed for route /v1/players"

    if expectedStatusCode != res.Code {
        t.Errorf("Expected status code %d, got %d\n", expectedStatusCode, res.Code)
    }

    if expectedBody != res.Body.String() {
        t.Errorf("Expected body %s, got %s\n", expectedBody, res.Body.String())
    }
}

// TODO: Test downstream proxy

