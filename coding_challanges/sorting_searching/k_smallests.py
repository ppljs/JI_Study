import heapq

def get_k_smallest(arr, k):
    if not arr:
        return []
    if len(arr) <= k:
        return arr

    arr = invert_arr(arr)
    k_smallests = [arr[0]]
    for value in arr[1:]:
        if len(k_smallests) >= k:
            heapq.heappop(k_smallests)
        
        heapq.heappush(k_smallests, value)
    
    return invert_arr(k_smallests)

def invert_arr(arr):
    return [-elem for elem in arr]


print(get_k_smallest([7,4,1,99,5,3,-11,0,3,-1], 4))
