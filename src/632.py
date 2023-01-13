# By inclusion-exclusion the number of square-free integers below N is
# sum_{n=1..sqrt(N)} mu(n) floor(N / n^2)
# https://math.stackexchange.com/a/2888117 for more details
# Instead of calculating mu(n), I keep track of over a range of numbers
# how many times a prime factor divides a number, ignoring numbers divisible by
# a prime more than once.
# Let A_i be the set of multiples of the ith prime.
# For k = 0 we want everything not in the intersection of A_i's
# For k = 1 we want everything in exactly one A_i.
# For k = 2 we want everything in exactly two A_i's
# This is the generalized inclusion-exclusion principle and the coefficient for
# the intersection of m sets is (-1)^(m+k) C(m, k)

from number import sieve, comb, prod

def C(N):
    sqrt_N = int(N**0.5)
    primes = sieve(sqrt_N+1)
    p_count = [0] * (sqrt_N+1)

    for p in primes:
        for n in range(p, sqrt_N+1, p):
            if n % p == 0 and p_count[n] != None:
                p_count[n] += 1
            if n % p**2 == 0:
                p_count[n] = None

    C_k = [0] * (max(p_count)+1)
    for n in range(1, sqrt_N + 1):
        if p_count[n] == None: continue
        for k in range(len(C_k)):
            C_k[k] += ((-1)**(p_count[n]+k)) * \
                      comb(p_count[n], k) * (N // n ** 2)

    print(C_k)
    return prod(C_k)

print(C(10**16)) % 1000000007