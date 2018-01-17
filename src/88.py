# Current benchmarks: 13s with python 3, 3s with pypy
from number import factors

MAX_PSNUM = 13000
sorted_divisors = [factors(n) for n in range(MAX_PSNUM)]

# Uses function that keeps track of sum, product, and sum/product list size
#actually faster without memoization (!)
def f(s, p, k, min_d):
    if s < 0: return False
    if k == 0: return s == 0 and p == 0
    if k == 1: return s == p
    if p == 1: return s == k  # Fill remaining list with 1s

    #print(s,p,k)
    for d in sorted_divisors[p]:
        # Enforce using divisors in ascending order (5x speedup)
        if d < min_d: continue
        if f(s-d, p//d, k-1, d): return True
    return False

min_set = set()

for k in range(2, 12001):
    for s in range(k+1, MAX_PSNUM):  # sum > k
        # Doesn't save time to skip primes
        if f(s, s, k, 2):  # Min divisor of 2 to avoid filling list with 1s
            print(k, s)
            min_set.add(s)
            break

print(sum(min_set))
