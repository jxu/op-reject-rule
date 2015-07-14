# Reducing fractions is totient, also known as Farey sequence
from number import phi
print(sum(phi(n) for n in range(2, 1000001)))