import numpy as np
from scipy.optimize import minimize


def a(x):
    x = np.r_[-1,x,1]  # fixed endpoints at -1 and 1
    n = len(x)
    y = x**4
    area = sum((x[i] - x[i-1])*(2 - y[i] - y[i-1]) for i in range (1,n)) / 2

    # telescoping more stable?
    area = 1 + sum(x[i-1]*x[i]*(x[i]**3 - x[i-1]**3) for i in range(1,n))/2

    return -area

def grad(x):
    x = np.r_[-1, x, 1]
    g = np.array([-x[i-1]**4 + 4 * x[i]**3 * (x[i-1] - x[i+1]) + x[i+1]**4 for i in range(1,len(x)-1)])

    return -g

x = np.linspace(-.9, 1, 101-2)
# options={"ftol":1e-10, "gtol":1e-10, "maxfun":100000}
res = minimize(a, x, bounds=np.array([(-1,1)]*len(x)), jac=grad)
print(res)
print(round(res.fun, 9))
