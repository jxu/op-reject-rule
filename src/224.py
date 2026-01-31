# Better idea from 223: tree of Pythagorean triples works
# Just need to not do a redundant recursion if a == b
import sys
sys.setrecursionlimit(3000)

def f(a, b, c, M = 75_000_000):
    if a + b + c > M: return 0

    return (1 +
        f( a - 2*b + 2*c,  2*a - b + 2*c,  2*a - 2*b + 3*c) +
        f( a + 2*b + 2*c,  2*a + b + 2*c,  2*a + 2*b + 3*c) +
        (0 if a == b else  # short circuit 
        f(-a + 2*b + 2*c, -2*a + b + 2*c, -2*a + 2*b + 3*c)))

print(f(2, 2, 3))

