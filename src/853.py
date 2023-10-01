from number import fib_list, divisors, factor

F = fib_list(121)

def f(pi_n, limit):
    s = 0
    for n in sorted(divisors(factor(F[pi_n]))):
        if n >= limit: break
        if F[pi_n+1] % n != 1: continue
        if all((F[m]%n, F[m+1]%n) != (0,1) for m in range(1, pi_n)):
            print(n)
            s += n
    return s


print(f(120, 10**9))