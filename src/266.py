# WIP Adaptation of the knapsack problem (DP)

from __future__ import division
from number import sieve, product, memoize

primes = sieve(100)
memo = {}


def max_div(target, max_i):
    memo_args = (target, max_i)
    if memo_args in memo:
        print(memo_args)
        return memo[memo_args]
    #if max_i == 0: print(target, psr, max_i)

    if max_i == -1:
        memo[memo_args] = 1
        return 1

    if target/primes[max_i] > 1:
        r = max(max_div(target, max_i-1),
                   max_div(target/primes[max_i], max_i-1) * primes[max_i])
    else:
        r = max_div(target, max_i-1)

    memo[memo_args] = r
    return r




x = max_div(product(primes)**0.5, len(primes)-1)

print(x, product(primes)**0.5 / x)

