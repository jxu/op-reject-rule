# We maximize the score with the best-case array [k-1] * n,
# but this array sum is r = n*(k-1) % k = 6337 above a multiple of k.
# So, minimize score loss p(k-1) - p(k-1-a_i) for a_i summing to r
# This is knapsack with s < n, so DP:
# m(s) = min(p(k-1) - p(k-1-s), min_{0<i<s} m(i) + m(s-i))
# This is O(k^2) and the result is max score minus gaps from adjusted primes
# n * p(k-1) - m(r)

# Other methods
# radeye, Icy0: Find which index decrements have the least proportional loss
# on the sum
# vikt, hitorare: (DP without assuming final a_i sum)
# Let d_n[r] be max score for n ints with score r mod k.
# For m1 + m2 = n, d_n[r] = max_{i+j = r mod k} d_m1[i] + d_m2[j]
# base case d_1[r] = max_{p(i) = r mod k} p(i)
# The straightforward solution with m1 = n-1, m2 = 1 takes O(k^2 n) time
# since the (max,+) convolution is associative, we can use exponentiation by
# squaring to solve in O(k^2 log n) time

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
