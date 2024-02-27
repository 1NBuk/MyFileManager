# -*- coding: utf-8 -*-
from main import *

i1 = 0
while i1 != 13:
    try:
        print('Возможности файлового менеджера:')
        print("1) Создание папки (с указанием имени)\n2) Удаление папки по имени\n3) Перемещение между папками (в пределах рабочей папки) - заход в папку по имени, выход на уровень вверх\n4) Создание пустых файлов с указанием имени\n5) Запись текста в файл\n6) Просмотр содержимого текстового файла\n7) Удаление файлов по имени\n8) Копирование файлов из одной папки в другую\n9) Перемещение файлов\n10) Переименование файлов\n11) Архивация файлов и папок\n12) Разархивация файлов и папок\n13) Выход")
        i1 = int(input('Введите цифру: '))
        if i1 == 1:
            name = input('Введите название папки: ')
            print(create_dir(name))
        if i1 == 2:
            name = input('Введите название папки: ')
            print(delete_dir(name))
        if i1 == 3:
            folder_name = input('Введите название папки (/ попасть в корневую, .. выход на уровень вверх): ')
            print(change_directory(folder_name))
        if i1 == 4:
            name = input('Введите название файла: ')
            print(create_file(name))
        if i1 == 5:
            name = input('Введите название файла: ')
            text = input('Введите текст: ')
            print(write_file(name, text))
        if i1 == 6:
            name = input('Введите название файла: ')
            print(prosmotr_file(name))
        if i1 == 7:
            name = input('Введите название файла: ')
            print(delete_file(name))
        if i1 == 8:
            name = input('Введите название файла: ')
            new_dir = input('Введите название папки: ')
            print(copy_file(name, new_dir))
        if i1 == 9:
            name = input('Введите название файла: ')
            new_dir = input('Введите название папки: ')
            print(move_file(name, new_dir))
        if i1 == 10:
            name = input('Введите старое название файла: ')
            new_name = input('Введите новое название файла: ')
            print(rename_file(name, new_name))
        if i1 == 11:
            name = input('Введите путь, по которому будет создан архив: ')
            dir = input('Введите путь к директории, которую нужно архивировать: ')
            print(create_archive(name, dir))
        if i1 == 12:
            name = input('Введите путь к архиву: ')
            dir = input('Введите путь, по которому будет разархивирован архив: ')
            print(razarchive(name, dir))
        if i1 == 13:
            print('Выход...')
            break
    except:
        print('Вы ввели что-то не из списка')


