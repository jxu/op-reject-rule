# DP saves the day again!
# Uses function that keeps track of sum, product, and sum/product list size

from number import memoize, factors

MAX_PSNUM = 15000
sorted_divisors = [sorted(factors(n)) for n in range(MAX_PSNUM)]


@memoize
def f(s, p, k):
    if s < 0: return False
    if k == 0:
        return s == 0 and p == 0
    if s == p and k == 1: return True  # Fill remaining list with 1s
    if p == 1:
        return s == k

    #print(s,p,k)
    for d in sorted_divisors[p]:
        if d == 1: continue  # Avoid filling list with 1s
        if f(s-d, p//d, k-1): return True
    return False

min_set = set()

for k in range(2, 12001):
    for s in range(k+1, MAX_PSNUM):  # sum > k
        if f(s, s, k):
            print(k, s)
            min_set.add(s)
            break

print(sum(min_set))
