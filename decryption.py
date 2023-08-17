import pyAesCrypt
import os


# функция дешифровки файла
def decryption(file, password):

    buffer_size = 512 * 1024   # размер буфера

    # вызов метода дешифровки
    pyAesCrypt.decryptFile(
        str(file),
        str(str(os.path.splitext(file)[0])),
        password,
        buffer_size
    )

    print(f"Файл {file} расшифрован")

    # удаление нешифрованной версии файла
    os.remove(file)


def main_dcrp():

    # абсолютный путь к файлу
    file_name = 'system_monitoring.txt.crp'
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, file_name)

    password = 'qwerty'

    # проверка на существование файла
    if os.path.exists(file_path):
        decryption(file_path, password)
    else:
        print(f'Файл {file_path} не найден.')

