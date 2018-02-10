from model.lexicon.lexicon import Lexicon


class Solver:
    def __init__(self):
        self.__geometry_graph = None
        self.__lexicon = None
        self.__current_node = None
        self.__from_previous = None

    def solve(self, geometry_graph, words):
        self.refresh(geometry_graph, words)
        way = []

        while True:
            if self.__from_previous:
                mask = self.__current_node.generate_mask()
                candidates = self.__lexicon.get_word_by(mask)
                self.__current_node.words_candidates = candidates

            else:
                self.__current_node.words_candidates.pop()

            if len(self.__current_node.words_candidates) == 0:
                self.__from_previous = False
                if len(way) > 0:
                    way.pop()
                self.__current_node = self.__geometry_graph.previous_node()
            else:
                self.__from_previous = True
                way.append(self.__current_node)
                self.__current_node = self.__geometry_graph.next_node()

            if self.__current_node is None:
                break

        if not self.__from_previous:
            return None

        solution = {}

        for node in way:
            solution[node] = node.words_candidates[-1]

        return solution

    def refresh(self, geometry_graph, words):
        self.__geometry_graph = geometry_graph
        self.__lexicon = Lexicon(words)
        self.__current_node = self.__geometry_graph.next_node()
        self.__from_previous = True


