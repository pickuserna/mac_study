package main

import "fmt"

func go2(c chan int) {
	c <- 222
}

func channel_test() {
	var nob_channel chan int
	if nob_channel == nil {

		nob_channel = make(chan int)
		fmt.Println("not valid channel : nob_channel: ")
	}
	go go2(nob_channel)
	fmt.Println(<-nob_channel)
	fmt.Println("hello channel")
}

func test_array() {
	var c, b [5]int

	fmt.Println(c == [5]int{0, 0, 0, 0, 0})
	fmt.Println(c == b)

}

// func main(){
// 	//channel_test()
// 	// hello_main()
// 	fmt.Println("hello dlv")
// 	test_array()
// }
