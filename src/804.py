from decimal import Decimal, getcontext, ROUND_DOWN

getcontext().prec = 50

def round_down(x):  # round to zero
    return x.to_integral_value(rounding=ROUND_DOWN)

def T(N):
    N = Decimal(N)
    y_max = round_down((4*N / 163).sqrt())
    s = -1  # exclude (0,0)

    y = -y_max
    while y <= y_max:
        disc = 4*N - 163*y**2
        sqrt_disc = disc.sqrt()
        #err = sqrt_disc**2 - disc
        #print(err)
        x_min = round_down((- sqrt_disc - y) / 2)
        x_max = round_down((sqrt_disc - y) / 2)
        #print(y, x_min, x_max)
        s += x_max - x_min + 1
        y += 1

    return s

print(T(10**16))