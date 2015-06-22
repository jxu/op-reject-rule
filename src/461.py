
def g(n):
    pi = math.pi
    k_max = int(n * math.log(pi))  # All other f(k) = 0
    fxn = [math.e**(x/n)-1 for x in range(k_max)]

    half = []
    for a in range(k_max):
        for b in range(a, k_max):
            half.append(fxn[a] + fxn[b])

    half.sort()
    threshold = 0.0001
    best_h = best_c = None
    for h in half:
        c = number.take_closest(half, pi-h)
        if abs(h + c - pi) < threshold:
            threshold = abs(h + c - pi)
            best_h = h
            best_c = c
            print(h, c, threshold)

    # Memory hack (for 32 bit python, search for a and b from half)
    g = 0
    for a in range(k_max):
        for b in range(a, k_max):
            if fxn[a] + fxn[b] == best_h:
                g += a*a + b*b
                break

    for c in range(k_max):
        for d in range(c, k_max):
            if fxn[c] + fxn[d] == best_c:
                g += c*c + d*d
                break

    return g


start = time.process_time()
print(g(10000))
print(time.process_time()-start, "s")

