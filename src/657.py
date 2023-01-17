# There are l^0 + ... + l^n words with at most l letters and length <= n
# (empty words are handled)
# By inclusion-exclusion the number of complete words is
# Sum_{k=0..l} (-1)^k (l choose l-k) Sum_{j=0..n} (l-k)^j
# = Sum_{k=0..l} (-1)^(l-k) (l choose k) Sum_{j=0..n} k^j
# Incomplete words is complement of this:
# Sum_{k=0..l-1} (-1)^(l-k+1) (l choose k) Sum_{j=0..n} k^j

# k^0 + ... + k^n = (k^(n+1) - 1) / (k - 1) if k != 1, n + 1 otherwise

from number import mod_inv
MOD = 1000000007

def I(l, n):
    s = 0
    binom = 1

    for k in range(l):
        z = n+1 if k == 1 else \
            ((pow(k, n+1, MOD) - 1) * mod_inv(k - 1, MOD)) % MOD
        s = (s + (-1)**(l-k+1) * binom * z) % MOD
        binom = (binom * (l-k) * mod_inv(k + 1, MOD)) % MOD

    return s

print(I(10**7, 10**12))
