# b'^2 = a' * c'
import number,time
def S(n):
    primes = number.sieve(n)
    sp = set(primes)
    print(primes[:30])

    #factored = [number.prime_factors(p+1) for p in primes]
    #print(factored[:10])
    for p in primes[1:]:
        b = [2] + number.prime_factors((p+1)//2)
        if p % 1000 == 1:
            print(p, b)





start = time.process_time()
S(10**6)
print(time.process_time()-start)