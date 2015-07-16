from math import log

with open("p099_base_exp.txt") as f:
    pairs = f.read().split('\n')

sums = []
for i in range(len(pairs)):
    m, n = map(int, pairs[i].split(','))
    sums.append(n*log(m))

print(sums.index(max(sums)) + 1)
