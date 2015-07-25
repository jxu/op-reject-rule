# TESTING

import itertools
p = itertools.product(('0', '1', '2'), repeat=15)

for d in p:
    s = int("".join(d))
    if s%999 == 0 and s>0:
        print(s, s//999)
        break

print(1111122222222222222222222 // 99999)
