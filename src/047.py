from number import sieve, factor
N = 5 * 10**5
primes = sieve(N)
w = [0] + [len(factor(n, primes).keys()) for n in range(1, N)]

for i in range(1, N-3):
    if 4 == w[i] == w[i+1] == w[i+2] == w[i+3]:
        print(i)
        break
