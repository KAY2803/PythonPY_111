def factorial_recursive(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in recursive way
    :param n: int > 0
    :return: factorial of n
    """
    if n < 0:
        raise ValueError
    if n in (0, 1):
        return 1
    else:
        return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in iterative way

    :param n: int > 0
    :return: factorial of n
    """
    if n < 0:
        raise ValueError
    if n in (0, 1):
        return 1
    else:
        f = 1
        for i in range(1, n+1):
            f *= i
    return f

    # Вариант 2
    # res = 1
    # while n > 1:
    #     res *= n
    #     n -= 1
    # return res

def factorial_generator(n: int):
    if n < 0:
        raise ValueError
    if n in (0, 1):
        yield 1
    else:
        f = 1
        for i in range(1, n + 1):
            f *= i
            yield f

