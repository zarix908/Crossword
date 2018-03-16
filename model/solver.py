from copy import copy

from model.lexicon.lexicon import Lexicon
from model.solutions_saver import SolutionsSaver


class Solver:
    def __init__(self):
        self.__geometry_graph = None
        self.__lexicon = None
        self.__current_node = None
        self.__from_previous = None
        self.__solutions_saver = SolutionsSaver()
        self.__solution_index = -1

    def get_next_solution(self, geometry_graph, words, reversed_mode):
        if self.__solution_index == -1:
            while not self.__solutions_saver.all_solutions_found:
                solution = self.solve(copy(geometry_graph), list(words),
                                      reversed_mode)
                self.__solutions_saver.save(solution)

        solutions = self.__solutions_saver.get_all()

        self.__solution_index += 1
        if self.__solution_index >= len(solutions):
            self.__solution_index = 0

        return solutions[self.__solution_index]

    def solve(self, geometry_graph, words, reversed_mode):
        self.refresh(geometry_graph, words, reversed_mode)
        way = []

        while True:
            if self.__from_previous:
                self.__current_node.generate_candidates(self.__lexicon)

            else:
                self.__current_node.pop_candidate(self.__lexicon)

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

    def refresh(self, geometry_graph, words, reversed_mode):
        self.__geometry_graph = geometry_graph
        self.__lexicon = Lexicon(words, self.__solutions_saver,
                                 reversed_enabled=reversed_mode)
        self.__current_node = self.__geometry_graph.next_node()
        self.__from_previous = True
