from random import randint
from time import perf_counter
from typing import List

from Tasks.utils import benchmark


# @benchmark(10)
def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """

    if len(container) > 1:

        # Ищем середину
        mid = len(container) // 2

        # Делим массив
        L = container[:mid]

        # на две части
        R = container[mid:]

        # Сортируем левую часть
        sort(L)

        # Сортируем правую часть
        sort(R)

        i = j = k = 0

        # Копируем данные из временных массивов
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                container[k] = L[i]
                i += 1
            else:
                container[k] = R[j]
                j += 1
            k += 1

        # Проверяем где должен находится элемент
        # из левой части
        while i < len(L):
            container[k] = L[i]
            i += 1
            k += 1

        # из правой
        while j < len(R):
            container[k] = R[j]
            j += 1
            k += 1

    return container

arr = [randint(-10000, 10000) for _ in range(10000)]

start = perf_counter()
sort(arr)
print(perf_counter() - start)