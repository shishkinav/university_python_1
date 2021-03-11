"""
6. Продолжить работу над пятым заданием. Реализуйте механизм валидации 
вводимых пользователем данных. Например, для указания количества принтеров, 
отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь по возможности реализовать в проекте 
«Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""

from lesson_8.task_4 import WareHouse, Equipment, Printer, Scaner, Xerox
from lesson_8.schemas import SchemaWareHouse, SchemaEquipment
from pydantic import ValidationError


if __name__ in "__main__":
    data = (
        (Printer, 'Canon', 'LBP-2900', 'P01 UTIL'),
        (Printer, 'HP', 'ISENSYS-01', 'P01'),
        (Scaner, 'HP', 'GOD666', 'AS01'),
        (Scaner, 'Laserjet', 'LBP-2900', 'S02'),
        (Xerox, 'Digma', 'BUILD5', 'X01 PRO'),
        (Xerox, 'Apple', 'M54', 'X02')
    )
    
    for obj, *args in data:
        try:
            maker, model, inv_number = args
            SchemaEquipment(maker=maker, model=model, inv_number=inv_number)
        except ValidationError as err:
            print(f'Передаваемые атрибуты не проходят валидацию: {err}')

"""
Результат выполнения:

Передаваемые атрибуты не проходят валидацию: 1 validation error for SchemaEquipment
inv_number
  Формат инвентарного номера AS01 некорректен (type=value_error)
"""
