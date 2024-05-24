import time
import win32console, win32con
from console_display import ConsoleDisplay

b0 = win32console.CreateConsoleScreenBuffer(DesiredAccess = win32con.GENERIC_READ | win32con.GENERIC_WRITE, ShareMode=0, SecurityAttributes=None, Flags=1)
b1 = win32console.CreateConsoleScreenBuffer(DesiredAccess = win32con.GENERIC_READ | win32con.GENERIC_WRITE, ShareMode=0, SecurityAttributes=None, Flags=1)

display = ConsoleDisplay(b0, b1)
display.clear('A')
display.flip()
display.clear('B')

while True:
    display.flip()
    time.sleep(0.1)