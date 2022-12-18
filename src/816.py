# Nearest pair of points divide-and-conquer algorithm by Shamos
# Section 5.4 of Algorithm Design book
# Thinkpad benchmark: Pypy3 27s
# Idea: store 2D points as complex numbers?

import numpy as np
from numpy.linalg import norm

def dist(p0, p1):
    return norm(p1 - p0)

# split points in linear time
def left_half(Px, Py, L):
    return (Px[Px[:,0] < L,],
            Py[Py[:,0] < L,])

def right_half(Px, Py, L):
    return (Px[Px[:,0] >= L,],
            Py[Py[:,0] >= L,])


# requires sorted points sorted by x
# Px, Py: points sorted by x and y
def closest_pair(Px, Py):
    n = len(Px)
    if n < 2: return float("inf")
    if n == 2: return dist(Px[0], Px[1])

    L =  Px[n//2, 0]  # midway line
    D = min(closest_pair(*left_half(Px, Py, L)),
            closest_pair(*right_half(Px, Py, L)))

    Sy = Py[abs(Py[:,0] - L) < D, ]

    for i in range(len(Sy)):
        for j in range(1, min(16, len(Sy)-i)):
            D = min(dist(Sy[i], Sy[i+j]), D)

    return D
def d(k):
    # RNG ensures no pair of points have same x or y coord
    P = np.zeros((k, 2))
    M = 50515093
    s0 = 290797
    s1 = pow(s0, 2, M)
    P[0,] = np.array([s0, s1])
    for n in range(1, k):
        s0 = pow(s1, 2, M)
        s1 = pow(s0, 2, M)
        P[n,] = np.array([s0, s1])

    Px = P[np.argsort(P[:,0]),]
    Py = P[np.argsort(P[:,1]),]


    return closest_pair(Px, Py)

print(round(d(2*10**6),9))