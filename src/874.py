# We maximize the score with the best-case array [k-1] * n,
# but this array sum is r = n*(k-1) % k = 6337 above a multiple of k.
# So, minimize score loss p(k-1) - p(k-1-a_i) for a_i summing to r with DP:
# m(s) = min(p(k-1) - p(k-1-s), min_{0<i<s} m(i) + m(s-i))
# This is O(k^2) and the result is max score minus gaps from adjusted primes
# n * p(k-1) - m(r)
# Other answers had tropical convolution!?

from number import sieve
primes = sieve(100000)

def M(k, n):
    r = n * (k-1) % k
    # iterative because python can't handle recursion depth 7000
    m = [0] * (r+1)
    for s in range(1, r+1):
        m[s] = primes[k-1] - primes[k-1-s]
        if s > 1:
            m[s] = min(m[s], min(m[j] + m[s-j] for j in range(1,s)))

    return n * primes[k-1] - m[r]

print(M(7000, primes[7000]))
