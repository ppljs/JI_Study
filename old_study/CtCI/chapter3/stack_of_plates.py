import sys
import os
sys.path.insert(0, os.getcwd())
from DataStructures.Stack import stack


class SetOfStacks:
    def __init__(self, max_size):
        self.curr_stack = stack.Stack()
        self.max_size = max_size
        self.stack_list = [self.curr_stack]
        self.curr_top_stack = 0

    def push(self, value):
        if self.curr_stack.length == self.max_size:
            self.curr_top_stack += 1
            self.curr_stack = stack.Stack()
            self.stack_list.append(self.curr_stack)

        self.curr_stack.push(value)

    def delete_a_stack(self, index):
        if self.curr_top_stack == 0:
                return None
        del self.stack_list[index]
        self.curr_top_stack -= 1
        self.curr_stack = self.stack_list[self.curr_top_stack]

    def pop(self):
        if self.curr_stack.is_empty():
            self.delete_a_stack(self.curr_top_stack)
            
        return self.curr_stack.pop()

    def pop_at(self, index):
        if index > self.curr_top_stack:
            return None

        if self.stack_list[index].is_empty():
            self.delete_a_stack(index)
            return None

        result = self.stack_list[index].pop()

        if self.stack_list[index].is_empty():
            self.delete_a_stack(index)

        return result


if __name__ == '__main__':
    sos = SetOfStacks(3)
    # Begining of the first stack
    sos.push(1)
    sos.push(2)
    sos.push(3)
    # Begining of the second stack
    sos.push(4)
    sos.push(5)
    sos.push(6)
    # Begining of the third stack
    sos.push(7)
    sos.push(8)
    sos.push(9)

    print(sos.pop())
    print(sos.pop_at(1))
    print(sos.pop_at(1))
    print(sos.pop_at(1))

    temp = sos.pop()
    while temp is not None:
        print(temp)
        temp = sos.pop()