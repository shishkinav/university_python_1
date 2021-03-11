"""
7. Реализовать проект «Операции с комплексными числами». 
Создайте класс «Комплексное число», реализуйте перегрузку методов 
сложения и умножения комплексных чисел. Проверьте работу проекта, 
создав экземпляры класса (комплексные числа) и выполнив сложение 
и умножение созданных экземпляров. Проверьте корректность 
полученного результата.
"""


class ComplexNumber:
    def __init__(self, a, b) -> None:
        self.a, self.b = a, b

    def __add__(self, other):
        return ComplexNumber(
            self.a + other.a,
            self.b + other.b
        )

    def __mul__(self, other):
        return ComplexNumber(
            self.a * other.a - self.b * other.b,
            self.a * other.b + self.b * other.a
        )

    def __str__(self) -> str:
        return f'{self.a} + {self.b}i' if self.b >= 0 else f'{self.a} {self.b}i'

if __name__ in "__main__":
    c1 = ComplexNumber(1, -1)
    c2 = ComplexNumber(3, 6)
    print("Сложение", c1 + c2)
    print("Умножение", c1 * c2)

"""
Результат выполнения:

Сложение 4 + 5i
Умножение 9 + 3i

"""
