# Uses method that ABC@Home uses according to https://arxiv.org/abs/1409.2974
# Link contains lots of good information about abc triples!
# Rename (a, b, c) as (x, y, z) such that rad(x) < rad(y) < rad(z)
# rad(x)*rad(y)*rad(z) = rad(a)*rad(b)*rad(c) < c < 120000
# Thus rad(x) < rad(y) < sqrt(120000), and rad(x) < 120000 / rad(y)^2
# This reduces search space to < 500000
# To improve efficiency: iterate over values of rad(x) and rad(y)

from __future__ import division
from number import sieve
from fractions import gcd

C_MAX = 120000
primes = sieve(C_MAX)

def rad(n):
    r = 1
    for p in primes:
        if p * p > n: break
        if n % p == 0:
            r *= p
            while n % p == 0:
                n //= p

    if n > 1: r *= n
    return r

small_rads = []
small_nums = []
for n in range(1, C_MAX):
    if rad(n) < C_MAX**0.5:
        small_rads.append(rad(n))
        small_nums.append(n)

s = 0
sum_c = 0
for xi in range(len(small_nums)):
    x, rad_x = small_nums[xi], small_rads[xi]

    for yi in range(len(small_nums)):
        y, rad_y = small_nums[yi], small_rads[yi]

        if rad_x < rad_y and rad_x < C_MAX / (rad_y**2):
            if gcd(x, y) == 1:
                for z in (x+y, abs(x-y)):  # Possible z from a+b=c
                    c = max(x, y, z)
                    if c < C_MAX and rad_y < rad(z) < c / (rad_x*rad_y):
                        print(x, y, z)
                        sum_c += c
                        s += 1

print(s, sum_c)
