def is_Lychrel(n):
    for i in range(50):
        n += int(str(n)[::-1])
        if str(n)[::-1] == str(n):
            return False

    return True

print(sum(is_Lychrel(n) for n in range(10000)))
