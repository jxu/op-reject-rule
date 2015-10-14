# Continuation of #108
# For n = p1^a1 * p2^a2 * ..., obvious realization that a1 >= a2 >= ...
small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43)  # 3^14 > 4 million
pow_list = []

def gen_pow_list(l):
    if len(l) == 14:
        global pow_list
        pow_list.append(l)
    else:
        for i in range(l[-1] + 1):
            gen_pow_list(l + [i])


for i in range(1, 5):
    gen_pow_list([i])

least_n = 10**20
for l in pow_list:
    d = 1
    for a in l:
        d *= 2*a + 1
    if d > 2*4000000 - 1:
        n = 1
        for i in range(len(l)):
            n *= small_primes[i] ** l[i]
        least_n = min(least_n, n)

print(least_n)
