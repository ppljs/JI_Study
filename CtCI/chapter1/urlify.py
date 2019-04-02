# This exercise asks for the programmer to create a function that, given a string with extra whitespaces in the end,
# replace all the non-extar white spaces with a symbol (%20 in this case).
# Sometimes is better to go backwards (philosofical, isn' it?)
def urlify(st, size):
    symbol = '%20'
    old_index = size - 1
    new_index = len(st) - 1
    while old_index != new_index:
        if st[old_index] == ' ':
            for i in range(len(symbol) - 1, -1 , -1):
                st[new_index] = symbol[i]
                new_index -= 1
            new_index += 1
        else:
            st[new_index] = st[old_index]

        old_index -= 1
        new_index -= 1

    return st

if __name__ == '__main__':
    st = '  aosdifj '
    end_spaces = ' ' * (st.count(' ') * 2)
    size = len(st)
    st = st + end_spaces
    print(urlify(list(st), size))
