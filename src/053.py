from math import comb
print(sum(comb(n, r) > 10**6 for n in range(1, 101) for r in range(n+1)))