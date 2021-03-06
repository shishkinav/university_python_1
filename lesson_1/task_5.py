"""
5. Запросите у пользователя значения выручки и издержек фирмы. 
Определите, с каким финансовым результатом работает фирма 
(прибыль — выручка больше издержек, или убыток — издержки больше выручки). 
Выведите соответствующее сообщение. Если фирма отработала с прибылью, 
вычислите рентабельность выручки (соотношение прибыли к выручке). 
Далее запросите численность сотрудников фирмы и определите 
прибыль фирмы в расчете на одного сотрудника.
"""
import sys


global revenue
global costs

try:
    revenue = float(input("Введите сумму прибыли:\n"))
    costs = float(input("Введите сумму издержек:\n"))
except Exception as err:
    print("Допустимо введение суммы, состоящей только из цифр "
        "+ возможно указать копейки через 'плавающую' точку. "
        f"example: 1234.99\nОшибка: {err}")
    sys.exit()

if revenue < costs:
    print("Издержки больше выручки. Пора на покой.")
elif revenue == costs:
    print("Работаем в ноль. Пора наверное провести Вам аудит.")
else:
    print("Выручка больше издержек")
    print("Рентабельность выручки (соотношение прибыли к выручке): %.2f %%" % (revenue / costs * 100))
    while True:
        try:
            _count_worker = int(input("Сколько человек в фирме?\n"))
            print("В расчёте на одного сотрудника чистой прибыли получается:\n"
                "%.2f рублей" % ((revenue - costs) / _count_worker))
            break
        except Exception as err:
            print(f"Необходимо ввести целое положительное число!\nОшибка: {err}")

"""
Результат выполнения выглядит следующим образом:

Введите сумму прибыли:
>198743.99
Введите сумму издержек:
>36855.08
Выручка больше издержек
Рентабельность выручки (соотношение прибыли к выручке): 539.26 %
Сколько человек в фирме?
>15
В расчёте на одного сотрудника чистой прибыли получается:
10792.59 рублей
"""