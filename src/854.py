from number import fib_list
from math import gcd

F = fib_list(20)
period = []
for i in range(20-1):
    period.append(gcd(F[i], F[i+1]-1))

print(period)