# A007732 By long division, the repetend period length is the
# multiplicative order of 10 mod d.
# equivalently, smallest k such that d divides 10^k - 1

max_k, max_d = 0, 0
for d in range(1000):
    if d % 2 == 0 or d % 5 == 0: continue
    for k in range(1, 1000):
        if (10 ** k - 1) % d == 0:
            if k > max_k:
                print(f"1/{d} {k}")
                max_k = k
                max_d = d
            break

print(max_d)
