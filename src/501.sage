# Sage docs links, because they can be hard to find

# prime_pi(x, prime_bound=0)
# https://doc.sagemath.org/html/en/reference/functions/sage/functions/prime_pi
# count primes <= x, can be real number
# prime_bound to pre-compute?

# prime_range: https://doc.sagemath.org/html/en/reference/rings_standard/sage/rings/fast_arith.html#sage.rings.fast_arith.prime_range
#   primes in range [start, stop-1], needs integer start and stop bounds

n = 10^12
icbrtN = floor(n^(1/3))
cbrtNindex = prime_pi(n^(1/3))
result = (prime_pi(n^(1/7)) 
    + sum(prime_pi(n // p^3) for p in prime_range(icbrtN+1)) 
    - prime_pi(n^(1/4))
    + sum(prime_pi(n // (p * q)) - prime_pi(q) 
          for p in prime_range(icbrtN+1) 
          for q in prime_range(p+1, isqrt(n/p)+1))
)
print(result)
