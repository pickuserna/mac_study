package main

import "fmt"

func main() {
	throwPanic()
}

func throwPanic() {
	defer func() {
		if p := recover(); p != nil {
			err := fmt.Errorf("internal error %v", p)
			fmt.Println(err)
		}
	}()
	for i := 1; i < 5; i++ {
		fmt.Println(i)
		if i >= 3 {
			// 发生panic 之后
			panic(15)
		}

		fmt.Println("after panic !!")
	}
}
