# Uses python3
import sys
import functools

def memoize(obj):
    cache = obj.cache = {}

    @functools.wraps(obj)
    def memoizer(*args, **kwargs):
        if args not in cache:
            cache[args] = obj(*args, **kwargs)
        return cache[args]
    return memoizer

@memoize
def multiply_by_3(x):
    return x * 3

@memoize
def multiply_by_2(x):
    return x * 2

@memoize
def add_one(x):
    return x * 1

def optimal_sequence(n):
    if n == 1:
        return [1]

# input = sys.stdin.read()
# n = int(input)
# sequence = list(optimal_sequence(n))
# print(len(sequence) - 1)
# for x in sequence:
#     print(x, end=' ')
