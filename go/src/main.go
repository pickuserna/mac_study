package main

import (
	"fmt"
	"reflect"
	"unsafe"
)

func helloMain() (result int) {
	defer func() {
		result++
	}()
	return
}

type User struct {
	name string
	age  int
	data interface{}
}

const (
	a int = iota
	b
	c
)

func main() {
	// u := User{name: "nihao"}
	// if val, ok := u.data.(string); ok {
	// 	fmt.Println("OK", val)
	// } else {
	// 	fmt.Println("not at all")
	// }
	var slice = []int{100, 2, 3}
	fmt.Println(unsafe.Pointer(&slice))
	var sliceB = slice
	fmt.Println(sliceB)
	fmt.Println(&slice[0], &sliceB[0])
	sliceHeader := (*reflect.SliceHeader)(unsafe.Pointer(&slice))
	fmt.Println(*sliceHeader)
	fmt.Println(unsafe.Pointer(sliceHeader.Data))
}
