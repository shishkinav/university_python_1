import pytest
from lesson_8.task_2 import our_div, DivisorError


@pytest.mark.parametrize('d, div', [(1000, '1000'),
                                    (1.00, '1.00'),
                                    (50.01, '50.01')])
def test_our_div(d: float, div: str):
    """Проверка корректности работы функции"""
    assert our_div(d, div) == 1.00, \
        f'Ошибка при делении {d} / {div} = {our_div(d, div)}.'


@pytest.mark.parametrize('div', ['str', '0,00', '0.00', 0])
def test_div_exception(div):
    """Проверка возбуждения нашего исключения"""
    with pytest.raises(DivisorError) as execinfo:
        our_div(1, div)

