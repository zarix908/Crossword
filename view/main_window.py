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

    def __init__(self, reversed_mode, **kwargs):
        super().__init__(**kwargs)
        self.__reversed_mode = reversed_mode
        self.__solver = Solver()

        self.__popup = None
        self.__geometry_graph = None
        self.__geometry_present = None
        self.__words = None
        self.__body_contain_widgets = []
        self.load = None

    def show_load(self, loading_component):
        if loading_component == "geometry.txt":
            self.load = self.load_geometry
        else:
            self.load = self.load_words

        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self.__popup = Popup(title="Load file", content=content,
                             size_hint=(0.9, 0.9))
        self.__popup.open()

    def load_geometry(self, file_names):
        self.__geometry_present = FileReader().read(file_names[0])
        self.__geometry_graph = GeometryParser().parse(self.__geometry_present)

        geometry_widget = GeometryWidget()
        self.__body_contain_widgets.append(geometry_widget)
        geometry_widget.show_geometry(self.__geometry_present)
        self.body_widget.add_widget(geometry_widget)
        self.dismiss_popup()

        self.__solver = Solver()

    def load_words(self, file_names):
        self.__words = FileReader().read(file_names[0])
        label = Label(text="\n".join(self.__words))
        self.__body_contain_widgets.append(label)
        self.body_widget.add_widget(label)
        self.dismiss_popup()

        self.__solver = Solver()

    def solve(self):
        solution = self.__solver.get_next_solution(self.__geometry_graph, self.__words,
                                              self.__reversed_mode)

        height = len(self.__geometry_present)
        width = len(self.__geometry_present[0])

        present = Presenter().get_present(width, height, solution)

        for widget in self.__body_contain_widgets:
            self.body_widget.remove_widget(widget)

        self.body_widget.size_hint_x = 1 - (30 / self.height)

        solution_widget = SolutionWidget(size=self.body_widget.size)
        solution_widget.show_solution(present)
        self.body_widget.add_widget(solution_widget)

    def dismiss_popup(self):
        if self.__popup is not None:
            self.__popup.dismiss()
