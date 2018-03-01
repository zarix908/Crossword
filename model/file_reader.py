class FileReader:
    @staticmethod
    def read(file_name):
        with open(file_name, 'r') as file:
            return list(map(lambda el: el.strip(), file.readlines()))
