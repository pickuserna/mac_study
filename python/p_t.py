
def NumberOf1(n):
    # write code here
    count = 0
    if n < 0:
        count += 1
        n = (1 << 31) + n
    while n > 0:
        count += n % 2
        n = n >> 1
    return count

print NumberOf1(-3)