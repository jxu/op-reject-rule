seq = (1, 2, 3, 4, 3, 2)
pos = 0

for i in range(1, 50):
    digit_sum = 0
    digits = 0
    while digit_sum != i:
        d = seq[pos]
        digit_sum += d
        digits = 10*digits + d

        pos = (pos+1) % len(seq)

    print(digit_sum, digits)
