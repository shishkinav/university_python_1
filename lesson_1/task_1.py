
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
_instance = int(5)
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
    ('instance = int(5)', _instance),
    ('instance == 5', _instance == 5),
    ('instance is 5', _instance is 5),
    ('instance is int()', _instance is int()),
    ('instance is int', _instance is int),
    ('instance is instance', _instance is _instance)
]

for values in _box_new:
    print(_expression_third.format(*values))


# Это результат вывода при запуске скрипта
"""
***** Список зарезервированных слов *****

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 
'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 
'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 
'raise', 'return', 'try', 'while', 'with', 'yield']

***** Преобразование и проверка типов *****

int(5) = 5
int(5.87) = 5
float(5.87) = 5.87
bool(1) = True
bool(0) = False
bool('') = False
bool('Я текст') = True
type(5) = <class 'int'>
type(5.55) = <class 'float'>
type('5') = <class 'str'>
type(True) = <class 'bool'>

***** Арифметические операции *****

Вы используете:
a = 100
b = 5.5

a + b      = 105.5
a - b      = 94.5
a * b      = 550.0
a / b      = 18.181818181818183
a // b     = 18.0
a % b      = 1.0
a ** b     = 100000000000.0

***** Логические операции *****

Напоминаем, что для сравнения вы используете:
a = 100
b = 5.5

a > b                = True
a < b                = False
a == b               = False
a != b               = True
a >= b               = True
a <= b               = False
bool(a and b)        = True
bool(a and None)     = False
bool(a or b)         = True
bool(not a or b)     = True
bool(not a or not b) = False
a in [1, 2, 3]       = False
a not in [1, 2, 3]   = True
a is 100             = True
a is not 100         = False
100 is a             = True
instance = int(5)    = 5
instance == 5        = True
instance is 5        = True
instance is int()    = False
instance is int      = False
instance is instance = True
"""