class DoubleDictionary:
    def __init__(self):
        self.__dict1 = {}
        self.__dict2 = {}

    def add(self, item1, item2):
        self.__dict1[item1] = item2
        self.__dict2[item2] = item1

    def __getitem__(self, item):
        return self.__dict1[item] if item in self.__dict1 else self.__dict2[
            item]

    def __iter__(self):
        return iter(self.__dict1)

    def items(self):
        return self.__dict2.items()

    def __len__(self):
        return len(self.__dict1)

    def __contains__(self, item):
        return item in self.__dict2
