class SolutionsSaver:
    def __init__(self):
        self.__solutions = []
        self.__solutions_found = False

    def save(self, solution):
        if solution is None:
            self.__solutions_found = True

        if len(self.__solutions) > 0:
            diff = set(self.__solutions[-1].items()) & set(solution.items())
            self.__solutions_found = len(diff) == len(self.__solutions[-1])

        if not self.__solutions_found:
            self.__solutions.append(solution)

    @property
    def all_solutions_found(self):
        return self.__solutions_found

    def get_last_values_for_node(self, node):
        result = set(map(lambda solution: solution[node], self.__solutions))
        return list(result)

    def get_all(self):
        return self.__solutions
