import number
sp = set(number.sieve(10000))
for i in range(1000, 10000):
    if i in sp and i != 1487:
        for d in range(2, 5000):
            if i+d in sp and i+2*d in sp and set(str(i)) == set(str(i+d)) == set(str(i+2*d)):
                print(str(i) + str(i+d) + str(i+2*d))
