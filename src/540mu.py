# Pengolodh idea

from number import mobius_range

def C(N):
    return sum(int((N - m**2)**0.5) // 2 
               for m in range(1, int(N**0.5)+1, 2))




def P(N): 
    mu = mobius_range(int(N**0.5))
    s = 0 
    for d in range(1, int(N**0.5)+1, 2):
        s += mu[d] * C(N / (d**2))

    return s

#print(P(10**6))
print(P(3141592653589793))
