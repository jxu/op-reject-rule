d = {}
for i in range(10000):
    c_digits = ''.join(sorted(str(i**3)))
    if c_digits in d:
        d[c_digits] += [i**3]
        if len(d[c_digits]) == 5:
            print(sorted(d[c_digits])[0])
            break
    else:
        d[c_digits] = [i**3]