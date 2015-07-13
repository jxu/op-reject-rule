# Search all primes, skipping seen cases (ex. 56**3)
from number import sieve

def family(max_test, family_size):
    primes = sieve(max_test)
    primes_set = set(primes)
    seen = set()

    for p in primes:
        sp = str(p)
        digits = list(sp[:-1])

        for d in digits:
            case = ''.join(['*' if c==d else c for c in sp])
            if case in seen:
                break
            else:
                seen.add(case)

            family = []
            for a in range(10):
                q = sp.replace(d, str(a))
                if q[0] != '0' and int(q) in primes_set:
                    family.append(int(q))

            if len(family) == family_size:
                print(case)
                return family[0]

print(family(10**6, 8))