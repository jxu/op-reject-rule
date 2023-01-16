# Window invariant means after k cols, the colsum of the new cols repeat
# Window can be converted to colsum string like 0112 0112 ...
# For each k-length segment, there are equal num of 2s as 0s
# Let i be num of 0 cols.
# Placing 0, 1, 2 has (k choose i) * (k-i choose i) combinations.
# There is one way to make matrix col with colsum 0 or 2, but 2 ways for 1
# For n/k segments, there are (2^(k-2i))^(n/k) ways to have 1-cols
# Final formula: sum_{i=0..k/2} (k C i) (k-i C i) 2^((k-2i)*n/k)

from number import mul_inv
M = 1000000007

# precompute factorial mod M
fact = [1] * (10**8 + 1)
for i in range(1, 10**8 + 1):
    fact[i] = (fact[i-1] * i) % M

def comb_mod(n, k):
    return (fact[n] * mul_inv(fact[k] * fact[n-k] % M, M)) % M

def A(k, n):
    s = 0
    for i in range(0, k//2+1):
        t = comb_mod(k, i) * comb_mod(k-i, i) * pow(2, (k-2*i)*(n//k), M)
        s = (s + t) % M

    return s

print(A(10**8, 10**16))