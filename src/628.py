# The rook can only get to the upper right corner if it isn't blocked by a
# diagonal of pawns.
# Ex. for 3x3 board:
# ...  ...  X..  .X.  ..X
# ...  X..  .X.  ..X  ...
# X..  .X.  ..X  ...  ...
# This overcounts some cases. If i is n - (length of diagonal), then
# 0! + 1! + ... + (i-1)! cases have been overcounted.
# f(n) = n! + 1 - Sum_{i=0..n-1} (2i! - Sum_{j=0..i-1} j!)
# = n! + 1 - Sum_{i=0..n-1} (n-3-i) * i!

M = 1008691207
def f(n):
    s = 0
    fact = 1
    for i in range(n):
        s = (s + (n-3-i) * fact) % M
        fact = (fact * (i+1)) % M

    return (s + fact + 1) % M

print(f(10**8))