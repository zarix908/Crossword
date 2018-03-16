from collections import defaultdict


class Lexicon:
    def __init__(self, words, solution_saver, reversed_enabled):
        self.__words = defaultdict(lambda: [])
        self.__used_words = set()
        self.__solution_saver = solution_saver

        for word in words:
            length = len(word)
            self.__words[length].append(word)

            if reversed_enabled:
                self.__words[length].append("".join(reversed(word)))

    def get_word_by(self, mask, node):
        def filter_function(word):
            return mask.word_is_match(word) and word not in self.__used_words
        words = list((filter(filter_function, self.__words[mask.length])))

        values = self.__solution_saver.get_last_values_for_node(node)
        for value in values:
            if value in words:
                words.remove(value)
                words.append(value)

        return list(reversed(words))

    def use_word(self, word):
        self.__used_words.add(word)

    def free_word(self, word):
        self.__used_words.remove(word)
