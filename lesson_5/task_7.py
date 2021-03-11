"""
7. Создать (не программно) текстовый файл, в котором каждая строка 
должна содержать данные о фирме: название, форма собственности, 
выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой 
компании, а также среднюю прибыль. Если фирма получила убытки, 
в расчет средней прибыли ее не включать.

Далее реализовать список. 
Он должен содержать словарь с фирмами и их прибылями, а также 
словарь со средней прибылью. Если фирма получила убытки, также 
добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
from collections import namedtuple
from typing import List, Tuple, List
import json


firm_data = namedtuple('Firma', 'name form revenue costs')


def check_profit(firma: firm_data) -> Tuple[str, float, bool]:
    """Функция проверяет наличие прибыли в фирме и возвращает кортеж:
    (название фирмы, размер прибыли, прибыль=True) - если прибыль есть;
    (название фирмы, размер убытков, прибыль=False) - если прибыли нет"""
    r = round(float(firma.revenue) - float(firma.costs), 2)
    return (firma.name, r, True) if r > 0 else (firma.name, abs(r), False)


def get_average_firm_with_revenue(data: List[firm_data]) -> float:
    """Расчёт средней прибыли по списку фирм"""
    firms_with_revenue = [x for x in dataset if check_profit(x)[2]]
    return round(sum(map(lambda obj: check_profit(obj)[1],
                         firms_with_revenue)) / len(firms_with_revenue), 2)


if __name__ == '__main__':
    try:
        with open('task_7_text.txt') as fr:
            dataset = [firm_data(*data.split()) for data in fr.readlines()]
        result = [dict([check_profit(obj)[:2] for obj in dataset]),
                  {"average_profit": get_average_firm_with_revenue(dataset)}]
        with open('task_7_result.json', 'w', encoding='utf-8') as fw:
            json.dump(result, fw)
    except Exception as err:
        print(f"Ошибка: {err}")
