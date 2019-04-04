class Stack:
    def __init__(self):
        self.length = 0
        self._top = -1
        self._stack = []
    
    def add(self, value):
        self._stack.append(value)
        self._top += 1
        self.length += 1

    def pop(self):
        value = self._stack.pop(self._top)
        self._top -= 1
        self.length -= 1
        return value
