# Numbers must be square-free (otherwise div by d), n = p-1, n = 2(p-2)
from number import sieve

primes = sieve(10**8)
sp = set(primes)
p_minus1 = set(p-1 for p in primes)
p_div2 = set(2*(p-2) for p in primes)
n_intersect = p_minus1.intersection(p_div2)
n_intersect.add(1)

def valid(n):
    for i in range(1, int(n**0.5)+1):
        if n%i == 0 and i + n//i not in sp:
            return False
    return True

print(sum(n for n in n_intersect if valid(n)))
