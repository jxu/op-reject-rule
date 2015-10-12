from number import sieve
primes = sieve(10**6)
for N in range(len(primes)):
    p = primes[N]
    if (pow(p-1, N+1, p**2) + pow(p+1, N+1, p**2)) % p**2 > 10**10:
        print(N+1)
        break