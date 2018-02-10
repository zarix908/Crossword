from enum import Enum


class WordType(Enum):
    HORIZONTAL = 0
    VERTICAL = 1

    @staticmethod
    def invert(type):
        return (int(type) + 1) % 2

    def __int__(self):
        return self.value

    def __str__(self):
        return self.name