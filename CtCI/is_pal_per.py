# This function checks if one of the possible permutations of a string ia a palindrome.
# Time complexity = O(N) (N is the size of the string)
def is_pal_per(st):
    if st == '':
        return False

    st = st.replace(' ', '')

    checker_bit_vec = int(0)
    number_of_odds = 0

    for c in st:
        one_hot_char = 1 << (ord(c) - ord('a'))
        
        if checker_bit_vec & one_hot_char > 0:
            number_of_odds -= 1
        else:
            number_of_odds += 1

        checker_bit_vec = checker_bit_vec ^ one_hot_char
    
    if len(st) % 2 == 0:
        return bool(number_of_odds == 0)
    else:
        return bool(number_of_odds == 1)


if __name__ == '__main__':
    st = 'aasfsf'
    print(is_pal_per(st))