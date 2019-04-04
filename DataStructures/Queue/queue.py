from DataStructures.LinkedList.linkedlist import LinkedNode


class Queue:
    def __init__(self):
        self._queue = None
        self._tail = None
        self.length = 0

    def add(self, value):
        if self._queue is None:
            self._queue = LinkedNode(value)
            self._tail = self._queue
        else:
            self._tail.next = LinkedNode(value)
            self._tail = self._tail.next
        
        self.length += 1

    def remove(self):
        if self.is_empty():
            return None

        r_item = self._queue.value
        self._queue = self._queue.next
        self.length -= 1

        return r_item

    def peek(self):
        return self._queue.value

    def is_empty(self):
        return bool(self._queue is None)

