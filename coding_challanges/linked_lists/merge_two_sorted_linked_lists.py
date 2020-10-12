# https://leetcode.com/problems/merge-two-sorted-lists/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if not l1 and not l2:
        return None
    elif not l1:
        return l2
    elif not l2:
        return l1

    result = None
    if l1.val < l2.val:
        result, l1 = l1, l1.next
    else:
        result, l2 = l2, l2.next
    start = result
    
    while l1 or l2:
        if l1 and l2:
            if l1.val < l2.val:
                result.next, l1 = l1, l1.next
            else:
                result.next, l2 = l2, l2.next
        elif l1:
            result.next, l1 = l1, l1.next
        else:
            result.next, l2 = l2, l2.next
        
        result = result.next
            
    return start