# Pick's theorem: A = i + b/2 - 1
from fractions import gcd
import time

def lattice(m):
    square_num = set()
    for i in range(int(20000**0.5)): square_num.add(i**2)

    # Generate all triangle values at start (50% faster)
    tri_table = [[-1]*101 for i in range(101)]
    for a in range(101):
        for b in range(101):
            A = a*b/2
            B = gcd(a, b) + a + b
            tri_table[a][b] = A - B/2 + 1

    s = 0
    for a in range(1, m+1):
        for b in range(1, m+1):
            for c in range(1, m+1):
                for d in range(1, m+1):
                    # Combine triangles
                    i = tri_table[a][b] + tri_table[b][c] + tri_table[c][d] + tri_table[d][a] + (a + b + c + d - 4) + 1
                    if i in square_num: s += 1

    return s

start = time.clock()
print(lattice(100))
print(time.clock() - start)
