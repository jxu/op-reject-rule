# Casework Optimizations
# Pick's theorem: A = i + b/2 - 1

# 4 triangles: 73.9 s
# Upper-lower triangles: 20.0 s
# a,c and b,d symmetry (third possible): 6.5 s
# Only integer math: 5.7 s
# a, b symmetry (credit: umu): 3.7 s

from fractions import gcd
import time

def lattice(m):
    square_num = set(i**2 for i in range(int(20000**0.5)))

    # Precalculate triangle values
    tri_table = [[[0]*101 for i in range(101)] for j in range(101)]
    for a in range(101):
        for h in range(101):
            for c in range(101):
                A2 = (a+c)*h
                B = gcd(a, h) + gcd(h, c) + a + c
                tri_table[a][h][c] = (A2 - B)//2 + 1

    s = 0
    for a in range(1, m+1):
        for c in range(1, a+1):
            # Symmetry case counter
            rc = 2 if c!=a else 1 # a,c symmetry

            for b in range(1, a+1):
                rcb = 2*rc if b!=a else rc # a, b symmetry
                # Upper triangle + horizontal edge correction
                abc_ = tri_table[a][b][c] + a + c - 1

                for d in range(1, b+1):
                    if abc_ + tri_table[a][d][c] in square_num:
                        s += 2*rcb if d!=b else rcb # b,d symmetry

    return s

start = time.clock()
print(lattice(100))
print(time.clock() - start)
