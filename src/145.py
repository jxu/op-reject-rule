# Empirical solution (brute-force small cases)
# (digit: count) 1: 0, 2: 20, 3: 100, 4:600, 5: 0, 6: 1800, 7: 50,000
# Guess: 8 digits = 540000 (1800*30), 9 digits = 0
def rev(d):
    count = 0
    for n in range(10**(d-1), 10**d):
        if n % 10:
            s = str(n + int(str(n)[::-1]))
            if all(int(c)%2 for c in s):
                count += 1
    return count

for d in range(1, 8):
    print(d, rev(d))

print(0 + 20 + 100 + 600 + 0 + 18000 + 50000 + 540000 + 0)
