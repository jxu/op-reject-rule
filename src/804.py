# Although g(n) is formulated for exact n, the problem is just counting
# lattice points within the (slightly rotated) ellipse
# (No quadratic number fields here)
# 1 <= x^2 + xy + 41y^2 <= N

# (Counting x values per y is more efficient, since fewer y's)
# lower bound only excludes (0,0)
# x values given by (-sqrt(D)-y)/2 <= x <= (sqrt(D)-y)/2 in constant time
# where disc D = 4N - 163y^2, and y range is when disc >= 0 (O(sqrt N) y's)

# Aside: My original wrong answer was 4921370551114716. I thought it was an
# error due to doubles only having ~15 digits of precision, but turns out it
# was me doing rounding wrong. I assumed x_min < 0 and x_max > 0 so used
# int(x) which rounds towards zero, instead of floor and ceil.

# Other ideas from problem thread:
# endagorion: maintain [x_min, x_max] and change interval through changing y
# ironman353 / ecnerwala: actual quadratic number field solution
# griff / abcwuhang: convex hull trick in O(N^1/3)

from math import floor, ceil

def T(N):
    y_max = int((4*N / 163)**0.5)
    s = -1  # exclude (0,0)

    for y in range(-y_max, y_max+1):
        sqrt_disc = (4*N - 163*y**2)**0.5
        x_min = ceil((- sqrt_disc - y) / 2)
        x_max = floor((sqrt_disc - y) / 2)
        s += x_max - x_min + 1

    return s

print(T(10**16))