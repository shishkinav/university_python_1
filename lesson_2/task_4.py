"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. 
Вывести каждое слово с новой строки. Строки нужно пронумеровать. 
Если слово длинное, выводить только первые 10 букв в слове.
"""
import string


_sentence = input("Введите строку из нескольких слов разделенных пробелами:\n")
_words = "".join([simbol for simbol in _sentence if simbol not in string.punctuation])
for i, word in enumerate(_words.split(), 1):
    print(f"{i:>3} {word[:10].lower()}")

"""
Результат выполнения:

Введите строку из нескольких слов разделенных пробелами:
>Тип данных: множество - это контейнер с неповторяющимися элементами, 
>расположенными в случайном порядке. Множество, создаваемое с помощью 
>функции set(), представляет собой изменяемый тип данных, 
>frozenset() - неизменяемый.

  1 тип
  2 данных
  3 множество
  4 это
  5 контейнер
  6 с
  7 неповторяю
  8 элементами
  9 расположен
 10 в
 11 случайном
 12 порядке
 13 множество
 14 создаваемо
 15 с
 16 помощью
 17 функции
 18 set
 19 представля
 20 собой
 21 изменяемый
 22 тип
 23 данных
 24 frozenset
 25 неизменяем
"""