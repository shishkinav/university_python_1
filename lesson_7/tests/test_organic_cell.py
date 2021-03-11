from typing import Tuple
import pytest
from lesson_7.task_3 import OrganicCell


def test_add_cell(right_cell_box: Tuple[OrganicCell, OrganicCell]):
    """Проверка корректности перегрузки метода __add__"""
    obj_1, obj_2 = right_cell_box
    new_cell: OrganicCell = obj_1 + obj_2
    assert new_cell.cell == obj_1.cell + obj_2.cell, \
        f"При сложении класса {obj_1.__dict__} с классом {obj_2.__dict__} " \
        f"мы получили класс {new_cell.__dict__}"


def test_sub_cell(right_cell_box: Tuple[OrganicCell, OrganicCell]):
    """Проверка корректности перегрузки метода __sub__"""
    obj_1, obj_2 = right_cell_box
    new_cell: OrganicCell = obj_1 - obj_2
    assert new_cell.cell == obj_1.cell - obj_2.cell, \
        f"При вычитании из класса {obj_1.__dict__} класса {obj_2.__dict__} " \
        f"мы получили класс {new_cell.__dict__}"


def test_mul_cell(right_cell_box: Tuple[OrganicCell, OrganicCell]):
    """Проверка корректности перегрузки метода __mul__"""
    obj_1, obj_2 = right_cell_box
    new_cell: OrganicCell = obj_1 * obj_2
    assert new_cell.cell == obj_1.cell * obj_2.cell, \
        f"При умножении класса {obj_1.__dict__} на класс {obj_2.__dict__} " \
        f"мы получили класс {new_cell.__dict__}"


def test_truediv_cell(right_cell_box: Tuple[OrganicCell, OrganicCell]):
    """Проверка корректности перегрузки метода __truediv__"""
    obj_1, obj_2 = right_cell_box
    new_cell: OrganicCell = obj_1 / obj_2
    assert new_cell.cell == obj_1.cell // obj_2.cell, \
        f"При делении класса {obj_1.__dict__} на класс {obj_2.__dict__} " \
        f"мы получили класс {new_cell.__dict__}"


def test_sub_exception(wrong_cell_box: Tuple[OrganicCell, OrganicCell]):
    """Проверка возбуждения исключения если первая клетка содержит
    меньше ячеек чем вторая"""
    obj_1, obj_2 = wrong_cell_box
    with pytest.raises(AssertionError) as execinfo:
        new_cell: OrganicCell = obj_1 - obj_2
    assert str(execinfo.value) == "У исходной клетки недостаточно ячеек."


def test_truediv_exception():
    """Проверка возбуждения исключения при делении на ноль"""
    with pytest.raises(ZeroDivisionError) as execinfo:
        OrganicCell(10) / OrganicCell(0)


@pytest.mark.parametrize('expression', ['+', '-', '*', '/'])
def test_truediv_exception(expression: str):
    """Проверка возбуждения исключения от декоратора в случаях когда 
    мы пытаемся использовать базовую арифметику для разных классов"""
    class Temp:
        pass
    with pytest.raises(TypeError) as execinfo:
        eval(f'OrganicCell(10) {expression} Temp()')
    assert 'Допустимо производить действия только с' in str(execinfo.value)


@pytest.mark.parametrize('object,count_row,str_result', [
    (OrganicCell(12), 5, '*****\n*****\n**'),
    (OrganicCell(15), 5, '*****\n*****\n*****\n'),
    (OrganicCell(4), 5, '****')
])
def test_make_order(object: OrganicCell, count_row: int, str_result: str):
    """Проверка строковых возвратов метода make_order"""
    assert object.make_order(count_row) == str_result, \
        f'Метод make_order({count_row}) для объекта {object.__dict__} ' \
        f'должен возвращать:\n{str_result}'
