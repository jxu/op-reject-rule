from itertools import accumulate
from functools import cache

def cross2d(p0, p1, p2):
    """2D cross product (p1 - p0) x (p2 - p0)
    
    Equals signed area of parallelogram formed by vectors p0p1 and p0p2.
    If positive, p2p0 is counterclockwise from p0p1
    If negative, p2p0 is clockwise from p0p1
    """
    return (p1[0]-p0[0]) * (p2[1]-p0[1]) - (p2[0]-p0[0]) * (p1[1]-p0[1])


def lower_hull(points):
    """Lower convex hull given points (x, y) with sorted distinct x.

    Andrew's monotone chain algorithm in O(n) time.
    """
    hull = points[0:3]

    for i in range(3, len(points)):
        # makes a CW (or non-CCW) turn
        while cross2d(hull[-2], hull[-1], points[i]) <= 0:
            hull.pop()

        hull.append(points[i])

    return hull


N = 10**7

a, b = [0], [0]
s = 102022661
for n in range(N):
    a.append(s)
    s = (s*s) % 998388889
    b.append(s)
    s = (s*s) % 998388889


pts_a = [(i, a[i]) for i in range(1, N+1)]
pts_b = [(j, b[j]) for j in range(1, N+1)]

hull_a = [p[0] for p in lower_hull(pts_a)]
hull_b = [p[0] for p in lower_hull(pts_b)]

# DP with hull
print(hull_a)
print(hull_b)

# prefix sum
pre_a = list(accumulate(a))
pre_b = list(accumulate(b))

@cache
def f(i, j):
    if i < 0 or j < 0:
        return float("inf")  # simplify min at boundary cases

    if i == 0 and j == 0:
        return a[hull_a[i]] + b[hull_b[j]]

    return min(
        (hull_a[i] - hull_a[i-1]) * b[hull_b[j]] + 
            pre_a[hull_a[i]] - pre_a[hull_a[i-1]] + f(i-1, j),
        (hull_b[j] - hull_b[j-1]) * a[hull_a[i]] + 
            pre_b[hull_b[j]] - pre_b[hull_b[j-1]] + f(i, j-1))


print(f(len(hull_a)-1, len(hull_b)-1))
        