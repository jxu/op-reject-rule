with open("p102_triangles.txt") as f:
    cases = f.read().split('\n')

cases = [map(int, case.split(',')) for case in cases[:-1]]
t = 0
for case in cases:
    ax, ay, bx, by, cx, cy = case
    cp1 = (ax*by - ay*bx >= 0)
    cp2 = (bx*cy - by*cx >= 0)
    cp3 = (cx*ay - cy*ax >= 0)
    t += (cp1 == cp2 == cp3)

print(t)
