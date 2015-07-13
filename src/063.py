s = 0
for exp in range(1, 30):  # Max 9^21
    for x in range(1, 10):
        if len(str(x**exp)) == exp:
            s += 1

print(s)

# Mathematical solution 9^x < 10^(x-1)
from math import log10
print(sum(int(1/(1 - log10(k))) for k in range(1, 10)))