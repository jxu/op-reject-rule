# Somehow Project Euler currently considers this the hardest problem I've 
# solved, although I don't think it is. But I admit that in my previous 
# Mathematica solution I didn't understand SymmetricPolynomial.
#
# The formula for c_7^inf was inspired by the well-known derivation for c_0^inf,
# the (limiting) proportion of square-free integers. It comes from
#     (3/4)(8/9)(24/25)...
# using the reasoning (in the limit) 3/4 of integers aren't divisible by 2^2,
# 8/9 aren't divisible by 3^2, etc., and each p^2 is independent due to the CRT.
# This gives 
#
#     prod_p (1 - 1/p^2) = zeta(2)^(-1) = 6/pi^2
#
# from the Euler product.
#
# For k = 1, we can consider each p separately: multiply 6/pi^2 by
# 1/(p^2 - 1) to include div by p^2 instead of excluding it.
# For example, for p = 2: (3/4)(1/3) = 1/4.
# I verified that c_1^inf = (6/pi^2) * sum_p 1/(p^2 - 1).
#
# For larger k, scale by the sum of products over all k-subsets of primes:
#
#     sum_{i_1 < ... < i_k} (1/(p_{i_1}^2 - 1)) * ... * (1/(p_{i_k}^2 - 1))
#
# A long time ago I asked on Math Stack Exchange and learned that this can be
# computed exactly with Newton's identities.
# Define the elementary symmetric polynomials:
#
#     e_k(x_1, ..., x_n) = sum_{i_1 < ... < i_k} x_{i_1} * ... * x_{i_k}
#
# i.e. the sum of the products of all k-subsets of {x_1, ..., x_n}.
# Define the k-th power sums:
#
#     p_k(x_1, ..., x_n) = sum_i x_i^k
#
# Newton's identities give us a convenient way of computing e_k:
#
#     e_k = (1/k) * sum_{i=1}^k (-1)^(i-1) * e_{k-i} * p_i
#
# So I can compute from the power sums with n terms instead of iterating over
# the (n choose k) k-tuples.
#
# Another way to do it would be to generate all 7-subsets until the denominator
# of the factor gets very small. Or use a fancy generating-function approach
# using the complete exponential Bell polynomials.

from number import sieve
from functools import cache 
from math import pi

primes = sieve(10**6)

@cache
def p(k):
    return sum((q**2 - 1)**-k for q in primes)

@cache
def e(k):
    if k == 0: return 1
    return sum((-1)**(j-1) * e(k-j) * p(j) for j in range(1, k+1)) / k

def c(k):
    return (6 / pi**2) * e(k)

print(f"{c(7):.4e}")
