def is_permutation(s1, s2):
    if len(s1) != len(s2):
        return False
    
    if len(s1) == 0:
        return True

    i = 1
    xor1 = ord(s1[0])
    xor2 = ord(s2[0])
    # This only works because the two strings have to have the same size
    while i < len(s1):
        xor1 = xor1 ^ ord(s1[i])
        xor2 = xor2 ^ ord(s2[i])
        i += 1

    if xor1 == xor2:
        return True
    else:
        return False


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

