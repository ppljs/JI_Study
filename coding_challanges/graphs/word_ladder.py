from collections import deque   
        
def get_ladder_smallest_length(begin, end, words):
    queue = deque([begin])
    next_level_queue = deque()
    words = set(words)
    length = 1
    while queue:
        curr = queue.popleft()
        to_remove = []
        for word in words:
            if can_go_to(curr, word):
                if word == end:
                    return length + 1
                next_level_queue.append(word)
                to_remove.append(word)
        
        for word_to_remove in to_remove:
            words.remove(word_to_remove)
        if not queue:
            length += 1
            queue, next_level_queue = next_level_queue, queue
                
    return 0


def can_go_to(source, target):
    diffs = 0
    for sl, tl in zip(source, target):
        if sl != tl:
            diffs += 1
        
        if diffs > 1:
            return False
    
    return True
