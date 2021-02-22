from sys import stdin


class Matrix:
    def __init__(self, values):
        self.values = list(values)
        for i in range(len(self.values)):
            self.values[i] = list(self.values[i])

    def __str__(self):
        return '\n'.join(map(lambda l: '\t'.join(map(str, l)), self.values))

    def size(self):
        return len(self.values), len(self.values[0])


exec(stdin.read())
