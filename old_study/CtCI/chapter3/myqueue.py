import sys
import os
sys.path.insert(0, os.getcwd())
from DataStructures.Stack.stack import Stack
from enum import Enum


class State(Enum):
    REMOVE = 1
    INSERT = 2

class Transition(Enum):
    R_I = 0
    I_R = 1

class MyQueue:
    def __init__(self):
        self.insertStack = Stack()
        self.removeStack = Stack()
        self.state = State.INSERT
    
    def insert(self, value):
        if self.state == State.REMOVE:
            self.change_states(Transition.R_I)

        self.insertStack.push(value)

    def remove(self):
        if self.state == State.INSERT:
            self.change_states(Transition.I_R)
        
        if self.removeStack.is_empty():
            return None

        return self.removeStack.pop()

    def change_states(self, transition):
        if transition == Transition.R_I:
            to_remove_stack = self.removeStack
            to_insert_stack = self.insertStack
            self.state = State.INSERT
        else:
            to_remove_stack = self.insertStack
            to_insert_stack = self.removeStack
            self.state = State.REMOVE
            
        while not to_remove_stack.is_empty():
            value = to_remove_stack.pop()
            to_insert_stack.push(value)


if __name__ == "__main__":
    my_queue = MyQueue()
    my_queue.insert(1)
    my_queue.insert(2)
    my_queue.insert(3)
    my_queue.insert(4)

    print(my_queue.remove())
    my_queue.insert(5)
    print(my_queue.remove())
    my_queue.insert(6)
    value = my_queue.remove()
    while value is not None:
        print(value)
        value = my_queue.remove()