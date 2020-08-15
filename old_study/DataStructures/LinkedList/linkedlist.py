class LinkedNode():
    def __init__(self, value):
        self.next = None
        self.value = value


class LinkedList():
    def __init__(self, value):
        self.node = LinkedNode(value)
        self.head = self.node
        self.tail = self.head

    def append(self, values):
        values = values if isinstance(values, list) else [values]
        for v in values:
            node = LinkedNode(v)
            self.tail.next = node
            self.tail = node

    def __str__(self):
        print_list = []
        curr_node = self.head
        while curr_node is not None:
            print_list.append(str(curr_node.value))
            curr_node = curr_node.next

        return ' -> '.join(print_list)

