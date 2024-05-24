import win32console, win32con

class ConsoleDisplay:
    def __init__(self):
        b0 = win32console.CreateConsoleScreenBuffer(DesiredAccess = win32con.GENERIC_READ | win32con.GENERIC_WRITE, ShareMode=0, SecurityAttributes=None, Flags=1)
        b1 = win32console.CreateConsoleScreenBuffer(DesiredAccess = win32con.GENERIC_READ | win32con.GENERIC_WRITE, ShareMode=0, SecurityAttributes=None, Flags=1)
        self.buffers = [b0, b1]
        self.active_buffer = 0
        self.back_buffer = 1

        self.buffers[self.active_buffer].SetConsoleActiveScreenBuffer()

    def flip(self):
        self.active_buffer = abs(self.active_buffer - 1)
        self.back_buffer = abs(self.back_buffer - 1)

        self.buffers[self.active_buffer].SetConsoleActiveScreenBuffer()

    def fill(self, c):
        buff = self.buffers[self.back_buffer]
        buffSize = buff.GetConsoleScreenBufferInfo()['Size'].X * buff.GetConsoleScreenBufferInfo()['Size'].Y

        buff.FillConsoleOutputCharacter(c, buffSize, win32console.PyCOORDType(0, 0))

    def clear(self):
        self.fill(' ')

    def print(self, str):
        buff = self.buffers[self.back_buffer]

        buff.WriteConsoleOutputCharacter(str, win32console.PyCOORDType(0, 0))
        