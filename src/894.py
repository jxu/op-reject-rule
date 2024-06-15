import numpy as np
from scipy.optimize import fsolve

def f(X):
    x, s, th = X
    return [
        x**2 + (s*x)**2 - 2*x*(s*x) * np.cos(th) - (1 + s)**2,
        x**2 + (s**7 * x)**2 - 2*x*(s**7 * x) * np.cos(7 * th) - (1 + s**7) ** 2,
        x**2 + (s**8 * x)**2 - 2*x*(s**8 * x) * np.cos(8 * th) - (1 + s**8)**2
    ]

x, s, th = fsolve(f, [2.5, 0.9, np.pi/4])

print(x, s, th)