from matrix.coomatrix import CoordinateMatrix
from matrix.coordinates import Coordinate
from matrix.denseMatrix import DenseMatrix
from matrixBuilders.densematrixgenerator import DenseMatrixBuilder


class MatrixTransformations:

    @staticmethod
    def transform(matrix):
        builder = DenseMatrixBuilder(matrix.size)
        for coordinate in matrix.coordinates:
            builder.set(coordinate.i, coordinate.j, coordinate.value)
        return builder.get()

