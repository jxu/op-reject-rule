from number import sieve


primes = sieve(10**6)


    
def S(n):
    result = [1]

    # non-recursive version
    for p in primes:
        result = sorted(result)
        new_result = result.copy()
        for x in result:

            y = p**3 * x
            while y <= n:
                new_result.append(y)
                y *= p

        result = new_result 







    s = n
    for x in result:
        if x == 1: continue
        s += n // x
    return s

print(S(10**4))
