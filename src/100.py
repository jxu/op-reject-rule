# For b/t, 2b(b-1) = t(t-1)
# = (2t-1)^2 - 2(2b-1)^2 = a^2 - 2b^2 = -1
# Pell's equation related, recurrence formula for odd powers of fundamental solution

a, b = 1, 1
t = 1
while t < 10**12:
    a, b = 3*a + 4*b, 2*a + 3*b
    t = (a+1)//2

print((b+1)//2)  # Blue discs
