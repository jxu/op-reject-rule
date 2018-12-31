from number import sieve, combination, product
n = 10**2
primes = sieve(n)

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


result = combination(n//2, 2)
terms = 1
while True:
    # Find combinations of primes other than 2
    prime_combos = combo_max_product(primes[1:], terms, n)
    if not prime_combos: break

    for combo in prime_combos:
        result += (-1)**terms * combination(n // (2*product(combo)), 2)

    terms += 1


print(result % 1000000007)
