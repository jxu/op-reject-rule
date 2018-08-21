from __future__ import division
from number import sieve, product, combination
from itertools import combinations

inv_p2 = [1/(p**2) for p in sieve(100)]
s = 0
for i in range(7, 20):
    s += (-1)**(i+1) * combination(i, 7) * sum(map(product, combinations(inv_p2, i)))
    print(s)