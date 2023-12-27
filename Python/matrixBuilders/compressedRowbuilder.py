from matrix.coordinates import Coordinate
from matrix.crsmatrix import CompressorCRSMatrix

class CompressedRowMatrixBuilder():
    def __init__(self, size):
        self.row_pointers = [0] * (size + 1)
        self.row_starts = [0] * size
        self.row_ends = [0] * size
        self.size = size
        self.coordinates = []

    def set(self, i, j, value):
        self.coordinates.append(Coordinate(i, j, value))

    def get(self):
        col_ind = [0] * len(self.coordinates)
        values = [0.0] * len(self.coordinates)
        self.fill_crs_arrays(col_ind, values)
        self.calculate_row_ends()
        return CompressorCRSMatrix(self.size, self.row_pointers, col_ind, values)

    def fill_crs_arrays(self, col_ind, values):
        column_index = 0

        for coordinate in self.coordinates:
            i = coordinate.i
            j = coordinate.j
            value = coordinate.value

            self.row_starts[i] += 1
            col_ind[column_index] = j
            values[column_index] = value

            column_index += 1

    def calculate_row_ends(self):
        cum_sum = 0

        for i in range(self.size):
            self.row_ends[i] = cum_sum + self.row_starts[i]
            self.row_pointers[i] = cum_sum
            cum_sum = self.row_ends[i]

        self.row_pointers[self.size] = len(self.coordinates)

    def set_matrix(self, coordinate_matrix):
        size = coordinate_matrix.size
        for i in range(size):
            for j in range(size):
                value = coordinate_matrix.get(i, j)
                if value != 0:
                    self.coordinates.append(Coordinate(i, j, value))
        
    def set_coordinate_matrix(self, coordinate_matrix):
        self.coordinates = []
        self.set_matrix(coordinate_matrix)
