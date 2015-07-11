# Subset sum problem variation (taken in pairs)
import math, time, number

def g(n):
    pi = math.pi
    k_max = int(n * math.log(pi))  # All other f(k) = 0
    fxn = [math.e**(x/n)-1 for x in range(k_max)]

    half = [fxn[a] + fxn[b] for a in range(k_max) for b in range(a, k_max)]

    half.sort()
    # Pair sum must have 1 value in lo and 1 value in hi
    lo, hi = half[:len(half)//2], half[len(half)//2:]

    threshold = 0.00001
    best_h = best_c = None
    for h in lo:
        c = number.take_closest(hi, pi-h)
        if abs(h + c - pi) < threshold:
            threshold = abs(h + c - pi)
            best_h = h
            best_c = c
            print(h, c, threshold)

    # Memory hack (for 32-bit python, search for a, b, c, d from half)
    g = 0
    for a in range(k_max):
        for b in range(a, k_max):
            if fxn[a] + fxn[b] == best_h or fxn[a] + fxn[b] == best_c:
                print(a, b, end=' ')
                g += a*a + b*b  # Add either half

    return g


start = time.process_time()
print(g(10000))
print(time.process_time()-start, "s")
