# Level 10, 250 solved!
# n=5 isn't symmetric! But (-1,1) and (1,1) have to be endpoints in convex
# I tried many different optimization methods, even random basin-hopping, even
# Hessian before, but for some reason it worked now with Hessian information.
# Optimizing area under the n-gon turns out to be the same as maximizing n-gon
# area, so doesn't help.

# Also I computed gradients, with partial derivatives
# dA / dx_i = -4 x_{i-1}^3 + 4 x_{i-1} x_i^3 - 4 x_i^3 x_{i+1} + x_{i+1}^4
# dA / dx_i = 0 =>
# x_i = cbrt((1/4) (x_{i-1}^4 - x_{i+1}^4) / (x_{i-1} - x{i+1}))
# Endagorion suggests iterating over coordinates based on grad which I didn't
# consider would work. See alternate solution.

import numpy as np
from scipy.optimize import minimize  # use cpython with scipy


def a(x):
    x = np.r_[-1,x,1]  # fixed endpoints at -1 and 1
    xm1 = np.r_[np.nan, x[:-1]]
    s = (xm1 * x * (x**3 - xm1**3))[1:].sum()
    area = 1 + s/2
    return -area  # to minimize

def grad(x):
    x = np.r_[-1, x, 1]
    xm1 = np.r_[np.nan, x[:-1]]
    xp1 = np.r_[x[1:], np.nan]
    g = (-xm1**4 + 4*x**3 * (xm1 - xp1) + xp1**4)[1:-1]

    return -g

def hess(x):
    x = np.r_[-1, x, 1]
    n = len(x)
    H = np.zeros((n,n))
    for i in range(1, n-1):
        H[i,i] = 12 * x[i]**2 * (x[i-1] - x[i+1])
        H[i,i-1] = -4 * x[i-1]**3 + 4 * x[i]**3
        H[i,i+1] =  4 * x[i+1]**3 - 4 * x[i]**3

    return -H[1:-1,1:-1]

n = 101
x0 = np.linspace(-.99, 1, n-2)  # asymmetric start

res = minimize(a, x0, jac=grad, hess=hess, method="newton-cg")

print(res)
print(res.x)
print(-round(res.fun, 9))
