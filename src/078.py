N_MAX = 100000
memo = [0]*N_MAX
memo[0] = 1

pent = [0]*2*N_MAX
for k in range(N_MAX):
    pent[k] = k*(3*k - 1)//2
    pent[-k] = -k*(3*-k - 1)//2


def p(n):
    if n < 0: return 0
    if memo[n] != 0:
        return memo[n]

    s = 0
    k = 1
    sign = 1
    while pent[k] <= n:
        s += sign * p(n - pent[k])
        s += sign * p(n - pent[-k])
        k += 1
        sign *= -1


    memo[n] = s
    return s

for n in range(N_MAX):
    if p(n) % 10**6 == 0:
        print(n)
        break

