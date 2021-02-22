from sys import stdin


class MatrixError(Exception):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class MatrixIsInvalidError(Exception):
    def __init__(self, matrix, description):
        self.matrix = matrix
        self.description = description


class MatrixVectorError(Exception):
    def __init__(self, matrix, vector):
        self.matrix = matrix
        self.vector = vector


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
        result = Matrix.mul_values(self.values, other.values)
        return Matrix(result)

    __rmul__ = __mul__

    def size(self):
        return len(self.values), len(self.values[0])

    def transpose(self):
        self.values = Matrix.transposed(self).values
        return self

    def solve(self, b_vector):
        matrix = Matrix.append_column_vector(self, b_vector)
        return Matrix.__gauss(matrix)

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

    @staticmethod
    def append_column_vector(matrix, vector):
        rows, columns = matrix.size()

        if rows != len(vector):
            raise MatrixVectorError(matrix, vector)

        values = list()
        for rowIndex in range(rows):
            line = list()
            for columnIndex in range(columns):
                line.append(matrix.values[rowIndex][columnIndex])
            line.append(vector[rowIndex])
            values.append(line)
        return Matrix(values)

    @staticmethod
    def mul_values(a, b):
        width = len(a[0])
        rows = len(a)
        columns = len(b[0])
        result = list()
        for i in range(rows):
            line = list()
            for j in range(columns):
                val = 0
                for r in range(width):
                    val += a[i][r] * b[r][j]
                line.append(val)
            result.append(line)
        return result

    @staticmethod
    def identity_values(size):
        values = list()
        for rowIndex in range(size):
            line = [0 for i in range(size)]
            line[rowIndex] = 1
            values.append(line)
        return values

    @staticmethod
    def __gauss(matrix):
        m = matrix.size()[0]

        if not all([len(row) == m + 1 for row in matrix.values[1:]]):
            raise MatrixIsInvalidError(matrix, 'Non-uniform rows length')

        a = Matrix(matrix.values).values

        n = m + 1

        for k in range(m):
            pivots = [abs(a[i][k]) for i in range(k, m)]
            i_max = pivots.index(max(pivots)) + k

            # Check for singular matrix
            if a[i_max][k] == 0:
                raise MatrixIsInvalidError(matrix, 'Matrix is singular')

            # Swap rows
            a[k], a[i_max] = a[i_max], a[k]

            for i in range(k + 1, m):
                f = a[i][k] / a[k][k]
                for j in range(k + 1, n):
                    a[i][j] -= a[k][j] * f

                # Fill lower triangular matrix with zeros:
                a[i][k] = 0

        # Solve equation Ax=b for an upper triangular matrix A
        x = []
        for i in range(m - 1, -1, -1):
            x.insert(0, a[i][m] / a[i][i])
            for k in range(i - 1, -1, -1):
                a[k][m] -= a[k][i] * x[0]
        return x


class SquareMatrix(Matrix):
    def __init__(self, values):
        if len(values) != len(values[0]):
            raise MatrixIsInvalidError(self, 'Matrix is not square')
        Matrix.__init__(self, values)

    def __pow__(self, n):
        if n < 0:
            raise MatrixIsInvalidError(self, 'Negative power')
        result = SquareMatrix.__fast_power_values(self.values, n)
        return SquareMatrix(result)

    @staticmethod
    def __fast_power_values(a, n):
        if n == 0:
            return Matrix.identity_values(len(a))
        elif n == 1:
            return a
        elif n % 2 != 0:
            x = SquareMatrix.__fast_power_values(a, n - 1)
            return Matrix.mul_values(x, a)
        else:
            x = SquareMatrix.mul_values(a, a)
            return SquareMatrix.__fast_power_values(x, n // 2)


exec(stdin.read())
