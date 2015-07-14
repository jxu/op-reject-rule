from decimal import *
getcontext().prec = 110

s = 0
for n in range(101):
    z = str(Decimal(n).sqrt())
    if round(n**0.5)**2 != n:
        s += sum(map(int, z[0] + z[2:101]))

print(s)
