from number import sieve
p_10000 = sieve(10000)
sp = set(sieve(10**8))

print("Primes up to 10^8 found")

def conc(a, b):
    return int(str(a) + str(b)) in sp and int(str(b) + str(a)) in sp

for a in range(len(p_10000)):
    ap = p_10000[a]

    for b in range(a):
        bp = p_10000[b]
        if not conc(ap, bp):
            continue

        for c in range(b):
            cp = p_10000[c]
            if not (conc(cp, bp) and conc(cp, ap)):
                continue

            for d in range(c):
                dp = p_10000[d]
                if not (conc(dp, cp) and conc(dp, bp) and conc(dp, ap)):
                    continue

                for e in range(d):
                    ep = p_10000[e]
                    if not (conc(ep, dp) and conc(ep, cp) and conc(ep, bp) and conc(ep, ap)):
                        continue

                    print(ap, bp, cp, dp, ep)
                    print(ap + bp + cp + dp + ep)
