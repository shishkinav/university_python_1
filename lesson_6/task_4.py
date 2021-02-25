"""
4. Реализуйте базовый класс Car. 
У данного класса должны быть следующие атрибуты: 
    speed, color, name, is_police (булево). 
А также методы: go, stop, turn(direction), которые должны сообщать, 
    что машина поехала, остановилась, повернула (куда). 
    
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
Добавьте в базовый класс метод show_speed, который должен показывать 
текущую скорость автомобиля. 
Для классов TownCar и WorkCar переопределите метод show_speed. 
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться 
сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. 
Выполните доступ к атрибутам, выведите результат. 
Выполните вызов методов и также покажите результат.
"""
from typing import List


class Car:
    speed: int = 0
    is_police: bool = False
    is_crashed: bool = False

    def __init__(self, name: str, color: str) -> None:
        self.name, self.color = name, color

    def show_speed(self):
        return self.speed

    def go(self):
        if self.speed:
            return (f'Посмотри на панель, автомобиль {self.name} '
                    f'итак уже движется со скоростью {self.speed}')
        self.speed = 5
        return f'Ключ на старт. Автомобиль {self.name} начал движение!'

    def stop(self):
        self.speed = 0
        return f'Произведена полная остановка автомобиля {self.name}.'

    def turn(self, direction: str):
        return f'Автомобиль {self.name} движется {direction.lower()}.'


class TownCar(Car):
    max_speed: int = 60

    def show_speed(self):
        speed = super().show_speed()
        if speed > self.max_speed:
            print(f"Снижайте скорость. Для {self.name} "
                  f"максимально допустимая скорость {self.max_speed} км/ч!")
        return speed


class SportCar(Car):
    pass


class WorkCar(TownCar):
    max_speed: int = 40


class PoliceCar(Car):
    is_police: bool = True

    def stop(self):
        self.is_crashed = True
        self.speed = 0
        return (f'Аааа, тормоза отказали и {self.name} врезается'
                ' в стену. Увы авто выбыло из гонки!')


class Race:
    """Класс турнирной гонки"""
    def __init__(self, cars: List[Car]) -> None:
        self.cars = cars

    def check_not_crash(self) -> List:
        return [_ for _ in self.cars if not _.is_crashed]

    def _round_one(self):
        for _ in self.check_not_crash():
            print(_.go())
        print('\nЭтап "Старт" - Все стартовали и едут с одинаковой скоростью:')
        for _ in self.check_not_crash():
            print(_.name, f'{_.show_speed()} км/ч')

    def _round_two(self):
        print('Этап "Проверка на взрывную скорость + 100 км/ч"')
        for _ in self.check_not_crash():
            _.speed += 100
            print(_.name, f'{_.show_speed()} км/ч')
            if getattr(_, 'max_speed', None):
                if _.max_speed < _.speed:
                    _.is_crashed = True
                    print(_.stop())
                    print(
                        f'Двигатель {_.name} перегрелся и он выбыл из гонки...')

    def _round_three(self):
        print('Этап "Проверка на прохождение змейки"')
        for _ in self.check_not_crash():
            print(_.turn('объезжая фишку слева'))
            print(_.turn('объезжая фишку справа'))
            if _.color == 'red':
                _.is_crashed = True
                print(_.stop())
                print(f'Для {_.name} гонка закончилась, т.к. '
                      f'прибежали страусы, которым не нравится {_.color} '
                      'и они открутили авто колёса. Выбыл!')
                continue
            print(_.turn('назад'))
            print(_.turn('к финишной черте'))
            print(f'{_.name} прошёл дистанцию.')

    def _round_fourth(self):
        print('Этап "Экстренное торможение"')
        for _ in self.check_not_crash():
            print(_.stop())

    def start_racing(self):
        print('Сегодня нас ждёт поездка по удивительным местам!')

        for stage in (self._round_one,
                      self._round_two,
                      self._round_three,
                      self._round_fourth):
            stage()
            if not len(self.check_not_crash()):
                print('К сожалению, никому не удалось пройти полосу полностью!')
            print()


if __name__ == '__main__':
    try:
        cars = [
            TownCar('Daewoo', 'yellow'),
            SportCar('Ferrari', 'red'),
            WorkCar('Lada', 'black'),
            PoliceCar('Hyundai', 'blue')
        ]
        race = Race(cars)
        race.start_racing()
    except Exception as err:
        print(f'Ошибка: {err}')

"""
Результат выполнения:

Сегодня нас ждёт поездка по удивительным местам!
Ключ на старт. Автомобиль Daewoo начал движение!
Ключ на старт. Автомобиль Ferrari начал движение!
Ключ на старт. Автомобиль Lada начал движение!
Ключ на старт. Автомобиль Hyundai начал движение!

Этап "Старт" - Все стартовали и едут с одинаковой скоростью:
Daewoo 5 км/ч
Ferrari 5 км/ч
Lada 5 км/ч
Hyundai 5 км/ч

Этап "Проверка на взрывную скорость + 100 км/ч"
Снижайте скорость. Для Daewoo максимально допустимая скорость 60 км/ч!
Daewoo 105 км/ч
Произведена полная остановка автомобиля Daewoo.
Двигатель Daewoo перегрелся и он выбыл из гонки...
Ferrari 105 км/ч
Снижайте скорость. Для Lada максимально допустимая скорость 40 км/ч!
Lada 105 км/ч
Произведена полная остановка автомобиля Lada.
Двигатель Lada перегрелся и он выбыл из гонки...
Hyundai 105 км/ч

Этап "Проверка на прохождение змейки"
Автомобиль Ferrari движется объезжая фишку слева.
Автомобиль Ferrari движется объезжая фишку справа.
Произведена полная остановка автомобиля Ferrari.
Для Ferrari гонка закончилась, т.к. прибежали страусы, которым не нравится red и они открутили авто колёса. Выбыл!
Автомобиль Hyundai движется объезжая фишку слева.
Автомобиль Hyundai движется объезжая фишку справа.
Автомобиль Hyundai движется назад.
Автомобиль Hyundai движется к финишной черте.
Hyundai прошёл дистанцию.

Этап "Экстренное торможение"
Аааа, тормоза отказали и Hyundai врезается в стену. Увы авто выбыло из гонки!
К сожалению, никому не удалось пройти полосу полностью!
"""