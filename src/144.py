a, b = 1.4, -9.6
r_slope = (-9.6 - 10.1) / (1.4 - 0)

for bounce in range(1000):
    if -0.01 <= a <= 0.01 and b > 9.99:
        print(bounce)
        break

    # Calculate normal
    normal_slope = -1 / (-4*a / b)
    magnitude = (1 + normal_slope**2)**0.5
    normal_x = 1 / magnitude
    normal_y = normal_slope / magnitude

    # Calculate new slope
    dp = 1 * normal_x + r_slope * normal_y
    new_rx = 1 - 2 * dp * normal_x
    new_ry = r_slope - 2 * dp * normal_y
    r_slope = new_ry / new_rx  # New slope
    print(r_slope)

    # Calculate new point (a + t, b + r*t) (equation from WA)
    dis = (25 - a**2)**0.5*r_slope
    if b < 0: dis *= -1
    t = -4*(dis + 2*a) / (r_slope**2 + 4)

    a, b = a + t, b + r_slope*t
    print(a, b)
    r_slope = r_slope