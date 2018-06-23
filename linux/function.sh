# 1. $@ and $* indicates all the parameters
# 2. $# indicates the nubmer of the parameters
# 3. `cmd` and $(cmd) to get the result of cmd execution
# 4. $ and ${} get the value of the variable. of course # to retrieve the length of the variable or array

function func()
{
	echo $@
	echo $*
}

func 1 2 3 4