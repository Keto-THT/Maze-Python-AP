class Maze:
    def __init__(self, representation : list = None, file_path : str = None):
        self.representation = representation
        self.file_path = file_path

        if file_path:
            self.representation = self._load_from_file(file_path)

    def _load_from_file(self, file_path: str):
        representation = []
        with open(file_path, 'r') as f:
            for line in f:
                representation.append(list(line.rstrip('\n')))
        return representation

    def export(self, file_path: str):
        with open(file_path, 'w') as f:
            for line in self.representation:
                f.write(''.join(line) + '\n')

    def display_maze(self):
        for line in self.representation:
            print(''.join(line))

    def get_representation(self):
        return self.representation
