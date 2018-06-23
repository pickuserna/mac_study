package main

import (
	"ch08/tools"
	"log"
	"net"
	"os"
)

func main() {
	conn, err := net.Dial("tcp", "localhost:8000")
	if err != nil {
		log.Fatal(err)
	}
	defer conn.Close()
	go tools.MustCopy(os.Stdout, conn)
	tools.MustCopy(conn, os.Stdin)
}
