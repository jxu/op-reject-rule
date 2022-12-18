def dist(p0, p1):
    return ((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2) ** 0.5

# split points in linear time
def left_half(Px, Py, L):
    return ([p for p in Px if p[0] < L],
            [p for p in Py if p[0] < L])

def right_half(Px, Py, L):
    return ([p for p in Px if p[0] >= L],
            [p for p in Py if p[0] >= L])


# requires sorted points sorted by x
# Px, Py: points sorted by x and y
def closest_pair(Px, Py):
    n = len(Px)
    if n < 2: return float("inf")
    if n == 2: return dist(Px[0], Px[1])

    L =  Px[n//2][0]  # midway line

    D = min(closest_pair(*left_half(Px, Py, L)),
            closest_pair(*right_half(Px, Py, L)))
    #print(L)
    Sy = [p for p in Py if abs(p[0] - L) < D]

    for i in range(len(Sy)):
        for j in range(1, 16):
            if i+j < len(Sy):
                D = min(dist(Sy[i], Sy[i+j]), D)

    return D
def d(k):
    # RNG ensures no pair of points have same x or y coord
    s = [290797]
    P = []
    for n in range(2*k):
        s.append(s[-1]**2 % 50515093)
        if n % 2 == 0:
            P.append(s[-2:])

    print(P[:10])

    Px = sorted(P, key=lambda p:p[0])
    Py = sorted(P, key=lambda p:p[1])

    return closest_pair(Px, Py)

print(round(d(2*10**6),9))