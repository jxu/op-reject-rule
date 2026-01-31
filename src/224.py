# Better idea from 223: tree of Pythagorean triples works
# Just need to remove wrong side length order triangles
import sys
sys.setrecursionlimit(3000)


seen = set()

def f(a, b, c, M = 75_000_000):
    if a + b + c > M: return
    # sometimes b < a but we still need to recurse I think

    new_triple = (a, b, c) if a <= b else (b, a, c)
    seen.add(new_triple)

    f( a - 2*b + 2*c,  2*a - b + 2*c,  2*a - 2*b + 3*c)
    f( a + 2*b + 2*c,  2*a + b + 2*c,  2*a + 2*b + 3*c)
    f(-a + 2*b + 2*c, -2*a + b + 2*c, -2*a + 2*b + 3*c)

f(2, 2, 3)

print(len(seen))
