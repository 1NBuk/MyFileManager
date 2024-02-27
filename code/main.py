import os
import shutil
import nastroiki

raboch_dir = nastroiki.korn_dir

def create_dir(name): #Создание папки
    try:
        os.chdir(raboch_dir)#изменение текущей рабочей директории
        os.mkdir(os.path.join(raboch_dir, name))
        return 'Папка создана'
    except FileExistsError:
        return 'Папка с таким именем уже существует'

def delete_dir(name):
    try:
        if os.path.join(raboch_dir, name) != raboch_dir:
            os.rmdir(os.path.join(raboch_dir, name))
            return 'Папка удалена'
        else:
            return 'Вы хотите удалить папку в которой находитесь'
    except FileNotFoundError:
        return 'Такой папки не существует'
    except OSError:
        try:
            print('В этой папке есть файлы')
            o1 = int(input('Всё равно удалить?\n1)Да 2)Нет\n'))
            if o1 == 1:
                shutil.rmtree(os.path.join(raboch_dir, name))#для удаления директории вместе со всем ее содержимым
                return 'Папка удалена'
        except FileNotFoundError:
            return 'Такой папки не существует'

def change_directory(folder_name):
    global raboch_dir
    if folder_name == "..":
        a = os.path.dirname(os.getcwd()) #директория на один уровень выше
        if a != os.path.dirname(nastroiki.korn_dir):
            raboch_dir = os.path.dirname(raboch_dir)
            os.chdir("..")  #os.chdir("../..") на два
        else:
            return "Вы хотите выйти за пределы корневой директории"
    elif folder_name == "/":#в корневую
        raboch_dir = nastroiki.korn_dir#os.path.dirname(raboch_dir)
        os.chdir(raboch_dir)
    else:
        new_path = os.path.join(raboch_dir, folder_name)
        if os.path.exists(new_path) and os.path.isdir(new_path):
            raboch_dir = new_path
            os.chdir(raboch_dir)
    return f"Текущая рабочая папка: {raboch_dir}"

def create_file(name):
    if name not in os.listdir():#для получения списка всех файлов и папок
        open(os.path.join(raboch_dir, name), 'w').close()
        return 'Файл создан'
    else:
        return 'Файл с таким именем уже существует'

def write_file(name, text=None):
    w1 = int(input('Введите цифру 1 или 2:\n1)Перезаписать текст\n2)Добавить текст\n'))
    try:
        if w1 == 1:
            with open(name, 'w', encoding='utf-8') as f1:
                f1.write(text)
                return 'Текст записался в файл'
        if w1 == 2:
            with open(name, 'a', encoding='utf-8') as f1:
                f1.write('\n' + text)
                return 'Текст добавился в файл'
    except:
        return 'Вы ввели что-то не из списка'

def prosmotr_file(name):
    try:
        with open(os.path.join(raboch_dir, name), 'r') as f2:
            return f2.read()
    except FileNotFoundError:
        return 'Файла с таким именем не существует'

def delete_file(name):
    try:
        os.remove(os.path.join(raboch_dir, name))
        return 'Файл удален'
    except FileNotFoundError:
        return 'Файла с таким именем не существует'

def copy_file(name, new_dir):
    try:
        if '/' in name:
            first = os.path.join(raboch_dir, name)
            second = os.path.join(raboch_dir, new_dir, os.path.basename(name))#basename() возвращает последний компонент строки пути
            shutil.copyfile(first, second)
            return 'Файл скопирован'
        else:
            first = os.path.join(raboch_dir, name)
            second = os.path.join(raboch_dir, new_dir)
            shutil.copyfile(first, second)
            return 'Файл перемещён'
    except:
        return 'Файла с таким именем не существует или нет такой папки'


def move_file(name, new_dir):
    try:
        if '/' in name:
            first = os.path.join(raboch_dir, name)
            second = os.path.join(raboch_dir, new_dir, os.path.basename(name))
            shutil.move(first, second)
            return 'Файл перемещён'

        else:
            first = os.path.join(raboch_dir, name)
            second = os.path.join(raboch_dir, new_dir)
            shutil.move(first, second)
            return 'Файл перемещён'

    except:
        return 'Файла с таким именем не существует или нет такой папки'

def rename_file(name, new_name):
    try:
        first = os.path.join(raboch_dir, name)
        second = os.path.join(raboch_dir, new_name)
        os.rename(first, second)
        return 'Файл переименован'
    except FileNotFoundError:
        return 'Файла с таким именем в этой папке не существует'

#dir - путь к директории, которую нужно архивировать
#name - путь, по которому будет создан архив
def create_archive(name, dir):
    try:
        shutil.make_archive(name, 'zip', dir)
        return "Архив создан"
    except:
        return "Архив не создан"

#name - путь к архиву
#dir - путь, по которому будет разархивирован архив
def razarchive(name, dir):
    try:
        shutil.unpack_archive(name, dir)
        return "Архив разархивирован"
    except:
        return "Архив не разархивирован"

def help():
    return "1)mkdir name: Создание папки (с указанием имени)\n2)rmdir: Удаление папки по имени\n3)cd: Перемещение между папками (в пределах рабочей папки) - заход в папку по имени, выход на уровень вверх\n4)touch: Создание пустых файлов с указанием имени\n5)write name text: Запись текста в файл\n6)cat: Просмотр содержимого текстового файла\n7)rm: Удаление файлов по имени\n8)cp name new_dir: Копирование файлов из одной папки в другую\n9)mv name new_dir: Перемещение файлов\n10)rename name new_name: Переименование файлов\n11)zip name dir: Архивация файлов и папок\n12)unzip name dir: Разархивация файлов и папок"


all_commands = {'mkdir':create_dir, 'rmdir': delete_dir, 'cd':change_directory,
                'touch':create_file,
                'write':write_file,
                'cat':prosmotr_file,
                'rm':delete_file,
                'cp':copy_file,
                'mv': move_file,
                'rename':rename_file,
                'zip':create_archive,
                'unzip':razarchive,
                'help':help}

#print(create_dir('dir1'))
#print(delete_dir('dir1'))
#print(change_directory('dir2'))
#print(change_directory('dir1.1'))
#print(change_directory('/'))
#print(change_directory('..'))
#print(change_directory('..'))
#print(create_file('file3'))
#print(write_file('file3', 'Hello'))
#print(prosmotr_file('file'))
#print(delete_file('file2'))
#print(copy_file('dir2/file1', 'dir1'))
#print(move_file('file1', 'dir1'))
#print(rename_file('file', 'file3'))
#print(create_archive('dir2', 'dir1'))
#print(razarchive('a2.zip', 'dir1'))
