'''ФАЙЛ МАКСИМА, СКРЫТЬ ПРОГРАММУ'''

import win32gui
import win32con

# получение дескриптора текущего окна
hwnd = win32gui.GetForegroundWindow()

# скрытие окно из списка активных задач
win32gui.ShowWindow(hwnd, win32con.SW_HIDE)