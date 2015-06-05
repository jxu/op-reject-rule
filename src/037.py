import number

def both_truncate(n):
    l = []
    for i in range(1, len(str(n))):
        l.append(int(str(n)[:-i]))
        l.append(int(str(n)[i:]))

    return l

primes = number.sieve(10**6)
s = 0
for p in primes:
    if p > 7 and all(i in primes for i in both_truncate(p)):
        s += p

print(s)
