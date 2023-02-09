from number import fib_list, memoize


N = 10**17
fib = [x for x in fib_list(100) if x < N]
n = len(fib) - 1  # F_n < N
Zf = [0] * (n+1)


for i in range(1, n):
    Zf[i+1] = fib[i-1] + Zf[i] + Zf[i-1]

@memoize
def sumZ(N):
    if N < 2: return 0
    i = 0
    while i < len(fib) and fib[i] < N:
        i += 1
    i -= 1
    return N - fib[i] + sumZ(N - fib[i]) + sumZ(fib[i])

print(sumZ(N))