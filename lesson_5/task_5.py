"""
5. Создать (программно) текстовый файл, записать в него программно 
набор чисел, разделенных пробелами. Программа должна подсчитывать 
сумму чисел в файле и выводить ее на экран.
"""
from random import random


try:
    # генерируем 50 случайных float значений и записываем в файл через пробел
    with open('task_5_result.txt', 'w', encoding='utf-8') as fw:
        fw.writelines(
            [f"{round(random() * (15000 - 5000) + 5000, 2)} " for _ in range(50)]
        )
    # считываем значения и суммируем
    with open('task_5_result.txt') as fr:
        s = sum(
            [float(number) for number in fr.read().split()]
        )
    print(f"Сумма чисел в файле равна {round(s, 2)}")
except Exception as err:
    print(f"Ошибка: {err}")
