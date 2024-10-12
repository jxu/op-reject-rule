# 2:10 with cache before
# 6 min without cache because OOM

from prime_count import prime_count, PRIMES


def f(n):
    primes = PRIMES[1:]

    # Case 1: n = p^7
    count = prime_count(int(n**(1/7)))

    i = 0
    while (p := primes[i])**3 <= n:
        # Case 2: n = p^3 * q, Exclude case with p == q
        q_max = n // (p**3)
        count += prime_count(q_max) - (q_max >= p)

        # Case 3: n = p*q*r, p < q < r
        j = i + 1
        while (q := primes[j])**2 * p <= n:  # q*q*p < n
            print(p, q)
            # q < r < n/pq, so add pi(n/pq) - pi(q)
            count += prime_count(n // (p*q)) - (j + 1)
            j += 1
        i += 1

    return count


print(f(10**12))
