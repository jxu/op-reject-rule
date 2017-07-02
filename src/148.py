# Related A006047, extended to base 7
# Lucas's Theorem tells us that (n choose m) isn't div by 7 iff all digits of m
# in base 7 are <= corresponding digits of n in base 7.
# If n in base 7 has b1 1's, b2 2's, ..., b6 6's, the row count (not div 7)
# = 7^b6 * 6^b5 * ... * 2^b1

# To calc the total sum we consider all base 7 numbers below the # rows.
# Ex. 100-1 -> 99 = 201 base 7.
# Working digit by digit, if first digit is 0xx or 1xx then the rest can be
# freely assigned. If first digit is 2, then the next digits are bounded by 01.
# Recurse.
from number import int_to_base

# For drawing Sierpinski's Triangle
def factors_7(n):
    x = 7
    f = 0
    while x <= n:
        f += n // x
        x *= 7
    return f


def draw():
    for r in range(0, 200):
        s = 0
        j = ['.'] * (r+1)
        for n in range(r+1):
            if factors_7(r) - (factors_7(n) + factors_7(r-n)) >= 1:
                j[n] = 'X'
                s += 1

        print(str(r).ljust(4),
              str(r+1-s).ljust(4), "".join(j))


# Actual code starts here
def assign_digits(n, free_assign):
    if len(n) == 0:
        return 1

    total_count = 0
    if free_assign:
        total_count += (1+2+3+4+5+6+7)*assign_digits(n[1:], True)

    else:
        for d in range(n[0]):
            total_count += (d+1)*assign_digits(n[1:], True)

        total_count += (n[0]+1)*assign_digits(n[1:], False)

    return total_count


def f(n):
    return assign_digits(int_to_base(n-1, 7), False)

draw()
print(f(10**9))
