from matrix.ccs_matrix import CompressorCCSMatrix
from matrix.coordinates import Coordinate

class CompressedColumnMatrixBuilder():
    def __init__(self, size):
        self.size = size
        self.column_pointers = [0] * (size + 1)
        self.col_starts = [0] * size
        self.col_ends = [0] * size
        self.coordinates = []

    def set(self, i, j, value):
        self.coordinates.append(Coordinate(i, j, value))

    def get(self):
        self.row_ind = [0] * len(self.coordinates)
        self.values = [0.0] * len(self.coordinates)
        self.fill_ccs_arrays()
        self.calculate_col_ends()
        return CompressorCCSMatrix(self.size, self.column_pointers, self.row_ind, self.values)

    def fill_ccs_arrays(self):
        row_index = 0

        for coordinate in self.coordinates:
            i = coordinate.i
            j = coordinate.j
            value = coordinate.value

            self.col_starts[j] += 1
            self.row_ind[row_index] = i
            self.values[row_index] = value

            row_index += 1

    def calculate_col_ends(self):
        cumSum = 0

        for j in range(self.size):
            self.col_ends[j] = cumSum + self.col_starts[j]
            self.column_pointers[j] = cumSum
            cumSum = self.col_ends[j]
        self.column_pointers[self.size] = len(self.coordinates)


    def set_matrix(self, coordinate_matrix):
        size = coordinate_matrix.size
        for i in range(size):
            for j in range(size):
                value = coordinate_matrix.get(i, j)
                if value != 0:
                    self.coordinates.append(Coordinate(i, j, value))
