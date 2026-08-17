from math import prod
from number import sieve
from functools import cache

primes = sieve(2026)

@cache
def count_lists(n, i):
    """Count prime lists that sum to n, considering p_i and greater"""
    if n < 0 or i >= len(primes): return 0
    if n == 0: return 1
    # either incorporate p_i into the list or don't
    return count_lists(n - primes[i], i+1) + count_lists(n, i+1)


def search(n, i, target):
    """Search tree for target order-statistic, child list sums to n, 
    considering prime[i] here 
    """
    if n == 0: return []

    count = count_lists(n - primes[i], i+1)  # size of child subtree

    # previously this was a for loop accumulating a sum of count, 
    # but it's turned into a recursion adjusting target count
    if target < count:
        # take prime and recurse into subtree
        return [primes[i]] + search(n - primes[i], i+1, target)
    else: 
        # pass prime, keeping n and adjusting target count
        return search(n, i+1, target - count)


def mpl(n):
    # median index for list of len k: (k-1)/2
    return search(n, 0, (count_lists(n, 0)-1) // 2)

print(prod(mpl(2026)) % 10**9)
