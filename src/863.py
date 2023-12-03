# Let e(x) be expected dice rolls remaining starting with x (uniform) values
# for a 5-sided dice rolls and b 6-sided dice rolls:
# e(x) = min_{a,b} ((y%n)/y e(y%n) + (a+b)) where y = x 5^a 6^b
# As it turns out, it's sufficient to roll 1 dice at a time because rolling
# multiple dice at once gives the same EV as rolling procedure 1 at a time (?)
# Iterate over e(x) values until reaching a fixed point

def R(n):
    e = [0] * n
    for t in range(50):
        for i in range(1, n):
            e[i] = 1 + min(5*i%n/(5*i) * e[5*i%n],
                           6*i%n/(6*i) * e[6*i%n])
    return e[1]

def S(n):
    return sum(R(k) for k in range(2, n+1))

print(round(S(1000), 6))