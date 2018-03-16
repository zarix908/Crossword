from model.lexicon.mask import Mask

from model.geometry_parser.double_dict import DoubleDictionary


class GeometryNode:
    def __init__(self, is_vertical, matrix_position):
        self.words_candidates = []
        self.capacity = None
        self.id = None
        self.__incidents_nodes = DoubleDictionary()
        self.__is_vertical_orientation = is_vertical
        self.__matrix_position = matrix_position

    @property
    def is_vertical_orientation(self):
        return self.__is_vertical_orientation

    @property
    def matrix_position(self):
        return self.__matrix_position

    @property
    def incident_nodes(self):
        yield from self.__incidents_nodes

    def add_incident(self, node, index):
        self.__incidents_nodes.add(node, index)

    def generate_mask(self):
        mask_content = {}
        for index, node in self.__incidents_nodes.items():
            letter = node.get_letter_for(self)
            if letter is not None:
                mask_content[index] = letter

        return Mask(self.capacity, mask_content)

    def get_letter_for(self, incident_node):
        adj_letter_index = self.__incidents_nodes[incident_node]

        return self.words_candidates[-1][adj_letter_index] if len(
            self.words_candidates) > 0 else None

    def generate_candidates(self, lexicon):
        mask = self.generate_mask()
        self.words_candidates = lexicon.get_word_by(mask, self)

        if len(self.words_candidates) > 0:
            lexicon.use_word(self.words_candidates[-1])

    def pop_candidate(self, lexicon):
        word = self.words_candidates.pop()
        lexicon.free_word(word)

        if len(self.words_candidates) > 0:
            lexicon.use_word(self.words_candidates[-1])

    def __str__(self):
        return "\n--------------------------\n" + str(self.id) + "\n" + str(
            self.capacity) + "\n" + str(
            list(map(lambda el: el.id, self.__incidents_nodes))) + "\n" + str(
            self.__matrix_position) + "\n"
