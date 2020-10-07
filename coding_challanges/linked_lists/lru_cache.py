# In a real LRU Cache the value would be the key and the search would return the real data associated with the key

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class MyDeque:
    def __init__(self):
        self._start = None
        self._end = None
        self._len = 0

    def __len__(self):
        return self._len

    def __repr__(self):
        curr = self._start
        values = []
        while curr:
            values.append(str(curr.value))
            curr = curr.right
        return ' -> '.join(values)
    
    def appendleft(self, value):
        node = Node(value, right=self._start)
        if self._len:
            self._start.left = node
        else:
            self._end = node
        self._start = node
        
        self._len += 1
        return node

    def remove(self, node):
        if self._len == 0:
            return

        if node is self._start:
            self._start.right.left = None
            self._start = self._start.right
        elif node is self._end:
            self._end.left.right = None
            self._end = self._end.left
        else:
            node.left.right = node.right
            node.right.left = node.left
        
        self._len -= 1

    def pop(self):
        self._end.left.right = None
        self._end, poped_value = self._end.left, self._end.value
        self._len -= 1
        return poped_value


class LruCache:
    def __init__(self, maxlen):
        self._maxlen = maxlen
        self._cache = MyDeque()
        self._value_to_ref = {}
    
    def search(self, value):
        if value in self._value_to_ref:
            self._remove_value(value)
        else:
            if len(self._cache) >= self._maxlen:
                self._pop_lru()
        
        self._append_most_recently_used(value)
        return value
    
    def _remove_value(self, value):
        node_ref = self._value_to_ref.pop(value)
        self._cache.remove(node_ref)

    def _pop_lru(self):
        node_value = self._cache.pop()
        self._value_to_ref.pop(node_value)

    def _append_most_recently_used(self, value):
        node_ref = self._cache.appendleft(value)
        self._value_to_ref[value] = node_ref

        

    def __repr__(self):
        return str(self._cache)

items = [1,2,3,4,5,3,6,6]
maxlen = 5
cache = LruCache(maxlen)
for item in items:
    print(cache)
    cache.search(item)

print(cache)
