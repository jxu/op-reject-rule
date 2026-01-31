import sys

sys.setrecursionlimit(3000)

M = 75_000_000

seen = set()

def f(a, b, c, l=0):
    if a + b + c > M: return 

    new_triple = (a, b, c) if a <= b else (b, a, c)
    seen.add(new_triple)

    f(a - 2*b + 2*c, 2*a - b + 2*c, 2*a - 2*b + 3*c, l+1)
    f(a + 2*b + 2*c, 2*a + b + 2*c, 2*a + 2*b + 3*c, l+1)
    f(-a + 2*b + 2*c, -2*a + b + 2*c, -2*a + 2*b + 3*c, l+1)

f(2, 2, 3)

print(len(seen))
