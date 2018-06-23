package tests

func TestSliceAppend(t *testing.T){

}

func AppendInt(slice []int , val int)[]int{
	var ret []int 
	// can add more
	if len(slice) < cap(slice){
		ret = slice
	}
	else{
		ret = make([]int, len(slice)+1, len(slice)*2)
		
	}
}