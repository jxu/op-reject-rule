from itertools import accumulate
from functools import cache

def lower_hull(points):
    """Lower convex hull given points (x, y) in sorted x order, with x distinct
    
    Takes O(n h) time, where h is number of points in hull, using gift-wrap
    """
    hull = [points[0]]

    i = 0
    while points[i][0] < points[-1][0]:
        # find least slope
        def slope(j):
            x_i, y_i = points[i]
            x_j, y_j = points[j]
            return (y_j - y_i) / (x_j - x_i)

        # O(n) min operation to find next i
        i = min(range(i+1, len(points)), key = slope)
        
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

# 1-index?
hull_a = [0] + [p[0] for p in lower_hull(pts_a)]
hull_b = [0] + [p[0] for p in lower_hull(pts_b)]

# DP with hull
print(hull_a)
print(hull_b)

# prefix sum
pre_a = list(accumulate(a))
pre_b = list(accumulate(b))

@cache
def f(i, j):
    if i == 1 and j == 1:
        return a[hull_a[i]] + b[hull_b[j]]

    x = 1e20
    if i > 1:
        x = ((hull_a[i] - hull_a[i-1]) * b[hull_b[j]] + 
             pre_a[hull_a[i]] - pre_a[hull_a[i-1]] + f(i-1, j))

    y = 1e20
    if j > 1:
        y = ((hull_b[j] - hull_b[j-1]) * a[hull_a[i]] + 
             pre_b[hull_b[j]] - pre_b[hull_b[j-1]] + f(i, j-1))

    return min(x, y)


print(f(len(hull_a)-1, len(hull_b)-1))
        