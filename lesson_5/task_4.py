"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую 
построчно данные. При этом английские числительные должны заменяться 
на русские. Новый блок строк должен записываться в новый текстовый файл.
"""
try:
    output_box = {
        1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять",
        6: "шесть", 7: "семь", 8: "восемь", 9: "девять"
    }
    with open('task_4_text.txt') as fr:
        with open('task_4_result.txt', 'w', encoding='utf-8') as fw:
            for row in fr:
                _, str_number = row.split(" - ")
                _number = int(str_number)
                fw.write(f'{output_box[_number].capitalize()} - {_number}\n')
except Exception as err:
    print(f"Ошибка: {err}")
