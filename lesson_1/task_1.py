
"""
1. Поработайте с переменными, создайте несколько, выведите на экран, 
запросите у пользователя несколько чисел и строк и сохраните в 
переменные, выведите на экран.
"""
from keyword import kwlist

# input("Введите целое число:") -> str
# так можно запрашиваться данные у пользователя, возвращает всегда str

# манипуляции с числами и строкам без input сделаю, чтобы руками не вводить

_expression = "\n{marker} {title} {marker}\n"
_marker='*' * 5

print(_expression.format(title='Список зарезервированных слов', marker=_marker))
print(kwlist)

print(_expression.format(title='Преобразование и проверка типов', marker=_marker))
_integer = 5
print(
    "int(%s) = %d" % (_integer, int(_integer))
)
_float = 5.87
print(
    "int({1}) = {0}".format(int(_float), _float)
)
print(
    "float({1}) = {0}".format(float(_float), _float)
)
print(
    f"bool(1) = {bool(1)}"
)
print(
    f"bool(0) = {bool(0)}"
)
print(
    f"bool('') = {bool('')}"
)
print(
    f"bool('Я текст') = {bool('Я текст')}"
)
print(
    f"type(5) = {type(5)}"
)
print(
    f"type(5.55) = {type(5.55)}"
)
print(
    f"type('5') = {type('5')}"
)
print(
    f"type(True) = {type(True)}"
)

print(_expression.format(title='Арифметические операции', marker=_marker))
_a: int = 100
_b: float = 5.5
_box: list = [
    ('a + b', _a + _b),
    ('a - b', _a - _b),
    ('a * b', _a * _b),
    ('a / b', _a / _b),
    ('a // b', _a // _b),
    (''.join(['a ', u'%', ' b']), _a % _b),
    ('a ** b', _a ** _b)
]
_expression_second = "{:<10} = {}"
print(f"Вы используете:\na = {_a}\nb = {_b}\n")

for s, value in _box:
    print(_expression_second.format(s, value))

print(_expression.format(title='Логические операции', marker=_marker))

print(f'Напоминаем, что для сравнения вы используете:\na = {_a}\nb = {_b}\n')
_expression_third = "{:<20} = {}"
_box_new: list = [
    ('a > b', _a > _b),
    ('a < b', _a < _b),
    ('a == b', _a == _b),
    ('a != b', _a != _b),
    ('a >= b', _a >= _b),
    ('a <= b', _a <= _b),
    ('bool(a and b)', bool(_a and _b)),
    ('bool(a and None)', bool(_a and None)),
    ('bool(a or b)', bool(_a or _b)),
    ('bool(not a or b)', bool(not _a or _b)),
    ('bool(not a or not b)', bool(not _a or not _b)),
    ('a in [1, 2, 3]', _a in [1, 2, 3]),
    ('a not in [1, 2, 3]', _a not in [1, 2, 3]),
    ('a is 100', _a is 100),
    ('a is not 100', _a is not 100),
    ('100 is a', 100 is _a),
]

for values in _box_new:
    print(_expression_third.format(*values))

print(_expression.format(title='Арифметические операции', marker=_marker))