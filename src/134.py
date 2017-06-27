# m * 10^(digits of p1) + p1 = 0 (mod p2)

from number import sieve, mul_inv

primes = sieve(1000004)  # Last pair (999983, 1000003)
s = 0
for i in range(2, len(primes)-1):
    p1, p2 = primes[i], primes[i+1]
    base = 10**len(str(p1))
    m = (mul_inv(base, p2) * -p1) % p2
    s += m*base + p1

print(s)