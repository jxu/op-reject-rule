seq = (1, 2, 3, 4, 3, 2)
pos = 0

for i in range(1, 50):
    digit_sum = 0
    digit_seq = 0
    digits = 0
    old_pos = pos

    while digit_sum != i:
        d = seq[pos]
        digit_sum += d
        digit_seq = 10*digit_seq + d

        pos = (pos+1) % len(seq)
        digits += 1

    print("{:>2}  {}{:>4}  {}".format(digit_sum, old_pos, digits, digit_seq))