# Pick's theorem: A = i + b/2 - 1
# 4 triangles: 73.9 s   Upper-lower triangles: 20.0 s
from fractions import gcd
import time

def lattice(m):
    square_num = set(i**2 for i in range(int(20000**0.5)))

    # Generate all triangle values at start
    tri_table = [[[0]*101 for i in range(101)] for j in range(101)]
    for a in range(101):
        for h in range(101):
            for c in range(101):
                A = (a+c)*h/2
                B = gcd(a, h) + gcd(h, c) + a + c
                tri_table[a][h][c] = A - B/2 + 1

    s = 0
    for a in range(1, m+1):
        for c in range(1, m+1):
            for b in range(1, m+1):
                # Upper triangle + horizontal edge correction
                abc_ = tri_table[a][b][c] + a + c - 1
                for d in range(1, m+1):
                    if abc_ + tri_table[a][d][c] in square_num: s += 1

    return s

start = time.clock()
print(lattice(100))
print(time.clock() - start)
