# Pell's equations
# x^2 - 3y^2 = 1; n=3
x = 2
y = 1
P_MAX = 1000000000
p_sum = 0

while True:
    # a, a, a+1
    a3 = 2*x - 1
    A3 = y * (x-2)
    if a3 > P_MAX: break

    if A3 > 0 and a3 % 3 == 0 and A3 % 3 == 0:
        p_sum += a3 + 1
        
    # a, a, a-1
    a3 = 2*x + 1
    A3 = y * (x+2)
    
    if A3 > 0 and a3 % 3 == 0 and A3 % 3 == 0:
        p_sum += a3 - 1
        
    x, y = 2*x + 3*y, 2*y + x  # Recurrence relation
    
print(p_sum)
