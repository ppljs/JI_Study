from collections import deque
from copy import copy

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def __hash__(self):
        return hash(f"{self.weight}|{self.value}")
    
    def __eq__(self, other):
        return self.weight == other.weight and self.value == other.value

    def __repr__(self):
        return f"{self.weight}|{self.value}"


def get_most_valuable_items_combination(items, max_weight):
    items = set(items)
    max_value = _get_items(items, max_weight, {})
    return max_value

    
def _get_items(items, available_weight, memory):
    if available_weight in memory:
        return memory[available_weight]

    if available_weight == 0:
        return 0

    max_value = 0
    for item in items:
        if item.weight <= available_weight:
            value = item.value
            curr_value = _get_items(items - {item}, available_weight - item.weight, memory)
            value += curr_value
            if value > max_value:
                max_value = value

    memory[available_weight] = max_value
    return max_value


if __name__ == '__main__':
    items = [
        Item(5, 100),
        Item(3, 55),
        Item(4, 80),
        Item(1, 20),
    ]
    print(get_most_valuable_items_combination(items, 10))