# Function to check if the levenshtein distance is equal or less than one. For shure not
# the best implementation. I still have to discover a more elegant and scalable way (for two_edit, three_edit etc).
def is_one_edit(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        return False
    
    ind1 = ind2 = 0
    one_wrong = False
    while True:
        one_over = ind1 >= len(str1)
        two_over = ind2 >= len(str2)
        if one_over or two_over:
            if one_wrong:
                if one_over and two_over:
                    return True
                else:
                    return False
            else:
                return True

        if str1[ind1] != str2[ind2]:
            if one_wrong:
                return False
            else:
                one_wrong = True

            if ind1 + 1 < len(str1) and str1[ind1 + 1] == str2[ind2]:
                ind1 += 1
            elif ind2 + 1 < len(str2) and str2[ind2 + 1] == str1[ind1]:
                ind2 += 1

        ind1 += 1
        ind2 += 1


if __name__ == '__main__':
    str1 = 'a'
    str2 = ''
    print(is_one_edit(str1, str2))