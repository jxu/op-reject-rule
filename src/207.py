from scipy.optimize import bisect
from math import log2

def f(m):
    n = int(((4*m + 1)**0.5 + 1)/2)
    return int(log2(n)) / (n-1) - 1/12345

print("Approximate root", bisect(f, 10**10, 10**11))
for m in range(int(4.404e10), int(4.405e10)):
    if f(m) < 0:
        print(m)
        break

