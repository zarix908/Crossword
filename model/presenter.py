class Presenter:
    def __init__(self):
        self.__present = None
        self.__solution = None

    def get_present(self, width, height, solution):
        if solution is None:
            return None

        present = [['#' for x in range(width)] for y in range(height)]
        self.__solution = solution

        for node, word in self.__solution.items():
            self.print(present, word, node.matrix_position,
                       node.is_vertical_orientation)

        return present

    def print(self, present, word, matrix_position, is_vertical):
        x = matrix_position.x
        y = matrix_position.y

        for letter in word:
            present[y][x] = letter

            if is_vertical:
                y += 1
            else:
                x += 1


