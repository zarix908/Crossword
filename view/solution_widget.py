from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line, Rectangle
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.text import Label as CoreLabel


class SolutionWidget(Widget):
    CELL_SIZE = 30
    OFFSET = 5

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def show_solution(self, present):
        if present is None:
            self.add_widget(
                Label(text="No solution", color=(0, 1, 0, 1), size=self.size))
            return

        with self.canvas:
            Color(0, 0, 0, 1)

            Rectangle(pos=(0, 0), size=self.size)
            height = len(present)
            width = len(present[0])

            self.grid_layout.cols = height
            self.grid_layout.rows = width

            for x in range(width):
                for y in range(height):
                    symbol = present[y][x]

                    if symbol != '#':
                        Color(0, 1, 0, 1)
                        label = CoreLabel(text=symbol, font_size=20)
                        label.refresh()
                        Rectangle(
                            pos=(x * self.CELL_SIZE + self.OFFSET,
                                 self.size[1] - (
                                 y + 1) * self.CELL_SIZE + self.OFFSET),
                            texture=label.texture,
                            size=label.texture.size)
                        self.draw_empty_rectangle(x,
                                                  self.size[1] - (
                                                      y + 1) * self.CELL_SIZE)

    def draw_empty_rectangle(self, x, y):
        with self.canvas:
            x *= self.CELL_SIZE

            points = [x, y,
                      x + self.CELL_SIZE, y,
                      x + self.CELL_SIZE,
                      y + self.CELL_SIZE,
                      x, y + self.CELL_SIZE,
                      x, y]

            Line(points=points, width=2)
