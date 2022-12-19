# Nearest pair of points divide-and-conquer algorithm by Shamos
# Section 5.4 of Algorithm Design book

# Silly idea: store 2D points as complex numbers
# Pypy3 Thinkpad benchmark- points as tuples: 27s, points as complex: 16s

def dist(p0, p1):
    return abs(p0 - p1)

# partition points into left and right parts in linear time
def left_half(Px, Py, L):
    return ([p for p in Px if p.real < L],
            [p for p in Py if p.real < L])

def right_half(Px, Py, L):
    return ([p for p in Px if p.real >= L],
            [p for p in Py if p.real >= L])


# Main divide-and-conquer algorithm
# requires Px, Py: points sorted by x and y
def closest_pair(Px, Py):
    n = len(Px)
    if n < 2: return float("inf")
    if n == 2: return dist(Px[0], Px[1])

    L =  Px[n//2].real  # midway line

    D = min(closest_pair(*left_half(Px, Py, L)),
            closest_pair(*right_half(Px, Py, L)))

    Sy = [p for p in Py if abs(p.real - L) < D]

    # magic strip
    for i in range(len(Sy)):
        for j in range(1, min(16, len(Sy)-i)):
            D = min(dist(Sy[i], Sy[i+j]), D)

    return D

def d(k):
    # RNG ensures no pair of points have same x or y coord
    # (unless points repeat)
    s = [290797]
    P = []
    for n in range(2*k):
        s.append(s[-1]**2 % 50515093)
        if n % 2 == 0:
            P.append(s[-2] + s[-1]*1j)


    Px = sorted(P, key=lambda p:p.real)
    Py = sorted(P, key=lambda p:p.imag)

    return closest_pair(Px, Py)

print(round(d(2000000),9))