'''ФАЙЛ КОСТИН, ПО СОЗДАНИЮ КЕЙЛОГЕРА и сохранения в файл'''
from pynput import keyboard
import ctypes


class LangDetected:
    """Определение языка Раскладки Клавиатуры"""
    def keyboard_layaout(self):
        # хндл главного окна
        hwnd = ctypes.windll.user32.GetForegroundWindow()
        # нить исполняемого данного окна ID
        nitya_id = ctypes.windll.user32.GetWindowThreadProcessId(hwnd, None)
        # хндл нити
        hndl_nit = ctypes.windll.user32.GetKeyboardLayout(nitya_id)

        # id языка
        lang_id = hndl_nit & 0xFFFF
        return lang_id

    def manifest_lang(self):
        lang_layaout = self.keyboard_layaout()

        # словарь кодов для раскладок
        dict_lang = {
            0x0409: "US",
            0x0419: "RU"
        }

        current_lang = dict_lang.get(lang_layaout, 'Error')
        return current_lang















