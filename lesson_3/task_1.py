
"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и 
выполняющую их деление. Числа запрашивать у пользователя, предусмотреть 
обработку ситуации деления на ноль.
"""

def our_func(first: float, second: float) -> float:
    try:
        return first / second
    except Exception as err:
        print(f"Ошибка {err}")


if __name__ == '__main__':
    try:
        a = float(input("Введите делимое число, example: 100.45\n"))
        b = float(input("Введите число-делитель, example: 100.45\n"))
        print(f"Результат деления:\n{a} / {b} = {our_func(a, b)}")
    except Exception as err:
        print(f"Ошибка {err}")

"""
Результат выполнения:

# Первая попытка
Введите делимое число, example: 100.45
> sdf
Ошибка could not convert string to float: 'sdf'

# Вторая попытка
Введите делимое число, example: 100.45
> 10005.98
Введите число-делитель, example: 100.45
> 5423
Результат деления:
10005.98 / 5423.0 = 1.8451004978794026

# Третья попытка
Введите делимое число, example: 100.45
> 23424
Введите число-делитель, example: 100.45
> 0
Ошибка float division by zero
Результат деления:
23424.0 / 0.0 = None
"""
