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

def S(n):
    c = int(n**0.5)
    return (T(n) * pow(2, n-1, M)
        - sum(i * pow(2, (n - n//i) % (M-1), M) for i in range(1, n//c + 1)) 
        - sum((T(n//j) - T(n//(j+1))) * pow(2, (n-j)%(M-1), M) 
              for j in range(1, c)))

print(S(10**14) % M)
