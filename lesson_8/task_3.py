"""
3. Создайте собственный класс-исключение, который должен проверять 
содержимое списка на наличие только чисел. Проверить работу исключения 
на реальном примере. Необходимо запрашивать у пользователя данные и 
заполнять список. Класс-исключение должен контролировать типы данных 
элементов списка.

Примечание: длина списка не фиксирована. Элементы запрашиваются 
бесконечно, пока пользователь сам не остановит работу скрипта, введя, 
например, команду “stop”. При этом скрипт завершается, сформированный 
список выводится на экран.

Подсказка: для данного задания примем, что пользователь может вводить 
только числа и строки. При вводе пользователем очередного элемента 
необходимо реализовать проверку типа элемента и вносить его в список, 
только если введено число. Класс-исключение должен не позволить 
пользователю ввести текст (не число) и отобразить соответствующее 
сообщение. При этом работа скрипта не должна завершаться.
"""

class CheckNumberException(Exception):
    @classmethod
    def check_value(cls, number: str):
        try:
            n = float(number)
            return n
        except ValueError:
            raise cls('Ожидается ввод числа, а не текста!')


class Iterator:
    """Объект-итератор"""
    def __init__(self):
        self.iteration = True
        self.lst = []

    def __iter__(self):
        return self

    def __next__(self):
        number = input('Введите число:\n')
        if number == 'stop':
            self.iteration = False
        if self.iteration:
            try:
                number = CheckNumberException.check_value(number)
                self.lst.append(number)
                return number
            except CheckNumberException as err:
                print(err)
        else:
            raise StopIteration
        
        
if __name__ in "__main__":
    _iter = Iterator()
    [_ for _ in _iter]
    print(_iter.lst)

"""
Результат выполнения:

Введите число:
> 1
Введите число:
> 50.01
Введите число:
> привет
Ожидается ввод числа, а не текста!
Введите число:
> stop
[1.0, 50.01]
"""
