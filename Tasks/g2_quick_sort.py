from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param end:
    :param start:
    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """

    if len(container) > 1:
        pivot = container[len(container) // 2]
        less = []
        greater = []
        equal = []
        for i in container:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                greater.append(i)
            else:
                equal.append(i)
        return sort(less) + equal + sort(greater)
    else:
        return container