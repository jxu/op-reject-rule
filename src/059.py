with open("p059_cipher.txt") as f:
    t = list(map(int, f.read().split(',')))

for x in range(97, 123):
    for y in range(97, 123):
        for z in range(97, 123):
            p = t[:]
            for i in range(len(t)):
                p[i] = chr(t[i] ^ (x, y, z)[i%3])

            if " the " in ''.join(p):
                print(''.join(p))
                print(sum(map(ord, p)))
