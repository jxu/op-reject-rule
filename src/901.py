from math import exp, log

x = list(range(100)) + [1000]

for l in range(100):
    for i in range(1, len(x)-1):
        x[i] = - log(exp(-x[i-1]) / x[i+1])

    d = 0
    for i in range(1, len(x)):
        d += exp(-x[i-1]) * x[i]

    print(d)

print(x)
