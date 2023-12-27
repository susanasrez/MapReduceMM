from matrix.coomatrix import CoordinateMatrix
from matrixBuilders.compressedRowbuilder import CompressedRowMatrixBuilder
from matrixBuilders.compressedColumnbuilder import CompressedColumnMatrixBuilder
from matrix.crsmatrix import CompressorCRSMatrix
from matrix.ccs_matrix import CompressorCCSMatrix
from matrix.coordinates import Coordinate
from matrix.denseMatrix import DenseMatrix
from matrixBuilders.densematrixgenerator import DenseMatrixBuilder


class MatrixTransformations:
    def transform(self, matrix):
        builder = DenseMatrixBuilder(matrix.size)
        for coordinate in matrix.coordinates:
            builder.set(coordinate.i, coordinate.j, coordinate.value)
        return builder.get()

    def transformCOO_CRS(self, matrix):
        builder = CompressedRowMatrixBuilder(matrix.size)
        matrixSort = matrix.getByRows()
        for coordinate in matrixSort.coordinates:
            builder.set(coordinate.i, coordinate.j, coordinate.value)
        return builder.get()

    def transformCOO_CCS(self, matrix):
        builder = CompressedColumnMatrixBuilder(matrix.size)
        matrixSort = matrix.getSortCol()
        for coordinate in matrixSort.coordinates:
            builder.set(coordinate.i, coordinate.j, coordinate.value)
        return builder.get()

    def transformCRS_COO(self, matrix):
        size = matrix.size
        coordinates = []

        for i in range(size):
            rowStart = matrix.rowPointers[i]
            rowEnd = matrix.rowPointers[i + 1]

            for k in range(rowStart, rowEnd):
                j = matrix.colInd[k]
                value = matrix.values[k]
                coordinates.append(Coordinate(i, j, value))

        return CoordinateMatrix(size, coordinates)

    def transformCCS_COO(self, matrix):
        size = matrix.size
        coordinates = []

        for j in range(size):
            colStart = matrix.columnPointers[j]
            colEnd = matrix.columnPointers[j + 1]

            for k in range(colStart, colEnd):
                i = matrix.rowInd[k]
                value = matrix.values[k]
                coordinates.append(Coordinate(i, j, value))

        return CoordinateMatrix(size, coordinates)
