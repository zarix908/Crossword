from model.presenter import Presenter


class SameLettersChecker:
    def __init__(self):
        self.__presenter = Presenter()

    def check(self, solution, geometry_present, same_letters_positions):
        for position in same_letters_positions:
            height = len(geometry_present)
            width = len(geometry_present[0])

            present = self.__presenter.get_present(width, height, solution,
                                                   filled_grid=False)
            if present[position.y][position.x]:
                return False

        return True
