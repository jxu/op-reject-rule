# simple DP and multinomial coefficient, with 1/10 strings having leading zero

from math import prod

FACT = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800,
        479001600, 6227020800, 87178291200, 1307674368000, 20922789888000,
        355687428096000, 6402373705728000)


def dp(rem, max_d=9):
    if rem == 0:
        yield [0]*10
        return
    for d in range(max_d+1):
        for hist in dp(rem-1, d):
            hist[d] += 1
            if hist[d] <= 3:
                yield hist


print(sum(FACT[18] // prod(FACT[hist[d]] for d in range(10))
          for hist in dp(18)) * 9 // 10)