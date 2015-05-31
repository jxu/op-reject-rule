def get_rotations(n):
    l = [n]
    for i in range(len(str(n))-1):
        n = str(n)[-1] + str(n)[:-1]
        l.append(int(n))
    return l

print(get_rotations(123))