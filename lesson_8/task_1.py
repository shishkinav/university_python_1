"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату 
в виде строки формата «день-месяц-год». В рамках класса реализовать два метода. 
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и 
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, 
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). 
Проверить работу полученной структуры на реальных данных.
"""

from typing import Tuple
import datetime as dt


class Data:
    def __init__(self, date: str) -> None:
        self.date = date

    @classmethod
    def get_attrs(cls, date: str) -> Tuple:
        """Извлечение целочисленных значений день, месяц, год"""
        d: dt.datetime = Data.validate_date(date)
        return (d.day, d.month, d.year)
        

    @staticmethod
    def validate_date(date: str) -> dt:
        """Валидация формата передаваемой даты"""
        _format = '%d-%m-%Y'
        try:
            return dt.datetime.strptime(date, _format)
        except ValueError:
            raise ValueError('Format date fail. '
            'You need to use format "DD-MM-YYYY". Example: 12-12-2112')


if __name__ in "__main__":
    try:
        _data_1 = Data('12-12-2112')
        print(_data_1.get_attrs(_data_1.date))
        _data_2 = Data('32-12-21')
        print(_data_2.get_attrs(_data_2.date))
    except Exception as err:
        print(f'Ошибка: {err}')
    
"""
Результат выполнения:

(12, 12, 2112)
Ошибка: Format date fail. You need to use format "DD-MM-YYYY". Example: 12-12-2112
"""
