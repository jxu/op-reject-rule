# The following were intended to test pypy https://stackoverflow.com/q/44811418
from number import timeit
from sys import getsizeof

@timeit
def sieve(n):
    nums = [0] * n
    for i in range(2, n):
        if i * i >= n: break
        if nums[i] == 0:
            for j in range(i*i, n, i):
                nums[j] = 1

    return [i for i in range(2, n) if nums[i] == 0]

@timeit
def sieve_bool(n):
    nums = [False] * n
    for i in range(2, n):
        if i * i >= n: break
        if not nums[i]:
            for j in range(i*i, n, i):
                nums[j] = True

    return [i for i in range(2, n) if not nums[i]]


@timeit
def sieve_odd(n):
    assert n > 2
    nums = [0] * (n//2)  # use half the memory
    for i in range(3, n, 2):
        if i * i >= n: break
        if nums[i//2] == 0:
            for j in range(i*i, n, 2*i):
                nums[j//2] = 1

    return [2] + [i for i in range(3, n, 2) if nums[i//2] == 0]


@timeit
def sieve_slice(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]



if __name__ == "__main__":
    p = sieve(10**8)
    q = sieve_bool(10**8)
    assert p == q
