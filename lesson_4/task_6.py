"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools. 
Обратите внимание, что создаваемый цикл не должен быть бесконечным. 
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, 
а при достижении числа 10 завершаем цикл. Во втором также необходимо предусмотреть 
условие, при котором повторение элементов списка будет прекращено.
"""
from itertools import count, cycle
from typing import Iterator
from argparse import ArgumentParser


parser = ArgumentParser(description="""
    Скрипт работает в двух режимах в зависимости от введенных Вами
    опциональных аргументов, подробнее смотрите описание аргументов
    """)
parser.add_argument(
    "--start",
    help="Вернёт список из 10 элементов, начиная с указанного в параметре",
    type=int)
parser.add_argument(
    "--repeat",
    help="Вернёт повторяющийся список элементов по указанному количеству",
    type=int)


def get_iterator_count(start_number: int) -> Iterator:
    """Итератор, генерирующий 10 целых чисел, начиная с указанного"""
    for el in count(start_number):
        yield el
        if el == start_number + 10:
            break


def get_iterator_cycle(repeat_value: int, source_list: list) -> Iterator:
    """Итератор, повторяющий элементы списка, определенного заранее"""
    _iter = cycle(source_list)
    for _ in range(repeat_value):
        yield next(_iter)


if __name__ == '__main__':
    try:
        args = parser.parse_args()
        if not args.start and not args.repeat:
            print("Воспользуйтесь --help для получения справки")
        if args.start:
            print("Вы выбрали итератор, генерирующий целые числа, "
                  f"начиная с указанного {args.start}")
            print("Результирующий список элементов:",
                  [_ for _ in get_iterator_count(args.start)])
        if args.repeat:
            print(f"Вы выбрали итератор, повторяющий элементы {args.repeat} раз "
                  "некоторого, списка, определенного заранее.")
            print("Результирующий список элементов:",
                  [_ for _ in get_iterator_cycle(args.repeat, "Я_список!")])
    except Exception as err:
        print(f"Ошибка: {err}")

"""
Результат выполнения:

> python task_6.py
Воспользуйтесь --help для получения справки

> python task_6.py --help
usage: task_6.py [-h] [--start START] [--repeat REPEAT]

Скрипт работает в двух режимах в зависимости от введенных Вами опциональных аргументов, подробнее смотрите описание аргументов

optional arguments:
  -h, --help       show this help message and exit
  --start START    Вернёт список из 10 элементов, начиная с указанного в параметре
  --repeat REPEAT  Вернёт повторяющийся список элементов по указанному количеству

> python task_6.py --repeat 20 --start 2
Вы выбрали итератор, генерирующий целые числа, начиная с указанного 2
Результирующий список элементов: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
Вы выбрали итератор, повторяющий элементы 20 раз некоторого, списка, определенного заранее.
Результирующий список элементов: ['Я', '_', 'с', 'п', 'и', 'с', 'о', 'к', '!', 'Я', '_', 'с', 'п', 'и', 'с', 'о', 'к', '!', 'Я', '_']

> python task_6.py --repeat sdf
usage: task_6.py [-h] [--start START] [--repeat REPEAT]
task_6.py: error: argument --repeat: invalid int value: 'sdf'
"""
