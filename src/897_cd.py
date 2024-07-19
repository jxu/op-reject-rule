from math import copysign

def real_cbrt(x):  # use math.cbrt in python 3.11+
    return copysign(abs(x)**(1/3), x)

# silly numpy linspace replacement
def linspace(start, end, n):
    step = (end - start) / (n-1)
    return (start + i*step for i in range(n))

n = 101


def a(x):
    return 1 + 0.5*sum(-x[i-1]**4 * x[i] + x[i-1] * x[i]**4
                       for i in range(1, n))



x = [-1] + list(linspace(-.99, 1, n-2)) + [1]
print(len(x), x)


for r in range(2000):
    for i in range(1, n-1):
        # iterative relaxation / coordinate descent
        # so that partial derivative = 0
        x[i] = real_cbrt((x[i-1]**4 - x[i+1]**4) / (x[i-1] - x[i+1]) / 4)
    print(a(x))

print(round(a(x), 9))