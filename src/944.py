# for given N and k, #(subsets of {1, ..., N} with k as elivisor)
# = #(subsets with k and at least one (proper) mult of k)
# = #(subsets with k) - #(subsets with k and no (proper) mult of k)
# = 2^(N-1) - 2^(N - N//k)
# S(n) = Sum_{k=1..n} k (2^(n-1) - 2^(n - n//k))
# Use Dirichlet hyperbola method / squareroot trick iterating over n//k. 
# Time of O(sqrt(n) log n) as there's O(sqrt n) iters and pow takes O(log n).

M = 1234567891

def T(n): return n*(n+1)//2

# Optional nice optimization: 
# 2^x mod p = 2^(x mod p-1) mod p. pypy 17 -> 12 sec
# Let s = int(sqrt M). Sqrt decomposition: precompute two lists
# 2^0, 2^1, 2^2, ..., 2^(s-1)
# 2^s, 2^(2s), ..., 2^(M//s)
# With O(sqrt M) space, improves pow2 from O(log n) to O(1). -> 1.2 sec
from itertools import accumulate
s = int(M**0.5)
mul = lambda x, y: (x * y) % M
l1 = list(accumulate([2]*(s-1), mul, initial=1))
l2 = list(accumulate([pow(2,s,M)]*(M//s), mul, initial=1))

def pow2(x):
    x = x % (M-1)
    return (l2[x//s] * l1[x%s]) % (M) 


def S(n):
    c = int(n**0.5)
    return (T(n) * pow2(n-1)
        - sum(i * pow2(n - n//i) for i in range(1, n//c + 1)) 
        - sum((T(n//j) - T(n//(j+1))) * pow2(n-j) 
              for j in range(1, c)))

print(S(10**14) % M)
