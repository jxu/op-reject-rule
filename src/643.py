from __future__ import division
from number import sieve, combination, product, prime_count
N = 10**2

odd_primes = sieve(int(N**0.5) + 1)[1:]

def combo_max_product(X, terms, max_product):
    '''Like itertools.combinations(X, terms) but only picks values whose
    product is <= max_product.
    '''
    assert sorted(X) == X  # To keep track of index
    result = []

    def f(last_i, terms_so_far, product_):
        if len(terms_so_far) == terms:
            result.append(terms_so_far)
            return

        for i in range(last_i, len(X)):
            new_product = product_ * X[i]
            if new_product <= max_product:
                f(i+1, terms_so_far + [X[i]], new_product)
            else:  # Product too large already
                break

    f(0, [], 1)
    return result


result = combination(N//2, 2)  # All pairs of even nums


new_odd_primes = sieve(N)[1:]
from collections import Counter
c = Counter()
for p in new_odd_primes:
    c[N//(2*p)] += 1


def g(j):
    from math import ceil
    #print(j, (N/j)/2, (N/(j+1))/2)
    upper = prime_count((N/j)/2)
    lower = prime_count((N/(j+1))/2)
    return int(upper - lower)

#r = 0
seen_binom = set()
for p in odd_primes:
    print(N//(2*p))
    seen_binom.add(N//(2*p))
    result -= combination(N//(2*p), 2)


for j in range(2, N//(2*max(odd_primes))):
    print(j, g(j))
    assert c[j] == g(j)
    assert j not in seen_binom
    result -= g(j) * combination(j, 2)


terms = 2
while True:
    # Find combinations of odd primes
    prime_combos = combo_max_product(odd_primes, terms, N)
    if not prime_combos: break

    for combo in prime_combos:
        result += (-1)**terms * combination(N // (2*product(combo)), 2)

    terms += 1


print(result)
print(result % 1000000007)
