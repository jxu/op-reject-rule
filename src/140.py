# Like #137, use generating function
# sum(G_{n+2}*z^n) = sum(G_{n+1}*z^n) + sum(G_n*z^n)  Recurrence
# g(z) = sum(G_n*z^n),  => g(z)/z^2 - G_2/z^2 - G1/z = g(z)/z - G1/z + g(z)
# => g(z) = (1+3z)/(1-z-z^2),  A = z*g(z) = (z+3z^2)/(1-z-z^2)  Discriminant: 5A^2 + 14A + 1
from number import is_square

# Alpern Diophantine solver
# Starting pairs (0, +-1) (-3, +-2) (-4, +-5) (2, +-7)
xy = [(0, -1), (0, 1), (-3, -2), (-3, 2), (-4, -5), (-4, 5)]  # (2, +-7) unneeded

nuggets = set()
for i in range(15):
    print([p[0] for p in xy])
    for pair in xy:
        x = pair[0]
        if x > 0 and is_square(5*x**2 + 14*x + 1):
            nuggets.add(x)

    for j in range(len(xy)):
        x = xy[j][0]
        y = xy[j][1]
        xy[j] = (-9*x - 4*y - 14, -20*x - 9*y - 28)


print(sorted(nuggets))
print(sum(sorted(nuggets)[:30]))
