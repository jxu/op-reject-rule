# Brute force
from number import linear_sieve, linear_sieve_factors, prod

N = 10**7
lp = linear_sieve(N)
sigma = [0] * (N+1)

for n in range(2, N+1):
    pp = linear_sieve_factors(lp, n)
    sigma[n] = prod(e+1 for e in pp.values())

s = 0
for n in range(2, N):
    if sigma[n] == sigma[n+1]: s += 1
print(s)
