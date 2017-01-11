# Use small wheels similar to sieve of Eratosthenes

from number import sieve, product
from bisect import bisect_right

def generalised_hamming(cutoff, n):
    primes = sieve(100)
    i = bisect_right(primes, cutoff)
    small_primes = primes[:i]
    large_primes = primes[i:]

    wheel_size = product(small_primes)
    nums = [0] * wheel_size
    for i in small_primes:
        for j in range(i, wheel_size, i):
            nums[j] = 1

    not_hamming = [i for i in range(1, wheel_size) if nums[i] == 0]
    print(wheel_size, len(not_hamming)/float(wheel_size))

generalised_hamming(23, 10**9)