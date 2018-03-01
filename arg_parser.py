class ArgParser:
    def __init__(self, arguments):
        self.__arguments = arguments

    def parse(self):
        help_message = "Error! Too many arguments. Usage: ./main.py " + \
                       "[geometry filename] [words filename]"

        if len(self.__arguments) > 3:
            print()
