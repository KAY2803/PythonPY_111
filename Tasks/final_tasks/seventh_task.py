# 7.	Сорт
# Дано: массив из 10**6 целых чисел, каждое из которых лежит на отрезке [13, 25].
# Задача: отсортировать массив наиболее эффективным способом
from collections import defaultdict
from random import randint


def counting_sort(arr: list, min_num=13, max_num=25):
    count = defaultdict(int)
    for i in arr:
        count[i] += 1

    result = []
    for j in range(min_num, max_num + 1):
        result.append([j] * count[j])

    return result


if __name__ == '__main__':
    arr = [randint(13, 25) for _ in range(1000)]
    print(counting_sort(arr))