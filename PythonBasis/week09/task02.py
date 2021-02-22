from sys import stdin


class Matrix:
    def __init__(self, values):
        self.values = list(values)
        for i in range(len(self.values)):
            self.values[i] = list(self.values[i])

    def __str__(self):
        return '\n'.join(map(lambda l: '\t'.join(map(str, l)), self.values))

    def __add__(self, other):
        result = map(
            lambda pair: map(lambda v: v[0] + v[1], zip(pair[0], pair[1])),
            zip(self.values, other.values)
        )
        return Matrix(result)

    def __mul__(self, value):
        result = map(
            lambda line: map(lambda v: v * value, line),
            self.values
        )
        return Matrix(result)

    def __rmul__(self, value):
        return self * value

    def size(self):
        return len(self.values), len(self.values[0])


exec(stdin.read())
