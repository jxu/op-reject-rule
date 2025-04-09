# Idea: consider cases of primes in increasing order
# if n != 0 mod 2: u(n) = 2
# else: (n = 0 mod 2)
#   if n != 0 mod 3: u(n) = 3
#   else: (n = 0 mod 3, => n = 0 mod 6)
#     if n != 0 mod 5: u(n) = 5
#     else: (n = 0 mod 5, => n = 0 mod 30)
#       if n != 0 mod 7: u(n) = 7
#       else: (n = 0 mod 7, => n = 0 mod 210)
#         if n != 0,7 mod 11: u(n) = 11
#         else: (n = 0,7 mod 11 => n = 0,7*210 mod 11*210)
#         etc.
#
# So we maintain a list of residue classes mod M that are yet unknown u(n)
# for each prime, the list is from mod M to mod p*M
# then go through all the residues and check if they are 0, 7, 14, ... mod p
# if they are, they go in the list. otherwise, u(n) = p, and we add to total
# p times (how many in the res class occur <= N)
# 
# After up to a max prime, for the leftover residues we compute u(n) manually
# Previously, the max prime is chosen so that the res list fits into memory 
# while not having too many total n leftover to check. But it's simpler just
# to extend M until > N and stop computing any bigger residues.

from number import sieve

primes = sieve(100)  # actually suffices

def U(N):
    s = 0
    M = 1
    res = [0]
    for p in primes:
        newres = []
        for j in range(p):
            for r in res:
                n = j * M + r
                if n > N:  # res in increasing order
                    break
                if (n % p) % 7 == 0:
                    newres.append(n)
                else:
                    c = N // (M*p) + (N % (M*p) >= n)  # res count <= N
                    s += p * c
        
        res = newres
        M *= p
        print(len(res), "rems mod", M)

        if M > N:
            break

    # handle remaining cases individually, skipping 0
    for n in res[1:]:
        # no need to factor, just try primes
        for p in primes[15:]:
            if (n % p) % 7 > 0:
                s += p
                break
    
    return s

#print(U(1470))
print(U(10**17))
