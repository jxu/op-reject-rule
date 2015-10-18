# R(k) = (10^k-1)/9
from number import sieve
primes = sieve(10**6)
result = 0
count = 0
for p in primes:
    if pow(10, 10**9, 9*p) == 1:
        print(p)
        result += p
        count += 1
    if count == 40: break
print(result)

# One-liner
print(sum([p for p in primes if pow(10, 10**9, 9*p)==1][:40]))