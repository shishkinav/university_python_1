"""
5. Реализовать класс Stationery (канцелярская принадлежность). 
Определить в нем атрибут title (название) и метод draw (отрисовка). 
Метод выводит сообщение “Запуск отрисовки.” 

Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). 
В каждом из классов реализовать переопределение метода draw. 
Для каждого из классов методы должен выводить уникальное сообщение. 
Создать экземпляры классов и проверить, что выведет описанный метод 
для каждого экземпляра.
"""
from abc import ABC, abstractmethod


class Stationery(ABC):
    """Абстрактный класс канцелярской принадлежности"""
    title: str = ''

    @abstractmethod
    def draw(self) -> None:
        """Метод отрисовки"""
        print(f'Запуск отрисовки {self.title.capitalize()}')


class Pen(Stationery):
    title: str = 'ручка'

    def draw(self) -> None:
        super().draw()
        print("I'm pen.")


class Pencil(Stationery):
    title: str = 'карандаш'

    def draw(self) -> None:
        super().draw()
        print("I'm pencil.")


class Handle(Stationery):
    title: str = 'маркер'

    def draw(self) -> None:
        super().draw()
        print("I'm handle.")


if __name__ == '__main__':
    try:
        for stationery in [Pen(), Pencil(), Handle()]:
            stationery.draw()
    except Exception as err:
        print(f'Ошибка: {err}')

"""
Результат выполнения:

> python task_5.py 
Запуск отрисовки Ручка
I'm pen.
Запуск отрисовки Карандаш
I'm pencil.
Запуск отрисовки Маркер
I'm handle.
"""