class Mask:
    def __init__(self, length, mask_content):
        self.__length = length
        self.__mask_content = mask_content

    @property
    def length(self):
        return self.__length

    def word_is_match(self, word):
        for index, letter in self.__mask_content.items():
            if word[index] != letter:
                return False

        return True
