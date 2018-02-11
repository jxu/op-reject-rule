# Current benchmarks (no printing): 11s with python 3, 2s with pypy
# Results max k: (terms, sum):
# 10: (6, 61)
# 100: (37, 2061)
# 1000: (205, 93063)
# 10000: (1215, 5441890)
# 100000: (7672, 344017453)
# 1000000: (51112, 23089470906)
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
        # Enforce using divisors in ascending order (6x speedup)
        if d < min_d: continue
        if f(s-d, p//d, k-1, d): return True
    return False

min_set = set()

for k in range(2, 12001):
    for s in range(k+1, MAX_PSNUM):  # sum > k
        # Doesn't save time to skip prime s
        if f(s, s, k, 2):  # Min divisor of 2 to avoid filling list with 1s
            print(k, s)
            min_set.add(s)
            break

print(len(min_set), sum(min_set))
