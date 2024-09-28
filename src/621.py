"""Reduce to iterating over r2: sum of two squares count

Sum of 3 triangles is related to sum of 3 squares by [1]
     a(a+1)/2 +  b(b+1)/2 +  c(c+1)/2 = n
<=> 4a^2 + 4a + 4b^2 + 4b + 4c^2 + 4c = 8n
<=>  (2a+1)^2 +  (2b+1)^2 +  (2c+1)^2 = 8n + 3
all solutions of sum 3 squares equiv 3 mod 8 have a, b, c all odd
scale by 1/8 for 8 choices of sign in r3(n)

G(17526e9) = r3(8*17526e9 + 3) / 8 
8*17526e9 + 3 factors nicely as 3^8 * 13 * 3257 * 466073
[2] has a nice result which was probably intended 
r3(9^l n) = ((3^(l+1)-1)/2 - Jacobi(-n,3) (3^l - 1)/2) r3(n) = 161 * r3(n) 
Doing the calculation for l=4, n=21369913123


[1] has formulas for r3 in terms of the Jacobi symbol, but it's simpler
to just sum over 2 * r2(N - c^2) for possible c. (2 for +/-c)

r2 is classical, Jacobi's two-square theorem (also in [1]):
Let n = 2^f n1 n2, where 
n1 = Prod_{p = 1 mod 4} p^r, n2 = Prod_{q = 3 mod 4} q^s
If any s are odd, then r2(n) = 0. 
If all s are even, then r2 = 4 d(n1) = 4 Prod_i (r_i + 1)

original without reducing by 9^4: 80 mins
Current sol: ~3 s

1: Ono, Robins, Wahl -
On the representation of integers as sums of triangular numbers (1995)
2: Hirschhorn, Sellers - 
On representations of a number as a sum of three squares (1998)
"""

from number import factor


def r2(n):
    """Sum of two squares function via Jacobi's two-square theorem"""
    r = 4
    for p, e in factor(n).items():
        if p == 2: continue
        if p % 4 == 1: 
            r *= e + 1
        if p % 4 == 3 and e % 2 == 1:
            return 0 

    return r 


def G(n):
    return r3(8*n + 3) // 8


def r3(n):
    s = 0
    for c in range(int(n**0.5)+1):
        s += 2 * r2(n - c*c) 
    return s

    
#print(G(10**6))
print(161 * r3(13*3527*466073) // 8)
