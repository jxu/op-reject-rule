import numpy as np
from scipy.optimize import minimize


def a(x):

    #xm1 = np.r_[np.nan, x[:-1]]

    #a = (x - xm1) * (2 - x**4 - xm1**4) / 2
    #area = a[1:].sum()
    #x = np.r_[-1, x, 1]
    n = len(x)

    area = sum((x[i]-x[i-1])*(x[0]**4 + x[-1]**4 - x[i]**4 - x[i-1]**4)/2 for i in range(1, n))

    area = sum(x[i]**4 * (x[i-1] - x[(i+1)%n] ) for i in range(n)) / 2
    area = sum((x[i]**4 + x[i-1]**4)*(x[i] - x[i-1]) for i in range(n)) / 2

    return -area

def grad(x):
    n = len(x)
    xp1 = np.r_[x[1:], np.nan]
    xm1 = np.r_[np.nan, x[:-1]]
    g = -xm1**4 + 4 * x**3 * (xm1 - xp1) + xp1**4
    g[0] = 0
    g[-1] = 0
    return g

print(a(np.array([-0])))

x = np.array([-1,-0.5, 0, 0.5,1])
#step_size = 0.01
# for i in range(100):
#     print(a(x),x, grad(x))
#     x += step_size * grad(x)

res = minimize(a, x, bounds=np.array([(-1,1)]*5))
print(res)

