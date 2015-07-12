with open("p059_cipher.txt") as f:
    t = list(map(int, f.read().split(',')))

for x in range(97, 123):
    for y in range(97, 123):
        for z in range(97, 123):
            p = ""
            for i in range(len(t)):
                p += chr((t[i]^x, t[i]^y, t[i]^z)[i%3])

            if "the" in p and "that" in p and "is" in p:
                print(p)
                print(sum(ord(c) for c in p))
