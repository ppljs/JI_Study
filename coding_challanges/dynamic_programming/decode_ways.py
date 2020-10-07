def numDecodings(s):
    memory = [-1] * len(s)
    def ways_of_decoding(message, i=0):
        if i >= len(message):
            return 1

        if message[i] == 0:
            return 0

        if memory[i] != -1:
            return memory[i]

        count_one = ways_of_decoding(message, i + 1)
        count_two = ways_of_decoding(message, i + 2) if i + 2 <= len(message) and is_double_digit_valid(message[i], message[i+1]) else 0

        memory[i] = count_one + count_two
        return memory[i]

    s = [int(c) for c in s]
    return ways_of_decoding(s)


def is_double_digit_valid(first, second):
    return (first * 10) + second < 27
