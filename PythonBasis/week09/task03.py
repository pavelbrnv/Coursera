from sys import stdin


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    def __init__(self, values):
        self.values = list(values)
        for i in range(len(self.values)):
            self.values[i] = list(self.values[i])

    def __str__(self):
        return '\n'.join(map(lambda l: '\t'.join(map(str, l)), self.values))

    def __add__(self, other):
        if self.size() != other.size():
            raise MatrixError(self, other)

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

    __rmul__ = __mul__

    def size(self):
        return len(self.values), len(self.values[0])

    def transpose(self):
        self.values = Matrix.transposed(self).values
        return self

    @staticmethod
    def transposed(matrix):
        rows, columns = matrix.size()
        values = list()
        for columnIndex in range(columns):
            line = list()
            for rowIndex in range(rows):
                line.append(matrix.values[rowIndex][columnIndex])
            values.append(line)
        return Matrix(values)


exec(stdin.read())
