# IMO 1995 Problem 6 (thanks to my friend John for pointing this out)
# Generating function approach with roots-of-unity filter described in
# http://zacharyabel.com/papers/Multi-GF_A06_MathRefl.pdf

from number import sieve, mul_inv
import gc
M = 1000000009
L = 10**2
primes = sieve(L)

bin2 = [1]
bin3 = [1]
for n in range(L - 1):
    bin2.append((bin2[n] * (4*n + 2) * mul_inv(n + 1, M)) % M)
    bin3.append((bin3[n] * 3*(3*n+1)*(3*n+2)
                 * mul_inv((2*n+1)*(2*n+2), M)) % M)


    if n % 10 ** 5 == 0:
        print(n, bin2[n], bin3[n])
    if n % 10 ** 7 == 0:
        pass
        #print("gc")
        #gc.collect()  # pypy still runs out of memory??

A2 = -2  # adjust for A2(2) = 2 instead of 4
A3 = -3  # A3(2) = 6 instead of 9
for p in primes:
    p_inv = mul_inv(p, M)
    A2 = (A2 + p_inv * (bin2[p] + 2*(p-1))) % M
    A3 = (A3 + p_inv * (bin3[p] + 3*(p-1))) % M

print(A2, A3)
print((A2 + A3) % M)

