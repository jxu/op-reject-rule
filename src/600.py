from itertools import product

seen = set()
s = 0  # any hexagon
s1 = 0  # 60 deg rot
s2 = 0  # 120 deg rot
r1 = 0  # reflection thru side
for a,b,c,d,e,f in product(range(1,8), repeat=6):
    if a + b + c + d + e + f <= 12 and a + b == d + e and b + c == e + f:
        print(a,b,c,d,e,f)
        s += 1
        if a == c == e: s1 += 1
        if a == b and c == d: s2 += 1
        if c == e and b == f: r1 += 1

print(s, s1, s2, r1)
