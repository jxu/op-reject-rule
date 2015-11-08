import math
from fractions import gcd
def D(N):
    x = int(N / math.e)
    # (N / (x+1))**(x+1) > (N / x)**x
    if (x+1) * math.log(N / (x+1)) > x * math.log(N / x): x += 1

    x //= gcd(N, x)  # Numerator cancel
    while x%2 == 0: x //= 2
    while x%5 == 0: x //= 5
    if x == 1: return -N
    else: return N

print(sum(D(N) for N in range(5, 10001)))