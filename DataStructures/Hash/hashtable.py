

class HashLinkedList():
    def __init__(self, key, value):
        self.next = None
        self.key = key
        self.value = value
        self.collision_num = 0

    def append(self, key, value):
        curr_link = self
        while True:
            if curr_link.key == key:
                curr_link.value = value
                break
            elif curr_link.next is None:
                curr_link.next = HashLinkedList(key, value)
                self.collision_num += 1
                break
            curr_link = curr_link.next

    def search(self, key):
        curr_link = self
        while True:
            if curr_link is None:
                break

            if curr_link.key == key:
                return self
            curr_link = curr_link.next
        
        return None

    def del_key(self, key, index, hash_obj):
        curr_link = self
        if curr_link.next is None:
            if curr_link.key == key:
                hash_obj._set_index_after_del(index, None)
                return False
            else:
                return True
        else:
            if curr_link.key == key:
                curr_link.next.collision_num = curr_link.collision_num
                hash_obj._set_index_after_del(index, curr_link.next)
                return False

        while True:
            if curr_link.next.key == key:
                if curr_link.next.next is None:
                    curr_link.next = None
                else:
                    curr_link.next = curr_link.next.next
                hash_obj.collision_num -= 1
                return False
            elif curr_link.next.next is None:
                break
            else:
                curr_link = curr_link.next

        return True


class HashTable:
    def __init__(self, table_size=100):
        self.table_size = table_size
        self.hash_table = [None] * table_size
        self.collision_num = 0


    def hash(self, key):
        if isinstance(key, int):
            index = key
        else:
            index = 0
            if isinstance(key, float):
                key = str(key)
            for i, character in enumerate(key):
                index += (ord(character) * i)
            
        return index % self.table_size

    def _set_index_after_del(self, index, linked_list):
        self.hash_table[index] = linked_list
        self.collision_num -= 1

    def add(self, key, value):
        index = self.hash(key)
        if self.hash_table[index] is None:
            self.hash_table[index] =  HashLinkedList(key, value)
        else:
            before_col = self.hash_table[index].collision_num
            self.hash_table[index].append(key, value)
            self.collision_num += 1 if self.hash_table[index].collision_num - before_col != 0 else 0
    
    def get_value(self, key):
        result = None
        index = self.hash(key)
        if self.hash_table[index] is not None:
            result = self.hash_table[index].search(key)
        
        if result is None:
            raise KeyError(f'Mapping key not found: {key}')
        
        return result.value

    def del_key(self, key):
        index = self.hash(key)
        will_raise = False
        if self.hash_table[index] is not None:
            will_raise = self.hash_table[index].del_key(key, index, self)
        else:
            will_raise = True

        if will_raise:
            raise KeyError(f'Mapping key not found for delete opperation. Key: {key}')

    def print_structure(self):
        for i in range(self.table_size):
            print(f'index = {i}')
            if self.hash_table[i] is not None:
                    curr_link = self.hash_table[i]
                    while True:
                        print(f'\t{curr_link.key} : {curr_link.value}')
                        if curr_link.next is None:
                            break
                        curr_link = curr_link.next
            else:
                print('\tNone')
        print(f'\nCollisions number = {self.collision_num}\n')

if __name__ == '__main__':
    my_dict = HashTable(table_size=10)
    my_dict.add('aspects', 12)
    my_dict.add('this is a test', 100)
    my_dict.add('hello helo11', -89)
    my_dict.add('helldjove', -89)
    my_dict.add('helldjove', 0)
    my_dict.print_structure()
    print(my_dict.get_value(key='aspects'))
    

