from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    min_index = 0
    max_index = len(arr) - 1

    while max_index >= min_index:
        middle_index = (max_index + min_index) // 2
        value = arr[middle_index]
        if value == elem:
            return middle_index
        elif value > elem:
            max_index = middle_index - 1
        elif value < elem:
            min_index = middle_index + 1

    print(elem, arr)
    return None

