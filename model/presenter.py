from utills import is_int


class Presenter:
    def __init__(self):
        self.__present = None
        self.__solution = None

    def get_present(self, width, height, solution, filled_grid):
        if solution is None:
            return None

        present = [['#' for x in range(width)] for y in range(height)]
        self.__solution = solution

        for node, word in self.__solution.items():
            self.print(present, node, word, filled_grid)

        return present

    def print(self, present, node, word, filled_grid):
        x = node.matrix_position.x
        y = node.matrix_position.y

        for letter in word:
            if not is_int(present[y][x]):
                present[y][x] = "&&" if filled_grid else letter

            if node.is_vertical_orientation:
                y += 1
            else:
                x += 1

        if filled_grid:
            present[node.matrix_position.y][node.matrix_position.x] = str(
                node.id)
