package tests

import (
	"fmt"
	"testing"
)

const (
	Flagup uint = 1 << iota
	FlagBroadcast
	FlagLoopback
	FlagPointToPoint
	FlagMulticast
)

func TestIota(t *testing.T) {
	var a int = 3
	a &^= 1
	fmt.Println("hello iota ====", a)
	fmt.Println(Flagup, FlagBroadcast, FlagLoopback)
	// t.Error("hello")
}
