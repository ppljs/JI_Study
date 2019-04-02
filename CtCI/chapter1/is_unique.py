def is_unique_brute(curr_string):
    i = 0
    while i < len(curr_string):
        j = i + 1
        while j < len(curr_string):
            if curr_string[i] == curr_string[j]:
                return False

    return True


def is_unique_sort(curr_string):
    curr_string = [c for c in curr_string]
    curr_string.sort()
    for i in range(0, len(curr_string) - 1):
        if curr_string[i] == curr_string[i + 1]:
            return False

    return True


# With O(n) but with a data structure to help
def is_unique_fast(curr_string):
    # Assuming we are working with ASCII characters
    checker = [False] * 256
    for c in curr_string:
        if checker[ord(c)] == True:
            return False
        else:
            checker[ord(c)] = True
    
    return True


# This has O(n) of time complexity and O(1) of space complexity
# If you want to make this work for longer characters encodings, just make the size of the integer bigget like a long int
def is_unique_best(curr_string):
    checker = 0
    if len(curr_string) > 256:
        return False

    for c in curr_string:
        curr_1_index = ord(c) - ord('a')
        curr_onehot = 1 << curr_1_index
        if (checker & curr_onehot) > 0:
            return False
        else:
            checker = checker | curr_onehot

    return True



if __name__ == '__main__':
    characters = 'icaunciaweuvnawioeuv'
    characters2 = 'asdfghkj' 
    print(is_unique_best(characters))
    print(is_unique_best(characters2))

