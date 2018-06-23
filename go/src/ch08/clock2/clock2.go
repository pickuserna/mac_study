package main

import (
	"bufio"
	"fmt"
	"io"
	"log"
	"net"
	"strings"
	"time"
)

func main() {
	fmt.Println("Listen the port !")
	listener, err := net.Listen("tcp", "localhost:8000")
	if err != nil {
		log.Fatal(err)
	}
	for {
		conn, err := listener.Accept()
		fmt.Println("new connection comming !")
		if err != nil {
			log.Print(err)
			continue
		}
		handleConn(conn)
	}
}

func echo(c net.Conn, content string, delay time.Duration) {
	fmt.Fprintln(c, "\t", strings.ToUpper(content))
	time.Sleep(delay)
	fmt.Fprintln(c, "\t", strings.ToLower(content))
}

func handleConn(c net.Conn) {
	defer c.Close()
	input := bufio.NewScanner(c)
	for input.Scan() {
		echo(c, input.Text(), 1*time.Second)
	}
	for {
		_, err := io.WriteString(c, time.Now().Format("15:04:05\n"))
		fmt.Println(time.Now().Format("15:04:05\n"))
		if err != nil {
			log.Println(err)
			return
		}
		time.Sleep(1 * time.Second)
	}
}
