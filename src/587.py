# Throwback to Mathcounts days :P
# No need for integration, only basic trig.
# Call P(x,y) the intersection between line y=x/n and circle (x-1)^2 + (y-1)^2 = 1
# For areas, concave triangle + circular sector + remaining quadrilateral =
# total area of unit square from (0,0) to (1,1) = 1

# (Quadrilateral has points (0,0), (0,1), (1,0), (x,y))
# (Sector bounded by line between P and center and x=1)

import math

def area_ratio(n):
    Py = (n - (2*n)**0.5 + 1) / (n**2 + 1)
    Px = n * Py

    theta = math.asin(1 - Px)
    sector_area = theta / 2

    quad_area = (Px - Py + 1)/2  # x(1-y) + (1-x)(1-y)/2 + xy/2
    concave_triangle = 1 - sector_area - quad_area

    l_section = 1 - math.pi/4
    return concave_triangle / l_section

for n in range(1, 10000):
    if area_ratio(n) < 0.001:
        print(n)
        break