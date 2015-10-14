# Continuation of #129
from fractions import gcd
from number import sieve
def A(n):
    x = 1
    k = 1
    while x:
        x = (x*10 + 1) % n
        k += 1

    return k

result = 0
count = 0
sp = set(sieve(20000))
for n in range(3, 20000, 2):
    if count == 25: break
    if n not in sp and gcd(n, 10) == 1 and (n-1) % A(n) == 0:
        print(n)
        result += n
        count += 1

print(result)