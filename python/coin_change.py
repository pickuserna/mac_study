res = 0
def change(amount, coins):
    coins.sort(reverse=True)
    return helper(amount, coins, 0)

def helper(amount, coins, index):
    global res 
    if amount == 0:
        res = res+1
    if index >= len(coins):
        res+=1
	if index == len(coins)-1:
		if amount % coins[index]:
			res+=1
		return 0
    print 12
    for i in range(len(coins)):
		c = coins[i]
		max_num = amount / c
		print max_num
		for n in range(max_num+1):
			amount -= c*n
			helper(amount, coins, index+1)
			amount += c*n
    return res

change(5, [5, 2, 1])
print res