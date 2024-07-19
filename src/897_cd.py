import numpy as np

n = 101

def a(x):
    xm1 = np.r_[np.nan, x[:-1]]
    s = (xm1 * x * (x**3 - xm1**3))[1:].sum()
    area = 1 + s/2
    return area  # to maximize

x = np.r_[-1, np.linspace(-.99, 1, n-2), 1]


for r in range(2000):
    for i in range(1, n-1):
        # iterative relaxation / coordinate descent
        # so that partial derivative = 0
        x[i] = np.cbrt((x[i-1]**4 - x[i+1]**4) / (x[i-1] - x[i+1]) / 4)
    print(a(x))

print(round(a(x), 9))