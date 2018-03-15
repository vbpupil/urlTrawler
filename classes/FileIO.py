class FileIO:
    def __init__(self, path):
        if isinstance(path, str):
            self.path = path
        else:
            raise ValueError('Incorrect TYPE, expecting str')

    def write(self, data):
        try:
            file = open(self.path, 'w')
            file.write(str(data))
        except IOError:
            raise IOError('Problem dealing with file: ' + self.path)

    def read(self):
        try:
            file = open(self.path, 'r')
            return file.read()
        except IOError:
            raise IOError('Problem dealing with file: ' + self.path)

    def return_list(self, splitter='\n'):
        try:
            src = open(self.path, 'r')
            return [line.split(splitter) for line in src.readlines()]
        except IOError:
            raise IOError('Problem dealing with file: ' + self.path)