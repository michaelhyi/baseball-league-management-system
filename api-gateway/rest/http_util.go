package rest

import (
	"bytes"
	"encoding/json"
	"io"
	"log"
	"net/http"
	"strconv"
	"strings"
)

func GetRequest(r *http.Request, downstreamUrl string) (*http.Request, error) {
	var req *http.Request
	var err error

	if r.Method == http.MethodGet || r.Method == http.MethodDelete {
		req, err = http.NewRequest(r.Method, downstreamUrl+r.URL.String(), nil)
	} else {
		body, err := io.ReadAll(r.Body)
		defer r.Body.Close()
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
		return
	}

	w.Write(body)
}

func GetPathVariable(r *http.Request, prefix string) string {
	return strings.TrimPrefix(r.URL.Path, prefix)
}

func GetPathVariableAsInt(r *http.Request, prefix string) (int, error) {
	return strconv.Atoi(GetPathVariable(r, prefix))
}

func ConvertHttpRequestBodyToObject(w http.ResponseWriter, r *http.Request, obj any) {
	body, err := io.ReadAll(r.Body)
	defer r.Body.Close()
	if err != nil {
		log.Printf("error parsing http request body: %v", err)
		w.WriteHeader(http.StatusInternalServerError)
	}

	if err := json.Unmarshal(body, obj); err != nil {
		log.Printf("error parsing http request body json: %v", err)
		log.Printf("body: %s", body)
		w.WriteHeader(http.StatusInternalServerError)
	}
}

func ConvertObjectToHttpResponse(w http.ResponseWriter, resp any) {
	b, err := json.Marshal(resp)
	if err != nil {
		log.Printf("error converting grpc res to json: %v", err)
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	w.Write(b)
	return
}
