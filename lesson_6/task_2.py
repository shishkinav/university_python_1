"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: 
length (длина), width (ширина). Значения данных атрибутов должны передаваться 
при создании экземпляра класса. Атрибуты сделать защищенными. 
Определить метод расчета массы асфальта, необходимого для покрытия всего 
дорожного полотна. 

Использовать формулу: 
    длина * ширина * масса асфальта для покрытия одного кв метра дороги 
    асфальтом, толщиной в 1 см * число см толщины полотна. 

Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""
from functools import reduce


class Road:
    """Класс дорога"""
    expense_per_meter: float = 25

    def __check_value(self, value):
        """Условие положительности вводимых значений"""
        if value <= 0:
            raise ValueError("Все величины должны быть больше 0")
        return value

    def __init__(self, length: float, width: float) -> None:
        """Инициализация объема работ по длине и ширине в метрах"""
        self._length: float = self.__check_value(length)
        self._width: float = self.__check_value(width)

    def calculate_weight(self, depth: int) -> float:
        """Итоговый расчет расходов с учётом задаваемой толщины 
        покрытия в сантиметрах"""
        self.__check_value(depth)
        result = reduce(
            lambda x, y: x * y,
            (self._width, self._length, self.expense_per_meter, depth))
        return round(result / 1000, 2)


if __name__ == '__main__':
    try:
        road = Road(length=5000, width=20)
        expense = road.calculate_weight(depth=5)
        print(f"Потребуется {expense} тонн")
    except Exception as err:
        print(f'Ошибка: {err}')

"""
Результат выполнения:

> python task_2.py 
Потребуется 12500.0 тонн
"""
