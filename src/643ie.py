"""Old solution

What a journey. I did not use totient function at all, instead I directly
counted the pairs by inclusion-exclusion.

A pair of numbers is counted iff both have a common factor of 2 and
no other prime. With inclusion-exlcusion, 
we start with the set of all even pairs, then subtract out those divisible by
each odd prime p, then add back those divisible by pq for odd primes p,q, etc.
Let P' be the odd primes.

f(N) =   C(N//2, 2)
       - ∑_{p∈P'} C(N//2p, 2)
       + ∑_{p<q,{p,q}⊆P'} C(N//2pq, 2)
       - ∑_{p<q<r,{p,q,r}⊆P')} C(N//2pqr, 2) 
       + ...

Considering all odd n, if n = p, the sign is -, if n = pq, the sign is +, etc.
The Möbius function encodes this exactly:

f(N) = ∑_{odd n} μ(n) C(N//2n, 2)

My original solution used the Mertens function and summing its odd terms, but
using Möbius inversion is simpler. 

Let F(N) = ∑_{n} μ(n) C(N//2n, 2) be the simpler function which has even and 
odd terms. By Möbius inversion, C(N//2n, 2) = ∑_{n} F(N//n), rearranging

F(N) = C(N//2, 2) - ∑_{n>=2} F(N//n)

Now, to relate f and F. 
F(N) = ∑_{odd n} μ(n) C(N//2n, 2) + ∑_{even n} μ(n) C(N//2n, 2)

For odd n, μ(2n) = -μ(n), and for even n, μ(2n) = 0 (has 4 as a factor).

So the summation over even n only needs to consider 2n for odd n.

∑_{even n} μ(n) C(N//2n, 2) = ∑_{odd n} μ(2n) C(N//2(2n), 2)
= ∑_{odd n} -μ(n) C((N//2)//2n), 2) = -f(N//2)

So F(N) = f(N) - f(N//2), rearranging f(N) = F(N) + f(N//2)
This gives our recursive formula for f and F. 
F(N) is computed the usual hyperbola method. 
Let c = floor(sqrt(N))
∑_{n>=2} F(N//n) =  ∑_{2<=i<=n/c} F(N/i) + ∑_{j<=c-1} ((N//j)-(N//(j+1))) f(j)

F(n) can be precomputed up to sqrt(n) or n^2/3 to improve runtime. 
"""

from functools import cache 
from math import comb

@cache
def F(N):
    if N == 0: return 0
    
    c = int(N**0.5)
    s = comb(N//2, 2) 
    for n in range(2, N//c + 1):
        s -= F(N // n)
    for j in range(1, c):
        s -= ((N//j) - N//(j+1)) * F(j) 
        
    return s 

def f(N):
    if N == 0: return 0 
    return F(N) + f(N // 2)

print(f(10**11) % (10**9 + 7))
