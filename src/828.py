from operator import add, sub, mul, floordiv as div

def partition(x, l = [], r = []):
    """Partition list x into LHS and RHS"""
    if not x: return [(l,r)]
    return partition(x[1:], [x[0],] + l, r) + \
           partition(x[1:], l, [x[0],] + r)

def f(nums):
    if len(nums) == 1: return nums[0]
    # pick disjoint subsets l, r from nums
    res = []
    for l, rest in partition(nums):
        if not l or not rest: continue
        for r, _ in partition(rest):
            if not r: continue
            print(l, r)
            for op in (add, sub, mul, div):





f([2,3,5])