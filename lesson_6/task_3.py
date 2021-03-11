"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: 
    name, surname, position (должность), income (доход). 
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: 
    оклад и премия, например, {"wage": wage, "bonus": bonus}. 
    
Создать класс Position (должность) на базе класса Worker. 
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) 
и дохода с учетом премии (get_total_income). Проверить работу примера на реальных 
данных (создать экземпляры класса Position, передать данные, проверить значения 
атрибутов, вызвать методы экземпляров).
"""
from collections import namedtuple


pos = namedtuple('Grid',
                 field_names=['title', 'wage', 'bonus'])
grids = [pos(title, wage, bonus) for title, wage, bonus in (
    ('Waiter', 10000, 5000),
    ('Director', 100000, 50000),
    ('Manager', 10000, 30000)
)]


class Worker:
    """Базовый класс работника"""
    _income: pos = None

    def __init__(self, name: str, surname: str, position: str) -> None:
        self.name, self.surname = name, surname
        self.position = position.capitalize()
        for pos in grids:
            if pos.title == self.position:
                self._income = pos
        if not self._income:
            raise ValueError("Указанная позиция отсутствует в фирме")


class Position(Worker):
    """Класс позиции сотрудника в фирме"""

    def get_full_name(self) -> str:
        """Метод возврата полного имени"""
        return f'{self.surname} {self.name}'.title()

    def get_total_income(self) -> str:
        """Метод определения максимально возможного дохода"""
        return round(self._income.wage + self._income.bonus, 2)


if __name__ == '__main__':
    try:
        staff = [Position(*_) for _ in (
            ('Анатолий', 'Шишкин', 'waiter'),
            ('иван', 'сидоров', 'director'),
            ('Сергей', 'иванов', 'manager'),
        )]
        _format = '{:<30} {}'
        print(_format.format('Фамилия Имя', 'Максимальная ЗП'))
        _format += ' руб.'
        for employee in staff:
            print(_format.format(
                employee.get_full_name(),
                employee.get_total_income()
            ))
    except Exception as err:
        print(f'Ошибка: {err}')

"""
Результат выполнения:

> python task_3.py 
Фамилия Имя                    Максимальная ЗП
Шишкин Анатолий                15000 руб.
Сидоров Иван                   150000 руб.
Иванов Сергей                  40000 руб.
"""
