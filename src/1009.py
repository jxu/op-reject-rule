from math import log

def F(a, b):
    k = int(log(4) / log(b / a))

    def f(A, j, t):
        #print(A, j, t)
        if j == -1:
            if t == 0:
                return sum(A[i] * a**i for i in range(k+1))
            else:
                return 0

        for d in range(a-1, -1, -1):
            newA = A[:]
            newA[j] = d
            if (sum((a-1)*abs(2*a**i - b**i) for i in range(j)) >=
                abs(sum(newA[i] * (2*a**i - b**i) for i in range(j, k+1)))):
                ret = f(newA, j-1, t + d * (2*a**j - b**j))
            
                if ret != 0: return ret

        return 0

    z = f([0]*(k+1), k, 0)
    #print("F", a, b, z)
    return z

def G(a):
    return sum(F(a, b) for b in range(a+1, 3*a))

assert F(3,4) == 53
assert F(3,6) == 6
assert F(3,7) == 8
print(sum(G(a) for a in range(2, 21)))
