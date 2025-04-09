from number import sieve

primes = sieve(1000)
MAXP = 14

def U(N):
    s = 0
    M = 1
    L = [0]
    for i in range(0, MAXP):
        p = primes[i]
        newL = []
        newM = M * p
        #print("pM", p, M)
        for j in range(p):
            for r in L:
                t = j * M + r
                if ((t % p) % 7 == 0):
                    #print(t, "mod", newM, "list")
                    newL.append(t)
                else:
                    #print(t, "mod", newM, "add")
                    c = ((N) // newM + (((N) % newM) >= t))
                    #print("count", c)
                    s += p * c
        L = newL 
        M = newM

        print(len(L), "rems mod", M)

    print("leftover about", len(L) * (N // M))
    # handle remaining cases manually
    for j in range(N // M + 1):
        for r in L:
            t = j * M + r 

            if t == 0 or t > N:
                continue

            found = False
            # no need to factor
            for p in primes[MAXP:]:
                if (t % p) % 7 > 0:
                    #print(t, p)
                    s += p
                    found = True
                    break

            assert(found)

    
    return s 

#print(U(1470))
print(U(10**17))               
