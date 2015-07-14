def same_side(ax, ay, bx, by, p1x, p1y, p2x, p2y):
    # p1 and p2 on same side of AB
    Ax, Ay = bx - ax, by - ay
    Ux, Uy = p1x - ax, p1y - ay
    Vx, Vy = p2x - ax, p2y - ay

    cp1 = Ax*Uy - Ay*Ux
    cp2 = Ax*Vy - Ay*Vx

    return cp1*cp2 >= 0  # Interior or boundary


def point_in_triangle(px, py, ax, ay, bx, by, cx, cy):
    return same_side(bx, by, cx, cy, px, py, ax, ay) and same_side(ax, ay, cx, cy, px, py, bx, by) and \
            same_side(ax, ay, bx, by, px, py, cx, cy)


with open("p102_triangles.txt") as f:
    cases = f.read().split('\n')

cases = [list(map(int, case.split(','))) for case in cases[:-1]]
results = [point_in_triangle(0, 0, c[0], c[1], c[2], c[3], c[4], c[5]) for c in cases]
print(sum(results))
