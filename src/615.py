# Dijkstra like search idea

# best known upper bound: 86597.5

from number import sieve
from heapq import heappush, heappop

max_num = 10**5  # upper bound to tune
N = 10**6
PRIMES = sieve(2 * max_num)
MAX_I = len(PRIMES)

half_primes = [3/2, 2] + [p/2 for p in PRIMES[2:]]

print(half_primes)

visited = []

# store s, min_i
h = [(1,0)]

for t in range(N):
    s, min_i = heappop(h)
    visited.append(s)
    print(s)

    # add new frontier nodes
    for i in range(min_i, MAX_I):
        x = s * half_primes[i]
        if x > max_num: break

        heappush(h, (x, i))

# recover number
x = visited[-1]

pow2 = N
y = x
while int(y) != y:
    y *= 2
    pow2 -= 1

print(x, y, pow2)
print(int(y) * pow(2, pow2, 123454321) % 123454321)