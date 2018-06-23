def func(secret, guess):
    bulls_num = 0
    cows_num = 0
    secret_map = {}
    guess_map = {}
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bulls_num += 1
        secret_map[secret[i]] = secret_map.get(secret[i], 0)+1
        guess_map[secret[i]] = guess_map.get(guess[i], 0)+1
    for k, v_s in secret_map.iteritems():
        v_g = guess_map.get(k, 0)
        print k, v_s, v_g
        cows_num += min(v_s, v_g)
    cows_num -= bulls_num
    cows_num = max(0, cows_num)
    return "{}A{}B".format(bulls_num, cows_num)

print func('0', '1')