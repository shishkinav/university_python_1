"""
1. Реализовать класс Matrix (матрица). 
Обеспечить перегрузку конструктора класса (метод __init__()), 
    который должен принимать данные (список списков) для 
    формирования матрицы.

Подсказка: матрица — система некоторых математических величин, 
    расположенных в виде прямоугольной схемы.
    Примеры матриц вы найдете в методичке.

Следующий шаг — реализовать перегрузку метода __str__() для вывода 
    матрицы в привычном виде.

Далее реализовать перегрузку метода __add__() для реализации операции 
    сложения двух объектов класса Matrix (двух матриц). 
    Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно — первый 
    элемент первой строки первой матрицы складываем с первым элементом 
    первой строки второй матрицы и т.д.
"""
from typing import List
from random import randint


class Matrix:
    """Объект матрицы"""
    def __init__(self, body: List[List, ]) -> None:
        """Инцииализация объекта с первичными данными List[List,]"""
        self.body = body

    def __str__(self) -> str:
        """Строковое представление матрицы"""
        _format_row = ''.join(['{:<5} ' for _ in self.body[0]])
        return '\n'.join([_format_row.format(*row) for row in self.body])

    def __add__(self, other) -> object:
        """Перегрузка логики сложения двух матриц"""
        if len(self.body) != len(other.body) or len(self.body[0]) != len(other.body[0]):
            raise ValueError('Для сложения размерность матриц должна быть одинаковая!')
        new_matrix = []
        for idx_row in range(len(self.body)):
            new_matrix.append(
                [self.body[idx_row][idx_column] + other.body[idx_row][idx_column] \
                    for idx_column in range(len(self.body[0]))]
            )
        return Matrix(new_matrix)


if __name__ in '__main__':
    try:
        row, column = 5, 3
        m = [[randint(1, 100) for _ in range(column)] for _ in range(row)]
        matrix1 = Matrix(body=m)
        print(f"matrix1:\n{matrix1}")
        row, column = 5, 3
        m = [[randint(1, 100) for _ in range(column)] for _ in range(row)]
        matrix2 = Matrix(body=m)
        print(f"matrix2:\n{matrix2}")
        print(f"result:\n{matrix1 + matrix2}")
    except Exception as err:
        print(f'Ошибка: {err}')

"""
Результат выполнения:

matrix1:
8     4     6     
11    99    41    
11    48    70    
97    40    41    
12    30    100   
matrix2:
36    72    2     
76    37    69    
16    77    73    
74    36    34    
56    29    65    
result:
44    76    8     
87    136   110   
27    125   143   
171   76    75    
68    59    165
"""
