class Node:
    def __init__(self, value, next_node=None, next_smaller=None):
        self.value = value
        self.next = next_node
        self.next_smaller = next_smaller

class MinStack:
    def __init__(self):
        self._stack_top = None
        self._smaller = None

    def push(self, x: int) -> None:
        new_top = Node(x, next_node=self._stack_top)
        if not self._smaller or self._smaller.value > x:
            new_top.next_smaller = self._smaller
            self._smaller = new_top
        
        self._stack_top = new_top 

    def pop(self):
        if self._stack_top is self._smaller:
            self._smaller = self._smaller.next_smaller
            
        self._stack_top = self._stack_top.next

    def top(self) -> int:
        return self._stack_top.value

    def getMin(self) -> int:
        return self._smaller.value
