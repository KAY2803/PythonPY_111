from typing import Union, Sequence

def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """

    total_cost = {
        # ключ: номер ступени, значение: минимальная стоимость
    }  # таблица со стоимостями

    def lazy_stairway_path(stair_number):
        """Рекурсивная функция, которая возвращает стоимость до N-ступени"""

        # Первая реализация

        # if stair_number in total_cost:  # если номер ступени уже есть в кеше
        #     return total_cost[stair_number]  # возвращаем
        #
        # # если нет, то начинаем считать
        # if stair_number == 0:
        #     total_cost[stair_number] = stairway[stair_number]  # сохранил в кеш
        #     return total_cost[stair_number]  # вернул из кеша
        #
        # if stair_number == 1:
        #     total_cost[stair_number] = stairway[stair_number]  # сохранил в кеш
        #     return stairway[stair_number]  # stairway[1]
        #
        # current_cost = stairway[stair_number] + min(lazy_stairway_path(stair_number-1),
        #                                             lazy_stairway_path(stair_number-2))
        # total_cost[stair_number] = current_cost
        # return total_cost[stair_number]

        # Второй вариант

        if stair_number == 0 or stair_number == 1:
            total_cost.update({stair_number: stairway[stair_number]})
            return stairway[stair_number]
        current_price = total_cost.get(stair_number, None)

        if current_price is None:
            current_price = stairway[stair_number] + min(lazy_stairway_path(stair_number - 1),
                                                         lazy_stairway_path(stair_number - 2))
            total_cost.update({stair_number: current_price})
        return current_price

    # return direct_stairway_path(stairway)
    # return reverse_stairway_path(stairway)
    return lazy_stairway_path(len(stairway) - 1)


def reverse_stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:

    count_stairs = len(stairway)
    total_cost = [float('inf')] * count_stairs

    total_cost[0] = stairway[0]
    total_cost[1] = stairway[1]

    for i in range(0, count_stairs):
        if i + 1 < count_stairs:
            total_cost[i+1] = min(total_cost[i + 1], stairway[i + 1] + total_cost[i])

        if i + 2 < count_stairs:
            total_cost[i + 2] = min(total_cost[i + 2], stairway[i + 2] + total_cost[i])

    return total_cost[-1]


def direct_stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:

    count_stairs = len(stairway)
    total_cost = [float('inf')] * count_stairs

    total_cost[0] = stairway[0]
    total_cost[1] = stairway[1]

    for i in range(2, count_stairs):
        total_cost[i] = min(total_cost[i-1] + stairway[i], total_cost[i-2] + stairway[i])

    return total_cost[-1]

