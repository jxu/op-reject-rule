# Collect unique lines by using rational slope-intercept form
# (For vertical lines, slope=inf and offset is x coord)
# Then for every line, count intersections (# of other lines - # of parallel)
# 200 solved!

from fractions import Fraction
from itertools import combinations
from collections import Counter

def SL(n):
    S = 290797
    T = []
    for i in range(2*n+1):
        T.append((S % 2000) - 1000)
        S = S**2 % 50515093

    points = [(T[2*k-1], T[2*k]) for k in range(1, n+1)]
    lines = set()

    for combo in combinations(points, 2):
        ax, ay = combo[0]
        bx, by = combo[1]
        if ax == bx:
            slope = float("inf")
            offset = ax
        else:
            slope = Fraction(by - ay, bx - ax)
            offset = ay - slope * ax

        lines.add((slope, offset))

    slopes_counter = Counter()  # For unique lines
    for line in lines:
        slopes_counter[line[0]] += 1

    crossings = 0
    for line in lines:
        crossings += len(lines) - slopes_counter[line[0]]

    return crossings


print(SL(2500))

