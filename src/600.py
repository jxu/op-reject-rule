# brute force tester

import sys
from itertools import product

N = int(sys.argv[1])
s = 0  # any hexagon
s1 = 0  # 60 deg rot
s2 = 0  # 120 deg rot
r1 = 0  # reflection thru side
for a,b,c,d,e,f in product(range(1,N//2), repeat=6):
    if a + b + c + d + e + f <= N and a + b == d + e and b + c == e + f:
        print(a,b,c,d,e,f)
        s += 1
        if a == c == e: s1 += 1
        if a == b and c == d: s2 += 1
        if c == e and b == f: r1 += 1

print(s, s1, s2, r1)
