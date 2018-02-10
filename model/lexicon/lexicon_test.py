import unittest

from lexicon.mask import Mask

from model.lexicon.lexicon import Lexicon


class WordsFilterTest(unittest.TestCase):
    def test_main(self):
        words = ["apple", "banana", "pineapple", "cherry", "orange"]
        test_filter = Lexicon(words)

        mask = Mask(6, {})
        answer = sorted(list(test_filter.get_word_by(mask)))
        self.assertListEqual(answer,
                             ["ananab", "banana", "cherry", "egnaro", "orange",
                              "yrrehc"])

        mask = Mask(6, {2: 'n'})
        answer = sorted(list(test_filter.get_word_by(mask)))
        self.assertListEqual(answer, ["banana", "egnaro"])
