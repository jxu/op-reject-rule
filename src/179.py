# JohnMorris: Clever sieve solution for the divisor function without factoring
# Time complexity: sum_{i=2..N} N/i = O(N log N)
N = 10**7
sigma = [1] * (N+1)

for n in range(2, N+1):
    for i in range(n, N+1, n):
        sigma[i] += 1

print(sum(sigma[n] == sigma[n+1] for n in range(2, N)))