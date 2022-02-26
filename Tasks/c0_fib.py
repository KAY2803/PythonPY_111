from typing import Iterator
from functools import lru_cache


@lru_cache(maxsize=None)
def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError

    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError

    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def fib_generator(n: int) -> Iterator:
    a, b = 0, 1
    return (a + b for _ in range(n) if n > 0)
