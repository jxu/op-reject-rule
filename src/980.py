# Lazy method
from sympy.algebras import Quaternion
from collections import Counter

N = 10**6

a = [0] * (50*N + 50)
b = a[:]
for i in range(len(a)):
    a[i] = (8888 * a[i-1]) % 888_888883 if i > 0 else 88_888_888
    b[i] = a[i] % 3

c = [Quaternion()] * N
for i in range(N):
    c[i] = Quaternion(1)
    for j in range(50*i, 50*i+50):
        if b[j] == 0: 
            x = Quaternion(b=1)  # 0 -> x -> i
        elif b[j] == 1: 
            x = Quaternion(d=1)  # 1 -> y -> k
        else: 
            x = Quaternion(c=1)  # 2 -> z -> j

        c[i] *= x

counter = Counter(c)
print(counter)

s = 0
for k in counter:
    s += counter[k] * counter[k.inverse()]

print(s)
