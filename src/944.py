# for given N and k, #(subsets of {1, ..., N} with k as elivisor)
# = #(subsets with k and at least one (proper) mult of k)
# = #(subsets with k) - #(subsets with k and no (proper) mult of k)
# = 2^(N-1) - 2^(N - N//k)
# S(n) = Sum_{k=1..n} k (2^(n-1) - 2^(n - n//k))
# Use Dirichlet hyperbola method / squareroot trick iterating over n//k. 
# Time of O(sqrt(n) log n) as there's sqrt(n) iters and exp takes log n.
# To optimize log n factor out, have faster way to compute 2^x mod p

# Nice optimization: 2^x mod p = 2^(x mod p-1) mod p. pypy 17 -> 12 sec

M = 1234567891

def T(n): return n*(n+1)//2

s = int(M**0.5)
l1 = []
x = 1
for i in range(s):
    l1.append(x)
    x = (2 * x) % (M)

l2 = []
x = 1
s2 = pow(2, s, M)
for i in range(M // s + 1):
    l2.append(x)
    x = (s2 * x) % (M)


def pow2(x):
    x = x % (M-1)
    return (l2[x//s] * l1[x%s]) % (M) 


def S(n):
    c = int(n**0.5)
    return (T(n) * pow(2, n-1, M)
        - sum(i * pow2(n - n//i) for i in range(1, n//c + 1)) 
        - sum((T(n//j) - T(n//(j+1))) * pow2(n-j) 
              for j in range(1, c)))

print(S(10**14) % M)
