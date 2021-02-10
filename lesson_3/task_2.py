"""
2. Реализовать функцию, принимающую несколько параметров, описывающих 
данные пользователя: 
    имя, 
    фамилия, 
    год рождения, 
    город проживания, 
    email, 
    телефон. 
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""
import re


def get_data_user(
    first_name: str, last_name: str, city: str, phone: str, email: str, *args,
    year_birth: int = 2021, **kwargs) -> str:
    """Функция принимает набор данных, описывающих пользователя, и
    возвращает их единой строкой значений через запятую.
    Для phone и email предусмотрена валидация передаваемого значения."""
    pattern_email = r'.+@.+\.\w{2,4}'
    pattern_phone = r'\+7\s{1}\(\d{3}\)\s{1}\d{3}-\d{2}-\d{2}'
    if not re.match(pattern_phone, phone):
        raise ValueError("Номер телефона имеет неверный формат. Exapmle: +7 (999) 888-77-66")
    if not re.match(pattern_email, email):
        raise ValueError("email имеет неверный формат. Exapmle: xxxxxx@xxxx.xx")
    return ", ".join([
        first_name, last_name, city, phone, email, *[str(_) for _ in args], 
        str(year_birth), *[str(_) for _ in kwargs.values()]
    ])


def __gen_data() -> dict:
    """Приватный simple генератор для этого урока, который
    позволит нам перебрать варианты обращения к функции"""
    template = {
        'first_name': 'Анатолий', 'last_name': 'Шишкин',
        'phone': '+7 (999) 888-77-66', 'city': 'Волгоград',
        'email': 'example@domain.com', 'year_birth': 1985
    }
    yield template
    template.update({'place': 'GeekBrains'})
    yield template
    template.update({'phone': '89998887766'})
    yield template
    template.update({'phone': '+7 (999) 888-77-66',
        'email': 'example@domain'})
    yield template


if __name__ == '__main__':
    for data in __gen_data():
        try:
            arrgs = ', '.join([f'{key}={value}' for key, value in data.items()])
            print(f'\nПередавали именованные аргументы: {arrgs}')
            print('Результат:', get_data_user(**data))
        except Exception as err:
            print(f"Ошибка: {err}")

"""
Результат выполнения:

Передавали именованные аргументы: first_name=Анатолий, last_name=Шишкин, phone=+7 (999) 888-77-66, city=Волгоград, email=example@domain.com, year_birth=1985
Результат: Анатолий, Шишкин, Волгоград, +7 (999) 888-77-66, example@domain.com, 1985

Передавали именованные аргументы: first_name=Анатолий, last_name=Шишкин, phone=+7 (999) 888-77-66, city=Волгоград, email=example@domain.com, year_birth=1985, place=GeekBrains
Результат: Анатолий, Шишкин, Волгоград, +7 (999) 888-77-66, example@domain.com, 1985, GeekBrains

Передавали именованные аргументы: first_name=Анатолий, last_name=Шишкин, phone=89998887766, city=Волгоград, email=example@domain.com, year_birth=1985, place=GeekBrains
Ошибка: Номер телефона имеет неверный формат. Exapmle: +7 (999) 888-77-66

Передавали именованные аргументы: first_name=Анатолий, last_name=Шишкин, phone=+7 (999) 888-77-66, city=Волгоград, email=example@domain, year_birth=1985, place=GeekBrains
Ошибка: email имеет неверный формат. Exapmle: xxxxxx@xxxx.xx
"""