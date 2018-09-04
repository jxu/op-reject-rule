# IMO 1995 Problem 6 (thanks to my friend John for pointing this out)
# Generating function approach with roots-of-unity filter described in
# http://zacharyabel.com/papers/Multi-GF_A06_MathRefl.pdf
# Timing (ThinkPad) Python 3.6: 10m 25s, PyPy 5.10.0: 1m 37s

from number import sieve, mul_inv
M = 1000000009
L = 10**8
sp = set(sieve(L))

A2 = -2  # adjust for A2(2) = 2 instead of 4
A3 = -3  # A3(2) = 6 instead of 9
bin2 = 1 # (2n choose n)
bin3 = 1 # (3n choose n)
for n in range(L - 1):
    if n in sp:
        p = n
        p_inv = mul_inv(p, M)
        A2 = (A2 + p_inv * (bin2 + 2*(p-1))) % M
        A3 = (A3 + p_inv * (bin3 + 3*(p-1))) % M

    bin2 = (bin2 * (4*n + 2) * mul_inv(n + 1, M)) % M
    bin3 = (bin3 * 3*(3*n+1)*(3*n+2) * mul_inv((2*n+1)*(2*n+2), M)) % M

print(A2, A3)
print((A2 + A3) % M)
