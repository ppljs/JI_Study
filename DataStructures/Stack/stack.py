from DataStructures.LinkedList.linkedlist import LinkedNode


class Stack:
    def __init__(self):
        self.length = 0
        self._stack = None
    
    def push(self, value):
        if self._stack is None:
            self._stack = LinkedNode(value)
        else:
            tmp = LinkedNode(value)
            tmp.next = self._stack
            self._stack = tmp
        self.length += 1

    def pop(self):
        if self.is_empty():
            return None

        value = self._stack.value
        self._stack = self._stack.next

        return value

    def peek(self):
        return self._stack.value

    def is_empty(self):
        return bool(self._stack is None)
