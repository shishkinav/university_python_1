import pytest
from lesson_7.task_3 import OrganicCell


@pytest.fixture(params=[(2, 1), (4, 3), (6, 5)])
def right_cell_box(request):
    """Наборы пар органических клеток где первая всегда
    имеет БОЛЬШЕЕ кол-во ячеек чем вторая клетка"""
    cell_1, cell_2 = request.param
    box = (OrganicCell(cell_1), OrganicCell(cell_2))
    yield box
    for _ in box:
        del _


@pytest.fixture(params=[(7, 8), (9, 10)])
def wrong_cell_box(request):
    """Наборы пар органических клеток где первая всегда
    имеет МЕНЬШЕЕ кол-во ячеек чем вторая клетка"""
    cell_1, cell_2 = request.param
    box = (OrganicCell(cell_1), OrganicCell(cell_2))
    yield box
    for _ in box:
        del _