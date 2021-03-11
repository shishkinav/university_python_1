"""
1. Создать программно файл в текстовом формате, записать в него 
построчно данные, вводимые пользователем. Об окончании ввода 
данных свидетельствует пустая строка.
"""
with open('task_1_result.txt', 'w', encoding='utf-8') as file:
    while True:
        row_from_user = input("Введите строку для записи, "
                              "либо оставьте строку пустой для остановки:\n")
        if not row_from_user:
            break
        file.write(f'{row_from_user}\n')
