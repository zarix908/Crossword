from kivy.core.window import Window
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle, Line
from kivy.core.text import Label as CoreLabel
from kivy.uix.widget import Widget


class SolutionWidget(Widget):
    def __init__(self):
        super().__init__()

    def show_solution(self, present):
        with self.canvas:
            Color(0, 0, 0, 1)
            self.size = Window.size
            Rectangle(pos=(0, 0), size=self.size)
            height = len(present)
            width = len(present[0])

            for x in range(width):
                for y in range(height):
                    symbol = present[y][x]

                    if symbol != '#':
                        Color(0, 1, 0, 1)
                        label = CoreLabel(text=symbol, font_size=20)
                        label.refresh()
                        Rectangle(
                            pos=(x * 30 + 5, self.size[1] - (y + 1) * 30 + 5),
                            texture=label.texture,
                            size=label.texture.size)
                        self.draw_empty_rectangle(x,
                                                  self.size[1] - (y + 1) * 30)

    def draw_empty_rectangle(self, x, y):
        with self.canvas:
            x *= 30

            points = [x, y,
                      x + 30, y,
                      x + 30,
                      y + 30,
                      x, y + 30,
                      x, y]

            Line(points=points, width=2)
