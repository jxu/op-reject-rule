"""Polynomials with at Least One Integer Root

Surprisingly tough. 
My initial idea was generating functions given the constraints on digits a_i. 
Given a fixed root -9 <= x <= 0, a zero sum is the constant term of a 
generating function:
product_{i=0}^{15} (z^(0x^i) + z^(1x^i) + ... + z^(9*x^i))
= product_{i=0}^{15} (1 - z^(10*x^i)) / (1 - z^(x^i))

This counts solutions for an individual x correctly, but there is no good
way to handle multiple x without ugly inclusion-exclusion. The polynomials
also get too large.

After abandoning that approach, I noticed the polynomial can be written as
a recursion using Horner's method:
a_0 + x * (a_1 + x * (a_2 + ...))
By tracking the sums digit-by-digit as y, this gives a recursion of the form
a + x*y' = y
For fun, I drew out FSMs for each digit. For example, x = -4 can be written
completely in terms of transitions y -> y' labeled by a:
0 --0--> 0
0 --4--> 1
0 --8--> 2
1 --1--> 0
...
This is neat conceptually, but not as natural to code as just representing
a DP for each x in terms of y and length l. This seems much easier, but the
problem remains of how to handle solutions with multiple satisfying x.
Conceptually, I thought of somehow running the FSMs simultaneously by
combining them into a product FSM. This led to my DP, which tracks a vector
Y containing the state for each x. If the digit a is invalid, y becomes a
special dead state.
Surprisingly, this worked immediately: the state space of Y has only 17415
states, with special handling for the constant term at x = 0.
"""

from functools import cache

@cache
def f(Y, l):
    if l == 0:
        return int(any(y == 0 for y in Y))

    s = 0
    for a in range(10):
        newY = list(Y)
        for i in range(10):
            x = i - 9
            y = Y[i]
            if y is None: 
                continue  # leave as is

            if x == 0:
                # special case for constant term
                newY[i] = a if l == 1 else 0
            elif (y - a) % x == 0:
                newY[i] = (y - a) // x
            else: 
                newY[i] = None  # special invalid value

        s += f(tuple(newY), l-1)

    return s 


print(f((0,)*10, 16))
