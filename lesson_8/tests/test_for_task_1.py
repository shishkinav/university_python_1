import datetime as dt
import pytest
from lesson_8.task_1 import Data


@pytest.mark.parametrize('date_str,day,month,year', [('12-12-2112', 12, 12, 2112),
                                                     ('24-03-1985', 24, 3, 1985)])
def test_get_attrs(date_str: str, day: int, month: int, year: int):
    """Проверка извлечения атрибутов из строковой даты"""
    obj = Data(date_str)
    _day, _month, _year, *args = obj.get_attrs(obj.date)
    assert not args, 'Метод get_attrs возвращает больше трёх значений.'
    for attr, value, name in ((_day, day, 'day'),
                              (_month, month, 'month'), 
                              (_year, year, 'year')):
        assert attr == value, f'Для атрибута {name} ожидалось получение ' \
            f'значения {attr}, а получено {value}.'


@pytest.mark.parametrize('date_str', ['32-12-2112', '24-03-85'])
def test_get_attrs_exception(date_str: str):
    """Проверка возбуждения исключения при некорректном формате"""
    obj = Data(date_str)
    with pytest.raises(ValueError) as execinfo:
        _day, _month, _year, *args = obj.get_attrs(date_str)
    assert 'Format date fail. You need to use format "DD-MM-YYYY". ' \
        'Example: 12-12-2112' in str(execinfo.value), \
        f'При работе с {date_str} - исключение не возбуждено'
        

@pytest.mark.parametrize('date_str', ['12-12-2112', '24-03-1985'])
def test_validate_date(date_str: str):
    """Проверка извлечения атрибутов из строковой даты"""
    obj = Data(date_str)
    date = obj.validate_date(date_str)
    assert isinstance(date, dt.datetime), 'Валидация не произведена'
    
    
