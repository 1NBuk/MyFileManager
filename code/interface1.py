from main import *
# -*- coding: utf-8 -*-
print('Введите команду или введите help для подсказки. Напишите exit, чтобы выйти.')
command = []
while True:
    command = input().split(' ')
    if command[0].lower() == 'exit':
        print('Выход...')
        break
    try:
        if command[0] in all_commands:
            f1 = all_commands[command[0]]
            f2 = []
            for i in command[1:]:
                f2.append(i)
            print(all_commands[command[0]](*f2))

    except:
        print('Вы ввели что-то не из списка')
