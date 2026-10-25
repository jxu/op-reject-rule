from itertools import accumulate

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

        # O(n) min operation
        j = min(range(i+1, len(points)), key = slope)
        
        hull.append(points[j])
        i = j

    return hull


N = 10**7

a = [0]
b = [0]
s = 102022661
for n in range(1, 2*N+1):
    if n % 2: a.append(s)
    else: b.append(s)
    s = (s*s) % 998388889

points = [(j, b[j]) for j in range(1, N+1)]

# 1-index?
hull = [(0,0)] + lower_hull(points)
h = [p[0] for p in hull]

# DP with hull
print(hull)
print(h)


# prefix sum
pre = list(accumulate(b))
#print(pre)

from functools import cache

dp = [[0] * len(h)]

for i in range(1, N+1):
    new_dp = [0] * len(h)  # dp[i][k]
    for k in range(1, len(h)):
        if i == 1 and k == 1:
            new_dp[k] = a[i] + b[h[k]]
            continue

        x = 1e20
        if i > 1:
            x = a[i] + b[h[k]] + dp[k]

        y = 1e20
        if k > 1:
            y = (h[k] - h[k-1]) * a[i] + pre[h[k]] - pre[h[k-1]] + new_dp[k-1]

        new_dp[k] = min(x, y)

    dp = new_dp

print(dp[-1])
    