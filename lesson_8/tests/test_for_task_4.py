import pytest
from lesson_8.task_4 import WareHouse


def test_create_warehouse():
    """Проверка создания склада и извлечение имени"""
    warehouse = WareHouse('Название склада')
    assert isinstance(warehouse, WareHouse)
    assert warehouse.name == 'Название склада', \
        'Извлечение имени проходит неправильно'


