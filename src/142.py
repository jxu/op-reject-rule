# Brute force: Parametrization of a^2 + b^2 = c^2 + d^2
MAX_TEST = 1000

sum_squares = set()
for e in range(1, MAX_TEST):
    for f in range(e, MAX_TEST):
        sum_squares.add(e**2+f**2)

squares = set(i**2 for i in range(1, MAX_TEST))

for q in range(1, MAX_TEST):
    for r in range(1, MAX_TEST):
        for s in range(1, MAX_TEST):
            for p in range(q*s//r, min(q*r//s + 1, MAX_TEST)):
                if q*r > p*s and p*r > q*s:
                    a, b, c, d = p*r + q*s, q*r - p*s, p*r - q*s, p*s + q*r
                    if a%2 == b%2 and c%2 == d%2 and a**2 + b**2 in sum_squares:
                        x = (a**2 + b**2) // 2
                        y = (a**2 - b**2) // 2
                        z = c**2 - x
                        if z > 0 and y+z in squares and y-z in squares:
                            print(x, y, z, '|', x+y, x-y, x+z, x-z, y+z, y-z, '|', x+y+z)
