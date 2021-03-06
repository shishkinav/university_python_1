"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. 
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

_number = input("Введите целое число:\n")

try:
    # проверяем, что введённое значение может быть преобразовано в int
    int(_number)
    # собираем tuple значений string
    _data = tuple(map(
        lambda x: x * _number, range(1, 4)
    ))
    # формируем визуальную часть выражения
    _expression = ' + '.join(_data)
    # рассчитываем сумму значений
    _result = sum(map(int, _data))
    print(f'Результат вычислений:\n{_expression} = {_result}')
except Exception as err:
    print(f"Введенное значение должно быть целым числом! Ошибка: {err}")
    
"""
Результат исполнения скрипта:

Введите целое число:
>3
Результат вычислений:
3 + 33 + 333 = 369

Введите целое число:
>321
Результат вычислений:
321 + 321321 + 321321321 = 321642963
"""