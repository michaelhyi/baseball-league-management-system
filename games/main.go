package main

import (
	"database/sql"
	"log"
	"net"

	"github.com/go-sql-driver/mysql"
	pb "github.com/michaelhyi/baseball-league-management-system/games/proto"
	"google.golang.org/grpc"
)

type server struct {
	pb.UnimplementedGamesServiceServer
	dao DbAccessor
}

func getDb() *sql.DB {
	cfg := mysql.Config{
		User:   "root",
		Passwd: "root",
		Net:    "tcp",
		Addr:   "127.0.0.1:3306",
		DBName: "baseball_league_management_system",
        Params: map[string]string{"parseTime": "true"},
	}

	db, err := sql.Open("mysql", cfg.FormatDSN())
	if err != nil {
		log.Fatal(err)
	}

	err = db.Ping()
	if err != nil {
		log.Fatalf("error connecting to db: %v\n", err)
	}

	log.Println("connected to db")

	return db
}

func main() {
	lis, err := net.Listen("tcp", ":8083")

	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}

	s := grpc.NewServer()
	db := getDb()
	dao := &Dao{db: db}

	pb.RegisterGamesServiceServer(s, &server{dao: dao})

	log.Printf("server listening at %v", lis.Addr())

	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
