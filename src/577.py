# We're back, baby!
# For n, hexagons of size 1: sum from 1 to n-2, inclusive (triangular numbers)
# For hexagons size x: x-1 inscribed hexagons for a total of x hexagons
# H(n) = (n-2)(n-1)/2 + 2*(n-5)(n-4)/2 + 3*(n-8)(n-7)/2 + ...
# Also A011779

def H(n):
    result = 0
    m = n-2
    hexagons = 1
    while m >= 1:
        result += hexagons * m*(m+1)//2
        hexagons += 1
        m -= 3

    return result

print(sum(H(n) for n in range(3, 12346)))
