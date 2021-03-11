"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, 
значения которых больше предыдущего элемента.

Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. 
Для формирования списка использовать генератор.

Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""

from sys import argv
from random import randrange
from functools import reduce


def generate_gen(count: int) -> list:
    """Генерируем набор значений заданного количества"""
    if int(count) <= 0:
        raise ValueError(
            'Количество элементов должно быть целочисленным положительным')
    for _ in range(int(count)):
        yield randrange(1, 999)


def search_elements(count: int):
    """Собираем элементы исходного списка, значения которых 
    больше предыдущего элемента"""
    task_list = list(generate_gen(count))
    result_list = []
    for idx, el in enumerate(task_list[1:], start=1):
        if el > task_list[idx - 1]:
            result_list.append(el)
    return task_list, result_list


if __name__ == '__main__':
    try:
        _, count, *args = argv
        source_list, result_list = search_elements(count)
        print('{:<20}: {}'.format('Исходный список', source_list))
        print('{:<20}: {}'.format('Результат', result_list))

    except Exception as err:
        print(f"Ошибка: {err}")


"""
Результат выполнения:

> python task_2.py
Ошибка: not enough values to unpack (expected at least 2, got 1)
> python task_2.py -2
Ошибка: Количество элементов должно быть целочисленным положительным
> python task_2.py 10
Исходный список     : [873, 298, 566, 465, 915, 233, 622, 858, 725, 231]
Результат           : [566, 915, 622, 858]
"""
