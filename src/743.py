# Window invariant means after k cols, the colsum of the new cols repeat
# Window can be converted to colsum string like 0112 0112 ...
# For each k-length segment, there are equal num of 2s as 0s
# Let i be num of 0 cols.
# Placing 0, 1, 2 has (k choose k-2i,i,i) (multinomial) combinations.
# There is one way to make matrix col with colsum 0 or 2, but 2 ways for 1
# For n/k segments, there are (2^(k-2i))^(n/k) ways to have 1-cols
# Final formula: sum_{i=0..k/2} (k C k-2i,i,i) 2^((k-2i)*n/k)

from number import mod_inv_range
M = 1000000007

inv = mod_inv_range(M, 10**8)

# precompute factorial and inverse factorial mod M
# make into functions in number?
fact = [1] * (10**8 + 1)
inv_fact = [1] * (10 ** 8 + 1)
for i in range(1, len(fact)):
    fact[i] = (fact[i-1] * i) % M
    inv_fact[i] = (inv_fact[i-1] * inv[i]) % M


def A(k, n):
    s = 0
    for i in range(0, k//2+1):
        t = fact[k] * inv_fact[k-2*i] % M * \
            (inv_fact[i]**2 % M) % M * pow(2, (k-2*i)*(n//k), M)
        s = (s + t) % M

    return s

print(A(10**8, 10**16))
