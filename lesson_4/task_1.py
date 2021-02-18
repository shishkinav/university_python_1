"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета 
заработной платы сотрудника. В расчете необходимо использовать формулу: 

(выработка в часах * ставка в час) + премия. 

Для выполнения расчета для конкретных значений необходимо 
запускать скрипт с параметрами.
"""
from sys import argv


def calculation_salary(hours: float, rate_per_hour: float,
                       bonus: float) -> float:
    """Расчёт заработной платы сотрудника по формуле
    ( hours(выработка в часах) * rate_per_hour(ставка в час) ) + bonus(премия)"""
    hours, rate_per_hour, bonus = float(
        hours), float(rate_per_hour), float(bonus)
    if hours <= 0 or rate_per_hour <= 0 or bonus < 0:
        raise ValueError('Все аргументы не могут быть меньше 0')
    return (hours * rate_per_hour) + bonus


if __name__ == '__main__':
    try:
        salary = calculation_salary(*argv[1:])
        print(f'Получи у бухгалтера: {salary} руб.')
    except Exception as err:
        print(f"Ошибка: {err}")


"""
Результат выполнения:

> python task_1.py 1 1 -5
Ошибка: Все аргументы не могут быть меньше 0
> python task_1.py 10 10 5.55
Получи у бухгалтера: 105.55 руб.
"""
