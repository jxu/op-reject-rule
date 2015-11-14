# Apollonian gasket, Descartes' theorem: (a + b + c + d)^2 = 2(a^2 + b^2 + c^2 + d^2)
from math import pi

start_rad = 1 + 2/(3**0.5)
area = 3*pi*(1/start_rad)**2
MAX_LEVEL = 10

def place_circle(a, b, c, level):
    d = 2*(a*b + a*c + b*c)**0.5 + a + b + c
    global area
    area += pi*(1/d)**2

    if level < MAX_LEVEL:
        place_circle(a, b, d, level+1)
        place_circle(a, c, d, level+1)
        place_circle(b, c, d, level+1)


for i in range(3):
    place_circle(-1, start_rad, start_rad, 1)
place_circle(start_rad, start_rad, start_rad, 1)

print(round((pi - area) / pi, 8))
