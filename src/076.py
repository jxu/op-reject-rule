# Integer partition
# Euler's pentagonal number theorem

memo = [0]*101
memo[0] = 1

def p(n):
    if n < 0: return 0
    if memo[n] != 0:
        return memo[n]

    s = 0
    k = 1
    while k*(3*k-1)//2 < 100:
        s += (-1)**(k-1) * p(n - k*(3*k - 1)//2)
        s += (-1)**(k-1) * p(n - -k*(3*-k - 1)//2)
        k += 1

    memo[n] = s
    return s

print(p(100) - 1)
