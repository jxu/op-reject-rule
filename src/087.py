from number import sieve
primes = sieve(10000)

N = 50000000
nums = [False] * N
sprimes = [p for p in primes if p < N**0.5]
cprimes = [p for p in primes if p < N**(1/3)]
fprimes = [p for p in primes if p < N**0.25]

for s in sprimes:
    for c in cprimes:
            for f in fprimes:
                x = s**2 + c**3 + f**4
                if x < N:
                    nums[x] = True

print(nums.count(True))


