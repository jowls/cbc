package main

import (
	"fmt"
	"net/http"
    	_ "github.com/lib/pq"
    	"database/sql"
)


func handler(w http.ResponseWriter, r *http.Request) {
	db, _ := sql.Open("postgres", "user=j dbname=scrape password=face sslmode=disable")
	all_stories, _ := db.Query("SELECT * FROM stories",)
	all_comments, _ := db.Query("SELECT * FROM comments",)
	i := 0
	for all_stories.Next() {
		i++
	}
	j := 0
	for all_comments.Next() {
		j++
	}

	//fmt.Fprintf(w, "Hi there, I love %s!", r.URL.Path)
	fmt.Fprintf(w, "Hi there! Right now I have crawled %d stories and %d comments.", i, j)
}

func main() {

	http.HandleFunc("/", handler)
	http.ListenAndServe(":80", nil)
}
