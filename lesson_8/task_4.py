"""
4. Начните работу над проектом «Склад оргтехники». 
Создайте класс, описывающий склад. А также класс «Оргтехника», 
который будет базовым для классов-наследников. 
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
В базовом классе определить параметры, общие для приведенных типов. 
В классах-наследниках реализовать параметры, уникальные для каждого 
типа оргтехники.
"""

from abc import ABC, abstractmethod
from prettytable import PrettyTable


class Equipment(ABC):
    is_broken = False

    def __init__(self, maker: str, model: str, inv_number: str) -> None:
        self.type_obj = self.__class__.__name__
        self.manufacturer = maker
        self.model = model
        self.inventory_number = inv_number

    @abstractmethod
    def get_functions(self) -> list: ...

    def check_broken(self):
        if 'UTIL' in self.inventory_number:
            self.is_broken = True
            raise TypeError(f'Мусор на складе не хранят! {self} в утиль!')

    def __str__(self) -> str:
        return f'{self.__class__.__name__} {self.manufacturer} {self.model}'


class Printer(Equipment):
    _output = True

    def get_functions(self) -> list:
        return 'печать'

class Scaner(Equipment):
    _input = True

    def get_functions(self) -> list:
        return 'сканирование'


class Xerox(Equipment):
    _output = True
    _input = True

    def get_functions(self) -> list:
        return 'печать, сканирование, копирование'

class WareHouse(dict):
    def __init__(self, name) -> None:
        self.name = name

    def update(self, equip: Equipment) -> None:
        try:
            equip.check_broken()
            obj_list = self.get(equip.type_obj)
            if obj_list:
                new_value = obj_list + [equip]
            else:
                new_value = [equip]
            super().update({equip.type_obj: new_value})
        except Exception as err:
            print(err)

    def __str__(self) -> str:
        x = PrettyTable()
        x.field_names = ["Тип оборудования", "Количество", "Функциональность"]
        x.add_rows(
            [[key, len(value), value[0].get_functions() if len(value) else 'empty'] \
                for key, value in self.items()]
        )
        return x.get_string()


if __name__ in "__main__":
    warehouse = WareHouse('Обитель техники')
    data = (
        (Printer, 'Canon', 'LBP-2900', 'P01 UTIL'),
        (Printer, 'HP', 'ISENSYS-01', 'P01'),
        (Scaner, 'HP', 'GOD666', 'S01'),
        (Scaner, 'Laserjet', 'LBP-2900', 'S02'),
        (Xerox, 'Digma', 'BUILD5', 'X01 PRO'),
        (Xerox, 'Apple', 'M54', 'X02')
    )
    for obj, *args in data:
        warehouse.update(obj(*args))
    print(warehouse)

"""
Результат выполнения:

Мусор на складе не хранят! Printer Canon LBP-2900 в утиль!
+------------------+------------+-----------------------------------+
| Тип оборудования | Количество |          Функциональность         |
+------------------+------------+-----------------------------------+
|     Printer      |     1      |               печать              |
|      Scaner      |     2      |            сканирование           |
|      Xerox       |     2      | печать, сканирование, копирование |
+------------------+------------+-----------------------------------+
"""
