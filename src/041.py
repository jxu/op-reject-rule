import itertools, number
l = 0
for i in range(7, 1, -1):  # 9 and 8 digit can't be prime
    for perm in itertools.permutations(range(1, i+1), i):
        n = int(''.join(map(str, perm)))
        if number.is_prime(n):
            l = max(l, n)

print(l)