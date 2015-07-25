# TESTING
from fractions import gcd

def lcm(a, b): return a * b // gcd(a, b)
n = 100

lcm_sum = 0

for a in range(1, n+1):
    for b in range(1, a+1):
        lcm_sum += lcm(a, b)
        print(a, b, lcm(a, b))

total_pairs = n*(n+1)//2
print(lcm_sum / total_pairs)