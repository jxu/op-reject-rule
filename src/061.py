# DFS
from __future__ import division

fn = [[n*(n+1)//2 for n in range(200)],
      [n**2 for n in range(200)],
      [n*(3*n-1)//2 for n in range(200)],
      [n*(2*n-1) for n in range(200)],
      [n*(5*n-3)//2 for n in range(200)],
      [n*(3*n-2) for n in range(200)]]

def cyclic(s, seen):
    if all(seen) and s[-1]%100 == s[0]//100:
        print(s)
        print(sum(s))
        return

    for i in range(len(seen)):
        if not seen[i]:
            new_seen = seen[:]
            new_seen[i] = True
            for f in fn[i]:
                # Last two digits match first two of next
                if len(str(f)) == 4 and s[-1]%100 == f//100:
                    cyclic(s + [f], new_seen)



for t in fn[0]:
    if len(str(t)) == 4:
        cyclic([t], [True, False, False, False, False, False])
