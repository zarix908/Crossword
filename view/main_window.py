from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget

from model.file_reader import FileReader
from model.geometry_parser.geometry_parser import GeometryParser
from model.presenter import Presenter
from model.solver import Solver
from view.geometry_widget import GeometryWidget
from view.load_dialog import LoadDialog
from view.solution_widget import SolutionWidget


class MainWindow(Widget):
    body_widget = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__popup = None
        self.__geometry_graph = None
        self.__geometry_present = None
        self.__words = None
        self.load = None

    def show_load(self, loading_component):
        if loading_component == "geometry":
            self.load = self.load_geometry
        else:
            self.load = self.load_words

        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self.__popup = Popup(title="Load file", content=content,
                             size_hint=(0.9, 0.9))
        self.__popup.open()

    def load_geometry(self, file_names):
        self.__geometry_present = FileReader.read(file_names[0])
        self.__geometry_graph = GeometryParser().parse(self.__geometry_present)

        geometry_widget = GeometryWidget()
        geometry_widget.show_geometry(self.__geometry_present)
        self.body_widget.add_widget(geometry_widget)
        self.dismiss_popup()

    def load_words(self, file_names):
        self.__words = FileReader.read(file_names[0])
        label = Label(text="\n".join(self.__words))
        self.body_widget.add_widget(label)
        self.dismiss_popup()

    def solve(self):
        solution = Solver().solve(self.__geometry_graph, self.__words)

        height = len(self.__geometry_present)
        width = len(self.__geometry_present[0])

        present = Presenter().get_present(width, height, solution)

        self.body_widget.clear_widgets()
        solution_widget = SolutionWidget()
        solution_widget.show_solution(present)
        self.body_widget.add_widget(solution_widget)

    def dismiss_popup(self):
        if self.__popup is not None:
            self.__popup.dismiss()
