package main

import (
	"log"
	"net/http"
)

func main() {
	log.Printf("Server listening on port 8080")
	err := http.ListenAndServe(":8080", Controller())

	if err != nil {
		log.Fatalf("Server failed to start: %v", err)
	}
}
