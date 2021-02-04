"""
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и 
секунды и выведите в формате 'чч:мм:сс'. Используйте форматирование строк.
"""
from typing import List


def get_attrs_time(seconds: int) -> List[int, ]:
    _period = (60, 60, 24, 12)
    _d = list()
    _whole = 1
    for value in _period:
        _d.append(seconds // _whole % value)
        _whole *= value
    return _d

    
try:
    _time_for_user = int(input("Введите время в секундах для конвертации:\n"))
    # _time_for_user = 87398
    seconds, minutes, hours, *other = get_attrs_time(_time_for_user)
    print("%(hours)02d:%(minutes)02d:%(seconds)02d" % {
        "hours": hours, "minutes": minutes, "seconds": seconds
    })
except ValueError:
    print("Введенное значение должно быть целым числом!")


"""
Вывод при запуске:

Введите время в секундах для конвертации:
>87398
00:16:38
"""