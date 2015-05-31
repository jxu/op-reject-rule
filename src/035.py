def get_rotations(n): # Including original n
    l = []
    for i in range(len(str(n))):
        l.append(int(str(n)[i:] + str(n)[:i]))
    return l


def sieve(n):
    nums = [0] * n
    for i in range(2, int(n**0.5)+1):
        if nums[i] == 0:
            for j in range(2*i, n, i):
                nums[j] = 1

    return nums


mil_primes = sieve(10**6)
s = 0

for i in range(2, 10**6):
    if mil_primes[i] == 0:
        if all(mil_primes[j] == 0 for j in get_rotations(i)):
            s += 1

print(s)
