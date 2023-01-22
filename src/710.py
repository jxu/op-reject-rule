from number import memoize

M = 1000000

@memoize
def f(rem, two_seen):

    if rem == 0:
        if two_seen: return 1
        else: return 0

    s = 0

    for i in range(1, rem+1):
        #print(rem, two_seen, i)
        if i == 2: two_seen_new = True
        else: two_seen_new = two_seen

        s = (s + (f(rem - i, two_seen_new))) % M

    return s

#print(f([], 3, False))

def t(n):

    s = 0
    if n % 2 == 0:
        for middle in range(0, n+1, 2):
            two_seen = middle == 2
            s = (s +  (f((n-middle)//2, two_seen))) % M
    else:
        for middle in range(1, n+1, 2):
            two_seen = middle == 2
            s = (s +  (f((n-middle)//2, two_seen))) % M


    return s

for n in range(42, 1000000):
    tn = t(n)
    if tn < 1000:
        print(n, tn)
    if tn % 1000000 == 0:
        print(n)
        break