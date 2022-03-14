from random import randint
from typing import List

from Tasks.utils import benchmark


@benchmark(10)
def sort(container: List[int]) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """

    n = len(container)
    # 4.16912849 секунд для [randint(-10000, 10000) for _ in range(10000)]
    # for i in range(n - 1):
    #     for j in range(0, n - i - 1):
    #         if container[j] > container[j + 1]:
    #             container[j], container[j + 1] = container[j + 1], container[j]

    # 7.85179351 секунд для [randint(-10000, 10000) for _ in range(10000)]
    for _ in range(len(container)):
        for i in range(len(container) - 1):
            if container[i] > container[i + 1]:
                container[i], container[i + 1] = container[i + 1], container[i]
    return container

# arr = [randint(-10000, 10000) for _ in range(10000)]
# sort(arr)
