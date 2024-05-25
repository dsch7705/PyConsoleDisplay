import time, math
from console_display import ConsoleDisplay

display = ConsoleDisplay()
dT = 0

while True:
    pX = math.cos(dT) * display.width/2 + display.width/2 - 1  #rounding error required subtracting 1; TODO handle out-of-bounds coordinates
    pY = math.sin(dT) * display.height/2 + display.height/2
    dT += 0.1

    display.clear()
    display.print('hell0!')
    display.pixel(pX, pY, '#')
    display.flip()

    time.sleep(0.01)