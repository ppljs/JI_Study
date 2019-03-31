def compress_string(st):
    if len(st) < 3:
        return st
    
    i = 1
    curr_char = st[0]
    comp_st = []
    counter = 1
    while i < len(st):
        if st[i] == curr_char:
            counter += 1
        else:            
            comp_st.append(curr_char + str(counter))
            counter = 1
            curr_char = st[i]
        
        if len(comp_st) >= len(st):
            return st
        i += 1
    
    comp_st.append(curr_char + str(counter))
    
    return st if len(comp_st) >= len(st) else ''.join(comp_st)


if __name__ == '__main__':
    st = 'aaabbbccccccccab'
    print(compress_string(st))