

def lower_hull(points):
    """Lower convex hull given points (x, y) in sorted x order, with x distinct"""
    # Gift-wrap
    x0, y0 = points[0]
    hull = [points[0]]

    i = 0
    pt = points[0]
    x_i, y_i = pt

    while x_i < points[-1][0]:
        # find least slope?
        best_slope = float("inf")
        best_j = None
        for j in range(i+1, len(points)):
            x_j, y_j = points[j]
            slope = (y_j - y_i) / (x_j - x_i)
            if slope < best_slope:
                best_slope = slope
                best_j = j
            
        hull.append(points[best_j])

        i = best_j
        x_i, y_i = points[best_j]



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


from itertools import accumulate
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

print(dp)
    