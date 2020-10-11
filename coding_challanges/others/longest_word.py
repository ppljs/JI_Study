def get_longest_word(words):
    words = sorted(words, key=lambda word: len(word), reverse=True)
    wordToIsComposable = { word: True for word in words }

    for word in words:
        if is_word_made_by_composition(word, wordToIsComposable):
            return word
    
    return ''


def is_word_made_by_composition(word, wordToIsComposable, isOriginalWord=True):
    if word in wordToIsComposable and not isOriginalWord:
        return True

    for i in range(1, len(word)):
        word_left = word[0:i]
        if (
            word_left in wordToIsComposable and
            wordToIsComposable[word_left] and
            is_word_made_by_composition(word[i:], wordToIsComposable, False)
        ):
            return True

    wordToIsComposable[word] = False
    
    return False


if __name__ == '__main__':
    words = ['cat', 'banana', 'dog', 'nana', 'walk', 'walker', 'dogwalker']
    # words = ['cat', 'cats', 'sdog', 'catsdog']
    print(get_longest_word(words))
