import sys
import os
sys.path.insert(0, os.getcwd())
from DataStructures.LinkedList import linkedlist


# There are multiple ways of solving this problem. I will solve it in two different scenarios, one where I have the length of the linked list
# and the other where I do not have it.


class ReturnWrapper:
    def __init__(self, node, success):
        self.node = node
        self.success = success


# In this case, I do not have access to the length of the linked list, so I do duplicated work and stack my recursive function more
# than what was really necessary.
def is_list_palindrome(head, mov_head):
    if mov_head is None:
        return ReturnWrapper(head, True)

    ret_wrapper = is_list_palindrome(head, mov_head.next)
    if ret_wrapper.success:
        if ret_wrapper.node.value == mov_head.value:
            ret_wrapper.node = ret_wrapper.node.next
            return ret_wrapper
        else:
            ret_wrapper.success = False
            return ret_wrapper
    else:
        return ret_wrapper


# This is the case where I know the length of the list, so I am able to avoid the unnecessary function stacking and duplicated work
def is_list_palindrome_length(head, half_length, is_odd):
    if half_length == 0:
        if is_odd:
            return ReturnWrapper(head.next, True)
        else:
            return ReturnWrapper(head, True)

    half_length -= 1
    ret_wrapper = is_list_palindrome_length(head.next, half_length, is_odd)
    if ret_wrapper.success:
        if ret_wrapper.node.value == head.value:
            ret_wrapper.node = ret_wrapper.node.next
            return ret_wrapper
        else:
            ret_wrapper.success = False
            return ret_wrapper
    else:
        return ret_wrapper


if __name__ == '__main__':
    lk = linkedlist.LinkedList('a')
    lk.append(['a', 'f', 'b', 'f', 'a', 'a'])
    half_length = 7 // 2
    is_odd = True
    print('is_palindrome (with length) =',is_list_palindrome_length(lk.head, half_length, is_odd).success)
    print('is_palindrome =',is_list_palindrome(lk.head, lk.head).success)
