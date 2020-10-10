# https://www.byte-by-byte.com/autocomplete/
# With a given prefix and a collection of words, return all words that match that prefix

from collections import deque
from nltk.corpus import words # install nltk, then open python shell and run nltk.download('words')

class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else {}

class Trie:
    def __init__(self):
        self._root = Node(None, self._get_initial_children())

    def add_colection_of_words(self, dictionary):
        for word in dictionary:
            self.add_word(word)

    def add_word(self, word):
        curr = self._root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = Node(letter)
            curr = curr.children[letter]
        curr.children['*'] = None

    def get_all_words_from_prefix(self, prefix):
        if not prefix:
            return []

        curr = self._root
        base_word = deque()
        for letter in prefix:
            if letter not in curr.children:
                return []
            base_word.append(letter)
            curr = curr.children[letter]

        base_word.pop()
        words = deque()
        self._get_all_words_from_node(curr, base_word, words)
        
        return words

    def _get_all_words_from_node(self, node, curr_word, words):
        if not node:
            words.append(''.join(curr_word))
            return

        curr_word.append(node.value)
        for child in node.children.values():
            self._get_all_words_from_node(child, curr_word, words)
        curr_word.pop()

    def _get_initial_children(self):
        return {chr(i): Node(chr(i)) for i in range(ord('a'), ord('z') + 1)}


if __name__ == '__main__':
    english_trie = Trie()
    english_trie.add_colection_of_words(words.words())
    print(english_trie.get_all_words_from_prefix('light'))
