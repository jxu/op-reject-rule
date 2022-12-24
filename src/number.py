"""Commonly used helper functions"""
import operator
from ntheory import *

def is_close(a, b, tol=1e-9):
    return abs(a-b) <= tol


def is_int(n):
    return is_close(n, round(n))


def combination(n, k):
    return product(range(n-k+1, n+1)) // product(range(1, k+1))


def permutation(n, k):
    return product(range(n-k+1, n+1))


def take_closest(l, n):
    """If bisect (binary search): Assumes l is sorted.
    Returns closest value to n.
    If two numbers are equally close, return the smallest number.
    Credit: Lauritz V. Thaulow
    If not bisect: Use lambda and min to go through list, O(n) time.
    """
    from bisect import bisect_left
    pos = bisect_left(l, n)
    if pos == 0:
        return l[0]
    if pos == len(l):
        return l[-1]
    before = l[pos - 1]
    after = l[pos]
    if after - n < n - before:
       return after
    else:
       return before


def dijkstra(graph, start):
    """Dijkstra's algorithm using heaps.
    Test using g = {0:{1:2}, 1:{0:2, 2:6}, 2:{1:6}}  Credit: Janne Karila"""
    from heapq import heappush, heappop

    A = [None] * len(graph)
    queue = [(0, start)]
    while queue:
        path_len, v = heappop(queue)
        if A[v] is None: # v is unvisited
            A[v] = path_len
            for w, edge_len in graph[v].items():
                if A[w] is None:
                    heappush(queue, (path_len + edge_len, w))

    return A


def product(iterable):
    product = 1
    for i in iterable: product *= i  # No reduce() :(
    return product


def accumulate(iterable, func=operator.add):
    '''Return running totals, like itertools.accumulate'''
    it = iter(iterable)
    try:
        total = next(it)
    except StopIteration:
        return
    yield total
    for element in it:
        total = func(total, element)
        yield total


def powerset(iterable):
    """From itertools recipes
    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    """
    from itertools import chain, combinations
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def custom_powerset(s, min_size, max_size):
    from itertools import chain, combinations
    return chain.from_iterable(
        combinations(s, r) for r in range(min_size, max_size+1))


def memoize(obj):
    """Decorator that memoizes a function's calls. Credit: Python wiki"""
    # ignores **kwargs
    from functools import wraps
    cache = obj.cache = {}

    @wraps(obj)
    def memoizer(*args, **kwargs):
        if args not in cache:
            cache[args] = obj(*args, **kwargs)
        return cache[args]

    return memoizer


def timeit(f):
    """Timing decorator for functions. Example usage: sieve = timeit(sieve)"""
    from time import clock
    def timed(*args, **kwargs):
        time_start = clock()
        result = f(*args, **kwargs)
        time_end = clock()

        all_args = list(map(str, args))
        for key in kwargs:
            all_args.append("{}={}".format(key, kwargs[key]))

        print("{}({})   took {:2.4f}s".format(f.__name__, ', '.join(all_args),
                                              time_end - time_start))
        return result

    return timed


def unique_permutations(elements):
    """Like itertools.permutations but without duplicates. Credit: Luka Rahne"""

    class unique_element:
        def __init__(self, value, occurrences):
            self.value = value
            self.occurrences = occurrences

    eset=set(elements)
    listunique = [unique_element(i,elements.count(i)) for i in eset]
    u=len(elements)
    return perm_unique_helper(listunique,[0]*u,u-1)


def perm_unique_helper(listunique,result_list,d):
    if d < 0:
        yield tuple(result_list)
    else:
        for i in listunique:
            if i.occurrences > 0:
                result_list[d]=i.value
                i.occurrences-=1
                for g in  perm_unique_helper(listunique,result_list,d-1):
                    yield g
                i.occurrences+=1


def combo_max_product(X, terms, max_product):
    '''Like itertools.combinations(X, terms) but only picks values whose
    product is <= max_product.
    '''
    assert sorted(X) == X  # To keep track of index
    result = []

    def f(last_i, terms_so_far, product_):
        if len(terms_so_far) == terms:
            result.append(terms_so_far)
            return

        for i in range(last_i, len(X)):
            new_product = product_ * X[i]
            if new_product <= max_product:
                f(i+1, terms_so_far + [X[i]], new_product)
            else:  # Product too large already
                break

    f(0, [], 1)
    return result


if __name__ == "__main__":
    pass
