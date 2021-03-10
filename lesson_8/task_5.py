"""
5. Продолжить работу над заданием 4. Разработать методы, отвечающие за приём 
оргтехники на склад и передачу в определенное подразделение компании. Для хранения 
данных о наименовании и количестве единиц оргтехники, а также других данных, 
можно использовать любую подходящую структуру, например словарь.
"""

from lesson_8.task_4 import WareHouse, Equipment, Printer, Scaner, Xerox
from typing import List


class NewWareHouse(WareHouse):
    def take_to_warehouse(self, equip: Equipment):
        self.update(equip)

    def get_list_type_equipments(self, types: str) -> List:
        _lst = self.get(types)
        if not _lst:
            raise TypeError('Такого типа оборудования на складе нет')
        return _lst

    def transfer_to_division(self, inv_number: str, department: str) -> Equipment:
        for _, equip_list in self.items():
            for eq in equip_list:
                _equal = None
                if eq.inventory_number == inv_number:
                    _equal = eq
                    break
        if not _equal:
            raise ValueError(f'Оборудование с инв.№ {inv_number} нет на складе')
        _text = f'{_equal} выдано в подразделение {department}'
        with open('lesson_8/report.txt', 'a') as file:
            file.write(_text + '\n')
        return _text


if __name__ in "__main__":
    pass
    warehouse = NewWareHouse('Обитель техники')
    data = (
        (Printer, 'Canon', 'LBP-2900', 'P01 UTIL'),
        (Printer, 'HP', 'ISENSYS-01', 'P01'),
        (Scaner, 'HP', 'GOD666', 'S01'),
        (Scaner, 'Laserjet', 'LBP-2900', 'S02'),
        (Xerox, 'Digma', 'BUILD5', 'X01 PRO'),
        (Xerox, 'Apple', 'M54', 'X02')
    )
    for obj, *args in data:
        warehouse.take_to_warehouse(obj(*args))
    print(warehouse.transfer_to_division(
        inv_number='X01 PRO', department='Бухи'
    ))

"""
Результат выполнения:

Мусор на складе не хранят! Printer Canon LBP-2900 в утиль!
Xerox Digma BUILD5 выдано в подразделение Бухи
"""
