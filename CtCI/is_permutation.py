def is_permutation(s1, s2):
    if len(s1) != len(s2):
        return False
    
    if len(s1) == 0:
        return True

    checker = [0] * 256  # Considring the extended ASCII table

    for c in s1:
        checker[ord(c)] += 1

    for c in s2:
        if checker[ord(c)] == 0:
            return False
        
        checker[ord(c)] -= 1

    return True

def permute(a, l, r, result): 
    if l==r: 
        result.append(''.join(a)) 
    else: 
        for i in range(l,r+1): 
            a[l], a[i] = a[i], a[l] 
            permute(a, l+1, r, result) 
            a[l], a[i] = a[i], a[l] # backtrack 


if __name__ == '__main__':
    test = '1423'
    result = []
    permute(list(test), 0, len(test) - 1, result)
    k = 0
    for i in result:
        for j in result:
            if is_permutation(i, j) == False:
                print('Did not work')
                quit()
            k += 1

