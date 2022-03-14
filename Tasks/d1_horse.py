from functools import lru_cache


def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """

    rows = shape[0]
    cols = shape[1]

    @lru_cache  # только после этого становиться динамическим программированием
    def count_path(i, j):
        """Рекурсивная функция, возвращает количество шагов от i, j ячейки"""
        if i == 0 and j == 0:  # просто поставили в ячейку
            return 1

        if not 0 <= i < rows:  # Если индекс не находится от нуля, до количества строк
            return 0

        # Делают сами
        if not 0 <= j < cols:
            return 0

        # Количество ходов в i, j  равно сумме ходов в ячейках, откуда мог придти конь
        return sum([
            count_path(i - 2, j - 1),
            count_path(i - 2, j + 1),
            count_path(i - 1, j - 2),
            count_path(i + 1, j - 2)
        ])

    return count_path(point[0], point[1])

if __name__ == '__main__':
    assert 13309 == calculate_paths((7, 15), (6, 14))
    assert 2 == calculate_paths((4, 4), (3, 3))
