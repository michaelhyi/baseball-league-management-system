package main

import (
	"bytes"
	"io"
	"log"
	"net/http"
)

func GetRequest(r *http.Request, downstreamUrl string) (*http.Request, error) {
	var req *http.Request
	var err error

	if r.Method == http.MethodGet || r.Method == http.MethodDelete {
		req, err = http.NewRequest(r.Method, downstreamUrl+r.URL.String(), nil)
	} else {
		body, err := io.ReadAll(r.Body)
		if err != nil {
			return nil, err
		}
		req, err = http.NewRequest(r.Method, downstreamUrl+r.URL.String(), bytes.NewBuffer(body))
	}
	if err != nil {
		return nil, err
	}

	for header, value := range r.Header {
		log.Printf("set header: %v %v \n", header, value)
		req.Header.Set(header, value[0])
	}
	return req, err
}

func ForwardHttpResponse(w http.ResponseWriter, resp *http.Response) {
	w.WriteHeader(resp.StatusCode)
	for header, value := range resp.Header {
		w.Header().Set(header, value[0])
	}

	body, err := io.ReadAll(resp.Body)
	defer resp.Body.Close()
	if err != nil {
		w.WriteHeader(http.StatusInternalServerError)
		w.Write([]byte("internal server error"))
		return
	}

	w.Write(body)
}
