import random
from model.crsmatrix import CRSMatrix

class COOToCRSConverter:
    def __init__(self, coo_matrix):
        self.coo_matrix = coo_matrix
        self.rows, self.cols, self.vals = self.extract_coordinates()
        self.matrix = self.convert_to_crs()

    def extract_coordinates(self):
        elements = self.coo_matrix.get_elements()
        rows = [element[0] for element in elements]
        cols = [element[1] for element in elements]
        vals = [element[2] for element in elements]
        return rows, cols, vals

    def convert_to_crs(self):
        N = max(self.rows) + 1
        rowptr = [0] * (N + 1)
        col = []
        values = []

        for row in self.rows:
            rowptr[row + 1] += 1
        for i in range(1, N + 1):
            rowptr[i] += rowptr[i - 1]

        for i in range(len(self.rows)):
            row = self.rows[i]
            col_value = self.cols[i]
            val = self.vals[i]
            col.append(col_value)
            values.append(val)
            rowptr[row] += 1

        return CRSMatrix(rowptr, col, values)


