import win32console, win32con

class ConsoleDisplay:
    def __init__(self, front_buffer, back_buffer):
        self.buffers = [front_buffer, back_buffer]
        self.active_buffer = 0

        self.buffers[self.active_buffer].SetConsoleActiveScreenBuffer()

    def flip(self):
        self.active_buffer = abs(self.active_buffer - 1)
        self.buffers[self.active_buffer].SetConsoleActiveScreenBuffer()

    def clear(self, c):
        buff = self.buffers[self.active_buffer]
        buffSize = buff.GetConsoleScreenBufferInfo()['Size'].X * buff.GetConsoleScreenBufferInfo()['Size'].Y

        buff.FillConsoleOutputCharacter(c, buffSize, win32console.PyCOORDType(0, 0))
        