from number import sieve

def write(file_name, n):
    primes = sieve(n)
    with open(file_name, 'w') as f:
        for p in primes:
            f.write(str(p)+'\n')

write("primes_10_8.txt", 10**8)