# Bounding envelope/parabola given by max y, max x
# Form: x = a - by^2
# Volume is integration about y axis = pi * I(f(y) dy, 0, max_y)

from scipy.integrate import quad
import numpy.polynomial.polynomial as poly
from numpy import pi

v = 20
g = 9.81
max_y = v**2 / (2*g) + 100
b = -g / (2 * v**2)

x_2 = poly.Polynomial([-max_y/b, 1/b])

print(x_2, 0, max_y)
result = pi * quad(x_2, 0, max_y)[0]

print(round(result, 4)) # 557904400000000*pi/944076141
