"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    min_index = 0
    min_ = arr[min_index] # O(1)
    for i, num in enumerate(arr): # O (n)
        if num < min_:
            min_ = num
            min_index = i
    print(arr)
    return min_index
