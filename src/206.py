for n in range(10**9, int(1929394959697989990**0.5), 10):
    if str(n**2)[::2] == "1234567890":
        print(n)
        break
