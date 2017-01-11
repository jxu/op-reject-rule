# JUST BASIC RECURSION WOW

from number import sieve

CUTOFF = 100
N = 10**9
primes = sieve(CUTOFF+1)

generalised_hamming = []

def recurse(num, current_prime=primes[0]):
    if num > N: return
    generalised_hamming.append(num)
    for prime in primes:
        if prime >= current_prime:
            recurse(num * prime, prime)


recurse(1)
print(len(generalised_hamming))