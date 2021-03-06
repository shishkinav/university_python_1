"""
3. Создать текстовый файл (не программно), построчно записать фамилии 
сотрудников и величину их окладов. Определить, кто из сотрудников имеет 
оклад менее 20 тыс., вывести фамилии этих сотрудников. 
Выполнить подсчет средней величины дохода сотрудников.
"""

with open('task_3_text.txt') as fr:
    s = 0
    for idx, row in enumerate(fr, 1):
        last_name, balance = row.split()
        if float(balance) < 20000:
            print(f'{last_name} оклад менее 20К')
        s += float(balance)
    print(f'Средняя величина дохода по сотрудникам {round(s / idx, 2)}')

"""
Результат выполнения:
> python task_3.py 
Петров оклад менее 20К
Панчук оклад менее 20К
Петросян оклад менее 20К
Мишкин оклад менее 20К
Средняя величина дохода по сотрудникам 25608.26
"""