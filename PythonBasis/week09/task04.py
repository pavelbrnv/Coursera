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
        if isinstance(value, int) or isinstance(value, float):
            return self.__mul_by_scalar(value)
        elif isinstance(value, Matrix) and self.size()[1] == value.size()[0]:
            return self.__mul_by_matrix(value)
        else:
            raise MatrixError(self, value)

    def __mul_by_scalar(self, value):
        result = map(
            lambda line: map(lambda v: v * value, line),
            self.values
        )
        return Matrix(result)

    def __mul_by_matrix(self, other):
        width = self.size()[1]
        rows = self.size()[0]
        columns = other.size()[1]
        result = list()
        for i in range(rows):
            line = list()
            for j in range(columns):
                val = 0
                for r in range(width):
                    val += self.values[i][r] * other.values[r][j]
                line.append(val)
            result.append(line)
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
