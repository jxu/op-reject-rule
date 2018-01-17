from number import sieve, product
import math
from itertools import combinations

primes = sieve(100)

for i in range(len(primes)-13):
    x = product(primes[i:i+13])
    print(primes[i:i+13], x >= 10**19)


