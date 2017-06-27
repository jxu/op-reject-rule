# WIP Adaptation of the knapsack problem (DP)

from __future__ import division
from number import sieve, product, memoize
from math import log
from random import random, sample

primes = sieve(190)
log_primes = [log(p) for p in primes]
target = 0.5*sum(log_primes)
p_used = [False]*len(primes)

def err(l):
    r = target - sum(log_primes[i] for i in range(len(primes)) if l[i])
    return r if r > 0 else 1

def toggle(l, to_toggle):
    for t in to_toggle: l[t] = not l[t]
    return l

def P(err, new_err, tol):
    if new_err < err: return 1
    return (err - new_err) / tol

def new_tol(tol):
    if tol > 1: tol -= 0.0001
    elif tol > 0.1: tol -= 0.00001
    else: tol -= 0.00001
    return tol

final_err = 1
final_product = None
for trial in range(100):
    tol = 10
    best_err = 100
    while tol > 0:

        to_toggle = sample(range(len(primes)), 3)
        p_used = toggle(p_used, to_toggle)
        new_err = err(p_used)
        if P(best_err, new_err, tol) >= random():
            best_err = new_err

        else:  # toggle back
            p_used = toggle(p_used, to_toggle)

        #print(best_err)

        tol = new_tol(tol)
    if best_err < final_err:
        print(best_err)
        final_err = best_err
        final_product = \
            product(primes[i] for i in range(len(primes)) if p_used[i])


print(final_product)
