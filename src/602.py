# After r rounds, expected number of heads for each friend is geometric
# distribution: r(1-p)
# Since players are independent, the product of n friends is (r(1-p))^n
# Considering r = 1, 2, 3, ..., e(n, p) =
# p(1-p)((1(1-p))^n + p^2(1-p)((2(1-p))^n + ...
# = (1-p)^(n+1) sum_{i=1}^Inf{p^i * i^n}
# = (1-p)^(n+1) * Li_{-n}(p), the polylogarithm!
# The coefficient of z^(n-k) is A(n, k), an Eulerian number!
# A(n, m) = sum_{k=0}^{m+1}{(-1)^k (n+1 choose k) (m+1-k)^n}
# For efficiency, get (-1)^(k+1) (n+1 choose k+1) as -(n+1-k)/(k+1) *
# (-1)^k (n_1 choose k) (prev. term).

from number import mod_inv

mod = 10**9 + 7
def A(n, m):
    s = 0
    l = 1
    for k in range(0, m+2):
        s += l * pow(m+1-k, n, mod)
        l = (-l * (n+1-k) * mod_inv(k + 1, mod)) % mod

    return s % mod

def c(n, k): return A(n, n-k)
print(c(10**7, 4*10**6))
