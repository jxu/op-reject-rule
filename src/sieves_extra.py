# The following were intended to test pypy https://stackoverflow.com/q/44811418

def sieve(n):
    """Sieve of Eratosthenes. Returns a list. About O(n)"""
    count = 0
    nums = [0] * n
    for i in range(2, int(n**0.5)+1):
        if nums[i] == 0:
            for j in range(i*i, n, i):
                count += 1
                nums[j] = 1

    print(count)
    return [i for i in range(2, n) if nums[i] == 0]


def sieve_var(n):
    """Sieve of Eratosthenes. Returns a list. About O(n)"""
    count = 0
    nums = [0] * n
    for i in range(3, int(n**0.5)+1, 2):
        if nums[i] == 0:
            for j in range(i*i, n, i):
                count += 1
                nums[j] = 1

    print(count)
    return [2] + [i for i in range(3, n, 2) if nums[i] == 0]


def sieve_new(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]



if __name__ == "__main__":
    from time import clock
    s = clock()
    z = sieve(10**8)
    r = sieve_var(10**8)
    print(r == z)
    print(len(r))
    print(r[:20])
    print(clock()-s)