from kivy.core.window import Window
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle, Line
from kivy.core.text import Label as CoreLabel
from kivy.uix.widget import Widget


class MainWindow(Widget):
    def __init__(self, present, **kwargs):
        super().__init__(**kwargs)
        self.__present = present
        height = len(self.__present)
        width = len(self.__present[0])
        Window.size = (width * 30 + 2, height * 30 + 2)
        self.size = Window.size
        self.show_solution()

    def show_solution(self):
        with self.canvas:
            Color(0, 0, 0, 1)
            Rectangle(pos=(0, 0), size=self.size)
            height = len(self.__present)
            width = len(self.__present[0])

            for x in range(width):
                for y in range(height):
                    symbol = self.__present[y][x]

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
