package tools

import (
	"io"
	"log"
)

//MustCopy copy from src to dst
func MustCopy(dst io.Writer, src io.Reader) {
	if _, err := io.Copy(dst, src); err != nil {
		log.Fatal(err)
	}
}
