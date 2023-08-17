import pyAesCrypt
import os


# функция шифрования файла
def encryption(file, password):

    buffer_size = 512 * 1024   # размер буфера

    # вызов метода шифрования
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + '.crp',
        password,
        buffer_size
    )

    print(f'Файл {file} зашифрован')

    # удаление нешифрованной версии файла
    # os.remove(file)


def main_ecrp():
    # абсолютный путь к файлу
    file_name = 'system_monitoring.txt'
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, file_name)

    password = 'qwerty'

    # проверка на существование файла
    if os.path.exists(file_path):
        encryption(file_path, password)
    else:
        print(f'Файл {file_path} не найден')
