# c+1 = (b+1)^2 / (a+1)
import number,time
def S(n):
    primes = number.sieve(n)
    sp = set(primes)

    #for ai in range(len(primes)):
    #    print(primes[ai])
    #    for bi in range(ai+1, len(primes)):
    #        a = primes[ai]
    #        b = primes[bi]



S(10**4)