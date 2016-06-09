# Branch and bound for tree squares
# Every square is defined by a vector with initial point coordinates (x,y), 
# magnitude (size of square), and direction.
from __future__ import division
import math


def place_squares(x, y, magnitude, direction):
    if magnitude < 0.1: return
    print(x, y, magnitude, direction)

    # Larger square (initial point: top left of original square)
    ax = x + magnitude * math.cos(math.pi / 2 + direction)
    ay = y + magnitude * math.sin(math.pi / 2 + direction)
    am = (4 / 5) * magnitude
    ad = direction + math.acos(4 / 5)
    # place_squares(ax, ay, am, ad)

    # Smaller square (initial point: at right angle of triangle)
    # Initial point follows larger square vector from larger square start
    bx = ax + am * math.cos(direction + math.acos(4 / 5))
    by = ay + am * math.sin(direction + math.acos(4 / 5))
    bm = (3 / 5) * magnitude
    bd = ad - math.pi / 2
    place_squares(bx, by, bm, bd)


place_squares(0, 0, 1, 0)
