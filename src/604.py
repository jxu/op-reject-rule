# The slopes between each lattice point should be increasing:
# delta y / delta x with x and y coprime to avoid passing through another
# lattice point.
# The most efficient strategy is to take fractions with x+y = 2 (1/1), then
# x+y = 3 (1/2, 2/1), x+y = 4 (1/3, 3/1), x+y = 5 (1/4, 4/1, 2/3, 3/2), etc.
# There are precisely phi(n) fractions with x+y = n, so each n contributes
# n * phi(n) to delta x and delta y, and phi(n) to the lattice point count.

from number import totient_range

totients = totient_range(5*10**6)

def F(N):
    points = 0
    dx_left = 2*N
    n = 1
    while dx_left - n * totients[n] >= 0:
        dx_left -= n * totients[n]
        points += totients[n]
        n += 1

    points += dx_left // n  # Remaining fracs that can still be added
    return points

print(F(10**18))