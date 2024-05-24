import time
import win32console, win32con
from console_display import ConsoleDisplay

display = ConsoleDisplay()

while True:
    display.clear()
    display.print('hell0!')
    #display.flip()