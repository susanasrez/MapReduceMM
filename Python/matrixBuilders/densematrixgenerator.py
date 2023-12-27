from matrix.coomatrix import CoordinateMatrix
from matrix.denseMatrix import DenseMatrix

class DenseMatrixBuilder():
    def __init__(self, size):
        self.size = size
        self.values = [[0.0 for _ in range(size)] for _ in range(size)]

    def set(self, i, j, value):
        self.values[i][j] = value

    def set_Matrix(self, coordinateMatrix):
        coordMatrix = coordinateMatrix
        for i in range(self.size):
            for j in range(self.size):
                value = coordMatrix.get(i, j)
                self.set(i, j, value)

    def get(self):
        return DenseMatrix(self.values)
