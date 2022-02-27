from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """

    def fun_binary(left_part, right_part):
        middle_index = (left_part + right_part) // 2
        middle_value = arr[middle_index]
        if left_part == right_part and middle_value != elem:
             return None

        if middle_value == elem:
            return middle_index

        elif middle_value < elem:
            new_left_part = middle_index + 1
            return fun_binary(new_left_part, right_part)

        else:
            new_right_part = middle_index - 1
            if new_right_part < 0:
                return None
            return fun_binary(left_part, new_right_part)

    left_part = 0
    right_part = len(arr) - 1
    return fun_binary(left_part, right_part)


if __name__ == '__main__':
    arr = [i for i in range(100)] + [101]
    print(arr)
    print(binary_search(100, arr))