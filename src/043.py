import itertools
div = (2, 3, 5, 7, 11, 13, 17)
s = 0
for perm in itertools.permutations("0123456789", 10):
    n = ''.join(perm)
    if all(int(n[i+1:i+4]) % div[i] == 0 for i in range(7)):
        s += int(n)

print(s)