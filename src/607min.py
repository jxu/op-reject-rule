# Setup as pure minimization problem
import numpy as np
from scipy.optimize import minimize

def time(x):
    pts = np.array([
        [-50, 0],
        [x[0], x[0] + 25 * np.sqrt(2)],
        [x[1], x[1] + 15 * np.sqrt(2)],
        [x[2], x[2] +  5 * np.sqrt(2)],
        [x[3], x[3] -  5 * np.sqrt(2)],
        [x[4], x[4] - 15 * np.sqrt(2)],
        [x[5], x[5] - 25 * np.sqrt(2)],
        [50, 0],
    ])

    speeds = np.array([10, 9, 8, 7, 6, 5, 10])

    return sum(
        np.linalg.norm(pts[i+1] - pts[i]) / speeds[i]
        for i in range(7))

# There are some precision problems at the last digit using default BFGS
# Default gradient norm tol (gtol) seems to be 1e-5, which isn't enough
# gtol=1e-5 -> fun = 13.126510858659197 just barely rounds to 13.1265108587
# gtol=1e-6 -> fun = 13.126510858561831 rounds to correct 13.1265108586
# gtol=1e-7 -> fun = 13.126510858560875
# gtol=1e-8 -> fun = 13.126510858560875
result = minimize(time, np.zeros(6), method="BFGS", options={"gtol": 1e-10})

print(result)
print(round(result.fun, 10))