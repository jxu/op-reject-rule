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
# So we maintain a list of residue classes that are yet unknown u(n)
# for each prime, the list is extended and modulus is multiplied by p
# then go through all the residues and check if they are 0, 7, 14, ... mod p
# if they are, they go in the list. otherwise, u(n) = p, and we add to total
# p times (how many in the res class occur <= N)
# 
# After up to a max prime, for the leftover residues we compute u(n) manually
# Previously, the max prime is chosen so that the res list fits into memory 
# while not having too many total n leftover to check. But it's simpler just
# to extend M until > N and stop computing any bigger residues.

from number import sieve

primes = sieve(100)  # suffices
MAXP = 15  # adjust to consider as large res list as fits in memory

def U(N):
    s = 0
    M = 1
    res = [0]
    for p in primes[:MAXP]:
        newres = []
        newM = M * p
        for j in range(p):
            for r in res:
                n = j * M + r
                if n > N:  # res in increasing order
                    break
                if (n % p) % 7 == 0:
                    newres.append(n)
                else:
                    c = N // newM + (N % newM >= n)
                    s += p * c
        
        res = newres
        M = newM
        print(len(res), "rems mod", M)

    # handle remaining cases individually
    for n in res:
        if n == 0: continue
        # no need to factor, just try primes
        for p in primes[MAXP:]:
            if (n % p) % 7 > 0:
                s += p
                break
    
    return s

#print(U(1470))
print(U(10**17))
