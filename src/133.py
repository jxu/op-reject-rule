# Guess n
from number import sieve
primes = sieve(100000)
result = 0
for p in primes:
    never = True
    for n in range(1, 30):
        if pow(10, 10**n, 9*p) == 1:
            never = False
            print(n, p)
            break
    if never:
        result += p

print(result)