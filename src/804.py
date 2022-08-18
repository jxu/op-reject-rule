def T(N):

    y_max = int((4*N / 163)**0.5)
    s = -1  # exclude (0,0)

    for y in range(-y_max, y_max+1):
        disc = 4*N - 163*y**2
        err = (disc**0.5)**2 - disc
        #print(err)
        x_min = int((- disc**0.5 - y) / 2)
        x_max = int((disc**0.5 - y) / 2)
        #print(y, x_min, x_max)
        s += x_max - x_min + 1

    return s

print(T(10**16))