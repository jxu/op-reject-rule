from number import sieve
from functools import cache

primes = sieve(2026)

@cache
def count_lists(n, min_i):
    """Count prime lists that sum to n, using only primes[min_i] and greater"""
    if n == 0: return 1
    s = 0
    for i in range(min_i, len(primes)):
        if (n - primes[i] < 0): break  # speed-up
        s += count_lists(n - primes[i], i+1)

    return s


def search(n, i, target):
    """Search tree for target order-statistic, child list sums to n, 
    considering prime[i] here 
    """
    if n == 0: return 1

    count = count_lists(n - primes[i], i+1)  # size of child subtree

    # previously this was a for loop, but it's turned into a recursion
    # adjusting target count
    if target < count:
        # take prime and recurse into subtree
        return (primes[i] * search(n - primes[i], i+1, target)) % 10**9
    else: 
        # pass prime, keeping n and adjusting target count
        return search(n, i+1, target - count)


def mpl(n):
    # median index for list of len k: (k-1)/2
    return search(n, 0, (count_lists(n, 0)-1) // 2)

print(mpl(2026))
