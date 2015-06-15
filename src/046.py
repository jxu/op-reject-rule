import number
sp = set(number.sieve(10000))
for i in range(3, 10000, 2):
    if i not in sp:
        writable = False
        for a in range(1, int((i/2)**0.5)+1):
            if i - 2*a*a in sp:
                writable = True
                break
        if not writable:
            print(i)
            break
