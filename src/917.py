"""Minimal Path Using Additive Cost

Really interesting and hard problem. I suspected convex hull but didn't see
how to make it work for a while.

My idea was to turn the 2D path problem into a 1D problem, as only 2N values
generate the entire matrix. Going row-by-row:
Pick 0 = x_0 <= x_1 <= ... <= x_n = n as transition points between rows
so the path is thus 
(1, x_0) to (1, x_1)
(2, x_1) to (2, x_2)
...
(n, x_{n-1}) to (n, x_n)

The sum cost per row i: 
a_i * (x_i - x_{i-1} + 1) + sum_{j=x_{i-1}..x_i} b_j

Isolating per x_i (for 1 <= i <= n-1):
(a_i - a_{i+1}) * x_i + b_{x_i}

Letting j = x_i, this is a linear cost like d_i * j + b_j (d_i can be < 0)

After guessing convex hull over points (j, b_j) would work, 
(actually the first thing I came up with is more like Pareto frontier)
I came up with an argument:
Any interior point (x, y) of the hull is above some segment of the convex hull
(x1, y1) to (x2, y2).
Due to the linear cost c(x, y) = d*x + y, any point along that segment, say ((1-λ)x1 + λx2, (1-λ)y1 + λy2),
will have cost >= smaller cost of the endpoints, and the interior point has
larger y, so will be more expensive as well.

So while the standard DP uses something like 
A(i, j) = a_i + b_j + min(A(i-1, j), A(i, j-1))
we only need to consider j values in the convex hull.
Later I realized this argument applies symetrically to (i, a_i).

Let h_i and h_j be the number of points in each convex hull. Then the DP
only has h_i * h_j states, which is quite tiny.
Theorem (Rényi and Sulanke, 1963): 
For random points in a rectangular area, the number of points on
the convex hull is O(log n).
So our compressed DP only needs O(log^2 n) space and time.
"""


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

    # DP of cost from the sparse i and j from their convex hulls
    # Use prefix sums to precompute fixed sums of a_i or b_j
    return min(
        (hull_a[i] - hull_a[i-1]) * b[hull_b[j]] + 
            pre_a[hull_a[i]] - pre_a[hull_a[i-1]] + f(i-1, j),
        (hull_b[j] - hull_b[j-1]) * a[hull_a[i]] + 
            pre_b[hull_b[j]] - pre_b[hull_b[j-1]] + f(i, j-1))


print(f(len(hull_a)-1, len(hull_b)-1))