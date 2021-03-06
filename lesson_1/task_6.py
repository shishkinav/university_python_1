"""
6. Спортсмен занимается ежедневными пробежками. В первый день его 
результат составил a километров. Каждый день спортсмен увеличивал 
результат на 10 % относительно предыдущего. Требуется определить 
номер дня, на который общий результат спортсмена составить 
не менее b километров. Программа должна принимать значения 
параметров a и b и выводить одно натуральное число — номер дня.

Например: a = 2, b = 3.

Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22

Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""
import sys


global a
global b

try:
    a = float(input("Введите результат первого дня, км:\n"))
    b = float(input("Введите результат, которого хотим достичь, км:\n"))
except Exception as err:
    print("Значение километража, необходимо вводит целым положительным числом, "
        f"либо числом с плавающей точкой. Example: 100.99 or 14\nОшибка: {err}")
    sys.exit()
_day, _value = 1, a
print("Результат:")
while True:
    print(f'{_day}-й день: {_value:.2f}')
    if b < _value:
        break
    else:
        _day += 1
        _value += _value * 0.1

print(f'Ответ: на {_day}-й день спортсмен достиг результата — не менее {b:.2f} км.')

"""
Результат выполнения программы:

Введите результат первого дня, км:
>2
Введите результат, которого хотим достичь, км:
>5.5
Результат:
1-й день: 2.00
2-й день: 2.20
3-й день: 2.42
4-й день: 2.66
5-й день: 2.93
6-й день: 3.22
7-й день: 3.54
8-й день: 3.90
9-й день: 4.29
10-й день: 4.72
11-й день: 5.19
12-й день: 5.71
Ответ: на 12-й день спортсмен достиг результата — не менее 5.50 км.
"""
