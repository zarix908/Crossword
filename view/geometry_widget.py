from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle, Line
from kivy.uix.widget import Widget


class GeometryWidget(Widget):
    def __init__(self):
        super().__init__()

    def show_geometry(self, geometry):
        with self.canvas:
            Color(0, 0, 0, 1)
            Rectangle(pos=(0, 0), size=self.size)
            height = len(geometry)
            width = len(geometry[0])

            for x in range(width):
                for y in range(height):
                    symbol = geometry[y][x]

                    if symbol != '#':
                        Color(1, 1, 1, 1)
                        self.draw_empty_rectangle(x, y)

    def draw_empty_rectangle(self, x, y):
        with self.canvas:
            x *= 30
            y *= 30

            points = [x, y,
                      x + 30, y,
                      x + 30,
                      y + 30,
                      x, y + 30,
                      x, y]

            Line(points=points, width=1)
