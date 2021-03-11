import pytest
from lesson_8.task_7 import ComplexNumber


@pytest.mark.parametrize('imag1,real1,imag2,real2',
                         [(1, -1, 3, 6),
                          (1.00, 2.25, -1, -4.45)])
def test_complex_add(imag1, real1, imag2, real2):
    """Проверка сложения комплексных чисел"""
    our_complex = ComplexNumber(imag1, real1) + ComplexNumber(imag2, real2)
    base_complex = complex(imag1, real1) + complex(imag2, real2)
    _text = 'При сложении комплексных чисел с входными параметрами ' \
        f'{(imag1, real1, imag2, real2)} - расхождение с базовым результатом.'
    assert our_complex.a == base_complex.real, _text
    assert our_complex.b == base_complex.imag, _text


@pytest.mark.parametrize('imag1,real1,imag2,real2',
                         [(1, -1, 3, 6),
                          (1.00, 2.25, -1, -4.45)])
def test_complex_mul(imag1, real1, imag2, real2):
    """Проверка умножение комплексных чисел"""
    our_complex = ComplexNumber(imag1, real1) * ComplexNumber(imag2, real2)
    base_complex = complex(imag1, real1) * complex(imag2, real2)
    _text = 'При умножении комплексных чисел с входными параметрами ' \
        f'{(imag1, real1, imag2, real2)} - расхождение с базовым результатом.'
    assert our_complex.a == base_complex.real, _text
    assert our_complex.b == base_complex.imag, _text
