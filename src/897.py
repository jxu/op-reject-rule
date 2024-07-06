import numpy as np
from scipy.optimize import minimize  # use cpython with scipy

def shiftm1(x):
    return np.r_[np.nan, x[:-1]]

def a(x):
    x = np.r_[-1,x,1]  # fixed endpoints at -1 and 1
    xm1 = np.r_[np.nan, x[:-1]]
    a = (xm1 * x * (x**3 - xm1**3))[1:].sum()
    area = 1 + a/2
    return -area

def grad(x):
    x = np.r_[-1, x, 1]
    xm1 = np.r_[np.nan, x[:-1]]
    xp1 = np.r_[x[1:], np.nan]
    g = (-xm1**4 + 4*x**3 * (xm1 - xp1) + xp1**4)[1:-1]

    return -g

x = np.linspace(-.9, 1, 101-2)

# options={"ftol":1e-10, "gtol":1e-10, "maxfun":100000}
res = minimize(a, x, jac=grad, options={"gtol":1e-9})
print(res)
print(round(res.fun, 9))
