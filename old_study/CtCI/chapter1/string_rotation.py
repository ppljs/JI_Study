def is_substring(whole_str, piece_str):
    i = 0

    while i < len(whole_str) and len(piece_str) + i < len(whole_str):
        if whole_str[i] == piece_str[0]:
            found = True
            i += 1
            temp = i
            for j in range(1, len(piece_str)):
                if piece_str[j] != whole_str[i]:
                    found = False
                    break
                i += 1

            if found:
                return found

            i = temp
            
        i += 1


def is_string_rot(s1, s2):
    s2 = s2 + s2 + s2
    if is_substring(whole_str=s2, piece_str=s1):
        return True
    else:
        return False


if __name__ == '__main__':
    s1 = 'waterbottle'
    s2 = 'rbottlewate'

    print(is_string_rot(s1, s2))