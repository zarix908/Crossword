from collections import defaultdict


class Lexicon:
    def __init__(self, words, reversed_enabled):
        self.__words = defaultdict(lambda: [])

        for word in words:
            length = len(word)
            self.__words[length].append(word)

            if reversed_enabled:
                self.__words[length].append("".join(reversed(word)))

    def get_word_by(self, mask):
        return list((filter(lambda word: mask.word_is_match(word),
                            self.__words[mask.length])))
