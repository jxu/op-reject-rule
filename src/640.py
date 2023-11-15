# Similar to Problem 863: iterate expected values to fixed point
# Let e[i] be the expected turns to win for every state of cards i
# (represented as a 12-bit bitstring)
# e[i] is averaged over possible rolls, use the state from
# (flip x, flip y, flip x+y) with the smallest expected value
# e[i] = (1/36) sum_{1<=x,y<=6} (1 + min(e[ix],e[iy],e[ixy]))

e = [0] * (2 ** 12)

for t in range(500):
    for i in range(1, 2 ** 12):
        e[i] = 0
        for x in range(1, 7):
            for y in range(1, 7):
                ix = i ^ (1 << (x-1))
                iy = i ^ (1 << (y-1))
                ixy = i ^ (1 << (x+y-1))
                e[i] += (1 + min(e[ix], e[iy], e[ixy])) / 36

    print(round(e[-1], 6))
