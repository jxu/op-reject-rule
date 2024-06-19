# Some simple trigonometry and geometry (in polar coordinates)
# Let circle C0 be centered at (x, 0) with radius 1
# Let circles Ck be centered at (s^k x, s theta) where s and theta are
# scaling and rotation factors
# As circles C1, C8, C9 are tangent to C0, the distances between centers
# d(C0, C1) = 1 + s, d(C0, C7) = 1 + s^7, d(C0, C8) = 1 + s^8
#
# Polar distance can be calculated with Law of Cosines
# The variables (x, s, theta) are solved numerically with scipy's fsolve
# (internally, MINPACK's hybrd routines of modified Powell method)
#
# Then circular triangle areas are computed with finding the angles and then
# law of cosines and law of sines. (Total triangle area can also be found with
# Heron's formula.) For the two spirals of triangles, the "outer" and "inner"
# triangles, each next triangle's sides are scaled by s so area is scaled by
# s^2, so the infinite sum is a geometric series.
#
# The circles can also be neatly expressed in complex numbers, where the
# scaling and rotation are combined into one parameter z. For example:
# C0 is centered at x, C1 is centered at zx with radius |z|.
# Then d(C0, c1) = 1 + |z| = |xz - x|
# This doesn't seem to make the actual computations that much simpler though.


from numpy import sin, cos, arccos, arcsin
from scipy.optimize import fsolve

def dist2(r1, th1, r2, th2):
    """Calculate distance between two points in polar coords."""
    return r1**2 + r2**2 - 2*r1*r2*cos(th2 - th1)  # law of cosines

def ctri_area(r0, r1, r2):
    """Calculate circular triangle area between circles of radii r0, r1, r2."""
    a, b, c = r0+r1, r1+r2, r2+r0
    gamma = arccos((a**2 + b**2 - c**2) / (2*a*b))  # law of cosines
    alpha = arcsin(a * sin(gamma) / c)  # law of sines
    beta  = arcsin(b * sin(gamma) / c)
    total_area = a * b * sin(gamma) / 2
    s1, s2, s3 = r1**2 * gamma/2, r2**2 * alpha/2, r0**2 * beta/2  # sector
    return total_area - s1 - s2 - s3

def f(X):
    x, s, th = X
    return [
        dist2(x, 0, s**1 * x,   th) - (1 + s**1)**2,  # C0 to C1
        dist2(x, 0, s**7 * x, 7*th) - (1 + s**7)**2,  # C0 to C7
        dist2(x, 0, s**8 * x, 8*th) - (1 + s**8)**2   # C0 to C8
    ]

x, s, th = fsolve(f, [2.5, 0.9, 0.8])  # numerically solve roots
print(x, s, th)

a = (ctri_area(s**0, s**7, s**8) + ctri_area(s**0, s**1, s**8)) / (1 - s**2)
print(round(a, 10))