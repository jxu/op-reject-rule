from number import sieve, combination

primes = sieve(int(combination(50, 25)**0.5)) # Max prime
prime_squares = [p**2 for p in primes]
square_free = set()
steps = 0

def is_square_free(c):
    for ps in prime_squares:
        global steps
        steps += 1
        if ps > c: return True
        if c % ps == 0: return False
    print("error")

for n in range(0, 51):
    for k in range(0, n//2 + 1):
        c = combination(n, k)
        if is_square_free(c): square_free.add(c)

print("Steps:", steps)
print(sum(square_free))


