from kivy.core.window import Window
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle, Line
from kivy.properties import ObjectProperty
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Widget


class GeometryWidget(Widget):
    grid_layout = ObjectProperty(None)

    def __init__(self):
        super().__init__()
        self.size = Window.size

    def show_geometry(self, geometry):
        height = len(geometry)
        width = len(geometry[0])

        self.grid_layout.cols = width
        self.grid_layout.rows = height

        for y in range(height):
            for x in range(width):
                symbol = geometry[y][x]

                self.grid_layout.add_widget(
                    ToggleButton() if symbol != "#" else Widget())

    def get_same_letters_positions(self):
        pass
