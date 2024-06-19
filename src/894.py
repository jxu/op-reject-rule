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
    s1, s2, s3 = r1**2 * gamma/2, r2**2 * alpha/2, r0**2 * beta/2
    return total_area - s1 - s2 - s3

def f(X):
    x, s, th = X
    return [
        dist2(x, 0,    s * x,   th) - (1 +    s)**2,  # C0 to C1
        dist2(x, 0, s**7 * x, 7*th) - (1 + s**7)**2,  # C0 to C7
        dist2(x, 0, s**8 * x, 8*th) - (1 + s**8)**2   # C0 to C8
    ]

x, s, th = fsolve(f, [2.5, 0.9, 0.8])

print(x, s, th)

print(round((ctri_area(s**0, s**7, s**8) +
             ctri_area(s**0, s**1, s**8)) / (1 - s**2), 10))