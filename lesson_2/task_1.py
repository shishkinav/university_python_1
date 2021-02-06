
"""
1. Создать список и заполнить его элементами различных типов данных. 
Реализовать скрипт проверки типа данных каждого элемента. Использовать 
функцию type() для проверки типа. Элементы списка можно не запрашивать 
у пользователя, а указать явно, в программе.
"""
from copy import deepcopy
import typing


example_list = [
    int(5), str(5), float(5.5), complex(5, 5), bool(5), list((5,)), 
    tuple((5,)), dict(key=5), set((5,)), frozenset((5,)), deepcopy
]
example_dict = {
    'int': 'Целочисленная переменная',
    'str': 'Строковая переменная',
    'float': 'Число с плавающей точкой',
    'complex': 'Комплексное число',
    'bool': 'Булево значение',
    'list': 'Список',
    'tuple': 'Кортеж',
    'dict': 'Словарь',
    'set': 'Множество (изменяемое)',
    'frozenset': 'Множество (неизменяемое)',
    'function': 'Функция'
}

for element in example_list:
    _obj_type = type(element).__name__
    print("{expression:<20} - {description}".format(
        expression=f"{_obj_type}()",
        description=(
            example_dict.get(_obj_type) if _obj_type in example_dict.keys() else "Noname"
        ).lower()
    ))

"""
Результат выполнения:

int()                - целочисленная переменная
str()                - строковая переменная
float()              - число с плавающей точкой
complex()            - комплексное число
bool()               - булево значение
list()               - список
tuple()              - кортеж
dict()               - словарь
set()                - множество (изменяемое)
frozenset()          - множество (неизменяемое)
function()           - функция
"""