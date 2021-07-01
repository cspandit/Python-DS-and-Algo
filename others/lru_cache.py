import cProfile
from functools import lru_cache
# lru_cache will minimize the repetitive recursive calls
@lru_cache
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-2) + fib(n-1)


cProfile.run('fib(10)')