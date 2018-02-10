from model.file_reader import FileReader
from model.geometry_parser.geometry_parser import GeometryParser
from model.presenter import Presenter
from model.solver import Solver
from view.main_window import MainWindow
from kivy.app import App


class Crossword(App):
    def build(self):
        geometry_present = FileReader.read("examples/exp0/geometry.txt")
        geometry_graph = GeometryParser().parse(geometry_present)

        words = FileReader.read("examples/exp0/words.txt")

        solution = Solver().solve(geometry_graph, words)

        height = len(geometry_present)
        width = len(geometry_present[0])

        present = Presenter().get_present(width, height, solution)

        return MainWindow(present)


if __name__ == '__main__':
    Crossword().run()
