class MinHeap:
    def __init__(self):
        self._min_heap = []

    def insert(self, value):
        self._min_heap.append(value)
        self.fix_heap(len(self._min_heap) - 1)

    def fix_heap(self, index_to_fix):
        if index_to_fix == 0:
            return

        parent_index = self.get_parent_index(index_to_fix)
        if self._min_heap[index_to_fix] < self._min_heap[parent_index]:
            self.swap_index_values(parent_index, index_to_fix)
            self.fix_heap(parent_index)

    def swap_index_values(self, first_ind, second_ind):
        self._min_heap[first_ind], self._min_heap[second_ind] = self._min_heap[second_ind], self._min_heap[first_ind]

    def get_parent_index(self, index):
        parent_index = index // 2
        return parent_index if parent_index < index / 2 else parent_index - 1

    def print_heap_by_levels(self, current_index=0, level=1, level_changed=True):
        if current_index >= len(self._min_heap):
            return
        last_index_in_level = (2 ** level) - 2
        last_node_in_level = last_index_in_level == current_index

        number_of_spaces = (self.get_heap_depth() - level)
        number_of_spaces += 1 if number_of_spaces > 0 else 0
        print_prefix = ' ' * number_of_spaces if level_changed else ''

        print(
            f"{print_prefix}{self._min_heap[current_index]} ",
            end='\n' if last_node_in_level else ''
        )

        next_level = level + 1 if last_node_in_level else level
        self.print_heap_by_levels(current_index + 1, next_level, next_level != level)

    def print_heap_as_array(self):
        print(self._min_heap)

    def get_heap_depth(self):
        depth = 0
        tree_len = len(self._min_heap)
        while tree_len > 0:
            depth += 1
            tree_len //= 2
        return depth



if __name__ == '__main__':
    heap_elements = [5, 1, 3, 5, 8, 9, 2, 10, 11, 20, 6, 0]
    my_heap = MinHeap()
    for elem in heap_elements:
        my_heap.insert(elem)
    my_heap.print_heap_as_array()
    my_heap.print_heap_by_levels()
