import sys


class FileReader:
    def read(self, file_name):
        try:
            with open(file_name, 'r') as file:
                return list(map(lambda el: el.strip(), file.readlines()))
        except FileExistsError:
            self.error(file_name, is_exist_error=True)
        except FileNotFoundError:
            self.error(file_name, is_exist_error=False)

    def error(self, file_name, is_exist_error):
        print(
            "File " + '\"' + file_name + '\"' + " not" +
            (" exist." if is_exist_error else " found.") +
            " Try main.py -h or --help",
            file=sys.stderr)
        exit(1)
