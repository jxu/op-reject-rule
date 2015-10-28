# G = 1 + z + 2z^2 + ... = 1/(1 -z - z^2)
# A(x) = x*G = x/(1 - x - x^2)  Discriminant = 5A^2 + 2A + 1
# Recurrence relations from http://www.alpertron.com.ar/QUAD.HTM
from number import is_square

def r(x, y): return (-9*x - 4*y - 2, -20*x - 9*y - 4)

x1, y1 = 0, 1
x2, y2 = 0, -1
x3, y3 = -1, -2
x4, y4 = -1, 2

nuggets = set()

for i in range(20):
    print(x1, x2, x3)
    for x in (x1, x2, x3):  # x3 and x4 generate same solutions
        if x > 0 and is_square(5*x**2 + 2*x + 1): nuggets.add(x)

    x1, y1 = r(x1, y1)
    x2, y2 = r(x2, y2)
    x3, y3 = r(x3, y3)
    x4, y4 = r(x4, y4)

print(sorted(nuggets))
print(sorted(nuggets)[14])
