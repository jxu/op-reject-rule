# A much more elegant solution using Snell's Law
# The rest of the angles of incidence are determined by the first one, so
# binary search the first angle that gets the dist travelled parallel to
# marsh borders closest to 50*sqrt(2)

from math import sin, asin, cos, tan

speeds = (10, 9, 8, 7, 6, 5, 10)
d0 = 25 * (2**0.5 - 1)
perp_dist = (d0, 10, 10, 10, 10, 10, d0)

def time(angles):
    return sum((perp_dist[i] / cos(angles[i]) / speeds[i] for i in range(7)))

def parallel_travelled(angles):
    return sum(perp_dist[i] * tan(angles[i]) for i in range(7))

def get_angles(a0):
    angles = [a0]
    for i in range(6):
        angles.append(asin(speeds[i+1] * sin(angles[i]) / speeds[i]))
    return angles


l, h = 0, 2
angles = None
for i in range(50):
    m = (l+h) / 2
    angles = get_angles(m)
    print(m, time(angles))
    if parallel_travelled(angles) > 50 * 2**0.5:
        h = m
    else: l = m

print(round(time(angles), 10))