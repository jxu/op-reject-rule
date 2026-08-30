# Newton's Method with simple derivative
# Can also use root-finding algorithm, but finnicky with precision and start

s = lambda r: sum((900-3*k) * (r**(k-1)) for k in range(1, 5001)) + 6e11

ds = lambda r: sum((900-3*k) * (k-1) * r**(k-2) for k in range(1, 5001))

eps = 1e-13
x = 1.1
for i in range(1000):
    step = s(x) / ds(x)
    print(f"iter={i} x={x} step={step} s(x)={s(x)}")
    if abs(step) < eps:
        break
    x -= step

print(round(x, 12))
