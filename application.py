from kivy.config import Config

Config.set('graphics', 'resizable', False)

from kivy.app import App
from view.main_window import MainWindow


class CrosswordApp(App):
    def __init__(self, geometry_file_name, words_file_name, reversed_mode):
        super().__init__()
        self.__geo_file_name = geometry_file_name
        self.__words_file_name = words_file_name
        self.__reversed_mode = reversed_mode

    def build(self):
        main_window = MainWindow(self.__reversed_mode)

        if self.__geo_file_name is not None:
            main_window.load_geometry([self.__geo_file_name])
        if self.__words_file_name is not None:
            main_window.load_words([self.__words_file_name])

        return main_window
