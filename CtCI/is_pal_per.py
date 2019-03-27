# This function checks if one of the possible permutations of a string ia a palindrome.
# Time complexity = O(N) (N is the size of the string)
# Space complexity = O(1)
def is_pal_per(st):
    if st == '':
        return False

    st = st.replace(' ', '')
    st = [ord(c) for c in st]

    all_xor = st[0]

    for i in range(1, len(st)):
        all_xor ^= st[i]
    
    if len(st) % 2 == 0:
        if all_xor == 0:
            return True
    else:
        for c in st:
            if c == all_xor:
                return True
    
    return False


if __name__ == '__main__':
    st = 'aasfsf34'
    print(is_pal_per(st))