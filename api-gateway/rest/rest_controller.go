package rest

import (
	"log"
	"net/http"
)

type RestController struct {
	HttpClient    *http.Client
	DownstreamUrl string
}

func (c *RestController) Handler(w http.ResponseWriter, r *http.Request) {
	log.Printf("%s %s\n", r.Method, r.URL.Path)
	req, err := GetRequest(r, c.DownstreamUrl)
	if err != nil {
		log.Printf("error deep copying request: %s\n", err)
		w.WriteHeader(http.StatusInternalServerError)
		w.Write([]byte("internal server error"))
	}

	resp, err := c.HttpClient.Do(req)
	if err != nil {
		log.Printf("req: %v\n", req)
		log.Printf("error forwarding request: %s\n", err)
		w.WriteHeader(http.StatusInternalServerError)
		w.Write([]byte("internal server error"))
		return
	}

	ForwardHttpResponse(w, resp)
}
