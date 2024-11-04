package main

import (
	"bytes"
	"io"
	"net/http"
)

func Controller() *http.ServeMux {
    mux := http.NewServeMux()
    mux.HandleFunc("/", handler)
    return mux
}

func handler(w http.ResponseWriter, r *http.Request) {
    path := r.URL.Path
    method := r.Method

    route, err := ValidatePath(path)

    if err != nil {
        w.WriteHeader(http.StatusNotFound)
        w.Write([]byte(err.Error()))
        return
    }

    err = ValidateMethod(route, method)

    if err != nil {
        w.WriteHeader(http.StatusMethodNotAllowed)
        w.Write([]byte(err.Error()))
        return
    }

    url := GetDownstreamUrl(route, path)
    forwardRequest(w, r, url, method)
}

func forwardRequest(w http.ResponseWriter, r *http.Request, url string, method string) {
    client := &http.Client{}

    var body []byte
    var err error

    if method == http.MethodPost || method == http.MethodPatch {
        body, err = io.ReadAll(r.Body)
        defer r.Body.Close()
    }

    if err != nil {
        w.WriteHeader(http.StatusInternalServerError)
        w.Write([]byte("500 - Internal Server Error"))
        return
    }

    var req *http.Request

    if method == http.MethodPost || method == http.MethodPatch {
        req, err = http.NewRequest(method, url, bytes.NewBuffer(body))
    } else {
        req, err = http.NewRequest(method, url, nil)
    }

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
    defer resp.Body.Close()

    if err != nil {
        w.WriteHeader(http.StatusInternalServerError)
        w.Write([]byte("500 - Internal Server Error"))
        return
    }

    w.Write(body)
}

