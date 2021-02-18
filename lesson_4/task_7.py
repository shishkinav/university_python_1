"""
7. Реализовать генератор с помощью функции с ключевым словом yield, 
создающим очередное значение. При вызове функции должен создаваться 
объект-генератор. 

Функция должна вызываться следующим образом: for el in fact(n). 

Функция отвечает за получение факториала числа, а в цикле необходимо 
выводить только первые n чисел, начиная с 1! и до n!.

Подсказка: факториал числа n — произведение чисел от 1 до n. 
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""
from typing import Generator
from functools import reduce
from argparse import ArgumentParser


parser = ArgumentParser(description="""
    Получить рассчитанный список факториалов от 1! до n!
    Рассчитываем через reduce, хотя можно было бы и через
    from math import factorial""")
parser.add_argument("n",
                    help="Порядковый номер элемента факториала" \
                         " до которого будем считать",
                    type=int)


def fact(n: int) -> Generator:
    """Генератор, который возвращает значения факториалов для 
    элементов от 1! до переданного !n"""
    for number in range(1, n + 1):
        yield number, reduce(lambda x, y: x * y, range(1, number + 1))


if __name__ == '__main__':
    try:
        args = parser.parse_args()
        for el in fact(args.n):
            print(f"{el[0]:>5}! = {el[1]}")
    except Exception as err:
        print(f"Ошибка: {err}")

"""
Результат выполнения:

> python task_7.py --help
usage: task_7.py [-h] n

Получить рассчитанный список факториалов от 1! до n! Рассчитываем через reduce, хотя можно было бы и через from math import factorial

positional arguments:
  n           Порядковый номер элемента факториала до которого будем считать

optional arguments:
  -h, --help  show this help message and exit

> python task_7.py 10
    1! = 1
    2! = 2
    3! = 6
    4! = 24
    5! = 120
    6! = 720
    7! = 5040
    8! = 40320
    9! = 362880
   10! = 3628800
"""
