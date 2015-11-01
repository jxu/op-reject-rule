# Commonly used number-related functions
import math

prime_100 = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)

def sieve(n):
    """Sieve of Eratosthenes. Returns a list. About O(n)"""
    nums = [0] * n
    for i in range(2, int(n**0.5)+1):
        if nums[i] == 0:
            for j in range(i*i, n, i):
                nums[j] = 1

    return [i for i in range(2, n) if nums[i] == 0]


def sieve_set(n):
    """Returns a set of sieve(n)"""
    return set(sieve(n))


def is_prime(n):
    """Returns whether a number is prime or not"""
    if n < 2: return False
    return all(n%i for i in range(2, int(n**0.5)+1))


def is_square(n):
    """Returns if a number is square without floating point math. Credit: Alex Martelli"""
    x = n // 2
    seen = set([x])
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in seen: return False
        seen.add(x)
    return True


def prime_factors(n):
    factors = []
    m = n
    prime = False
    prime_20 = (2, 3, 5, 7, 11, 13, 17, 19)
    while not prime:
        prime = True
        r = prime_100 + tuple(range(101, int(m**0.5)+1, 2))
        for i in r:
            if m%i == 0:
                m //= i
                factors.append(i)
                prime = False
                break

    if m != 1: factors += [m]
    return factors


def combination(n, k):
    f = math.factorial
    return f(n) // f(k) // f(n-k)


def permutation(n, k):
    f = math.factorial
    return f(n) // f(n-k)


def take_closest(l, n, bisect=True):
    """If bisect (binary search): Assumes l is sorted. Returns closest value to n.
       If two numbers are equally close, return the smallest number. Credit: Lauritz V. Thaulow
       If not bisect: Use lambda and min to go through list, O(n) time."""
    if bisect:
        from bisect import bisect_left
        pos = bisect_left(l, n)
        if pos == 0:
            return l[0]
        if pos == len(l):
            return l[-1]
        before = l[pos - 1]
        after = l[pos]
        if after - n < n - before:
           return after
        else:
           return before

    else:
        return min(l, key=lambda x:abs(x-n))


def gcd(a, b):
    """Euclid's algorithm. Identical to fractions.gcd(a, b)"""
    while b:
        a, b = b, a%b
    return a


def phi(n, product_formula=True):
    """Euler's product formula or straightforward calculation of Euler's totient function."""
    if n == 0: return 0
    if product_formula:
        r = n
        spf = set(prime_factors(n))
        for p in spf:
            r *= 1 - 1/p

        return round(r)

    else:
        r = 0
        for k in range(1, n+1):
            if gcd(n, k) == 1:
                r += 1
        return r


def dijkstra(graph, start):
    """Dijkstra's algorithm using heaps.
       Test using g = {0:{1:2}, 1:{0:2, 2:6}, 2:{1:6}}  Credit: Janne Karila"""
    from heapq import heappush, heappop

    A = [None] * len(graph)
    queue = [(0, start)]
    while queue:
        path_len, v = heappop(queue)
        if A[v] is None: # v is unvisited
            A[v] = path_len
            for w, edge_len in graph[v].items():
                if A[w] is None:
                    heappush(queue, (path_len + edge_len, w))

    return A


def product(iterable):
    product = 1
    for i in iterable: product *= i  # No reduce() :(
    return product


def highly_composite():
    hc = []
    with open("highly_composite.txt", 'r') as f:
        for rows in f:
            hc.append(int(rows.split(' ')[1]))
    return hc


def mul_inv(a, b):
    """Modular multiplicative inverse, ax = 1 mod m. Credit: rosettacode.org"""
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        assert b != 0, "a and b must be coprime"
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


if __name__ == "__main__":
    #g = {0:{1:2}, 1:{0:2, 2:6}, 2:{1:6}}
    #print(dijkstra(g, 0))
    print(mul_inv(3, 9))