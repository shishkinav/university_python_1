"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления 
на нуль. Проверьте его работу на данных, вводимых пользователем. 
При вводе пользователем нуля в качестве делителя программа должна корректно 
обработать эту ситуацию и не завершиться с ошибкой.
"""

from typing import Tuple
import datetime as dt


class DivisorError(ValueError):
    def __init__(self, message):
        self.txt = message


def our_div(d: float, div):
    try:
        div = float(div)
    except ValueError:
        raise DivisorError('Я ожидаю от тебя число-делитель.')
    if not div:
        raise DivisorError('На ноль делить нельзя.')
    return round(d / div, 2)


if __name__ in "__main__":
    while True:
        number = input('Введите число делитель:\n')
        if number == 'stop':
            break
        try:
           print(f'Результат: 1000 / {number} = {our_div(1000, number)}') 
        except DivisorError as err:
            print(f'Ошибка: {err}')

"""
Результат выполнения:

Введите число делитель:
> 0
Ошибка: На ноль делить нельзя.
Введите число делитель:
> 1.01
Результат: 1000 / 1.01 = 990.1
Введите число делитель:
> 0.00
Ошибка: На ноль делить нельзя.
Введите число делитель:
> ыпа
Ошибка: Я ожидаю от тебя число-делитель.
Введите число делитель:
> 1000
Результат: 1000 / 1000 = 1.0
Введите число делитель:
> stop
"""
