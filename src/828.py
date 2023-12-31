from operator import add, sub, mul, floordiv as div
from functools import cache

def partition(x, l = (), r = ()):
    """Partition list x into LHS and RHS"""
    if not x: yield (l,r); return
    yield from partition(x[1:], (x[0],) + l, r)
    yield from partition(x[1:], l, (x[0],) + r)


@cache
def op_tree(nums):
    if len(nums) == 1: return {nums[0]}
    res = set()
    # partition nums into non-empty l and r parts
    for l, r in partition(nums):
        if not l or not r: continue
        for lx in op_tree(l):
            for rx in op_tree(r):
                for op in (add, sub, mul, div):
                    #print(op, l, lx, r, rx)
                    if op == div:
                        if rx != 0 and lx % rx == 0:
                            res.add(op(lx, rx))
                    else:
                        res.add(op(lx, rx))

    return res

def challenge(target, available):
    best_score = float("Inf")
    for nums, _ in partition(available):
        if target in op_tree(nums):
            best_score = min(best_score, sum(nums))

    return 0 if best_score == float("Inf") else best_score

M = 1005075251
s = 0
n = 1

with open("p828_number_challenges.txt", 'r') as f:
    for line in f.readlines():
        l0, l1 = line.split(':')
        target = int(l0)
        nums = list(map(int, l1.split(',')))
        score = challenge(target, nums)
        print(target, nums, score)

        s = (s + pow(3, n, M) * score) % M
        n += 1

print(s)
