"""
4. Программа принимает действительное положительное число x и 
целое отрицательное число y. Необходимо выполнить возведение числа x в степень y. 
Задание необходимо реализовать в виде функции my_func(x, y). 
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами. 
    Первый — возведение в степень с помощью оператора **. 
    Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""

def my_func_1(x: float, y: int):
    """Возведение в степень с помощью оператора **.
    Функция pow() не используется."""
    return x ** y if y > 0 else 1 / x ** abs(y)


def my_func_2(x: float, y: int):
    """Возведение в степень БЕЗ помощи оператора **, используя цикл.
    Функция pow() не используется."""
    count = abs(y)
    result = 1
    while count > 0:
        result *= x
        count -= 1
    return result if y > 0 else 1 / result


if __name__ == '__main__':
    try:
        x = float(input("Введите любое действительное положительное число:\n"))
        if x <= 0:
            raise ValueError("Действительное положительное это > 0")
        y = int(input("Введите целое отрицательное число:\n"))

        print(my_func_1(x, y))
        print(my_func_2(x, y))
    except Exception as err:
        print(f"Ошибка: {err}")

"""
Результат выполнения:

Введите любое действительное положительное число:
> -3.33 
Ошибка: Действительное положительное это > 0

Введите любое действительное положительное число:
> 3.33
Введите целое отрицательное число:
> -5
0.0024421865352204065
0.0024421865352204065
"""