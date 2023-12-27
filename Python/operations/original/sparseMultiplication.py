from matrixBuilders.coordinateMatrixBuilder import CoordinateMatrixBuilder

class SparseMatrixMultiplication:
    def multiply(self, matrix_a, matrix_b):
        a = matrix_a
        b = matrix_b
        builder = CoordinateMatrixBuilder(a.size)

        for i in range(a.size):
            for j in range(b.size):
                rowStart = a.row_pointers[i]
                rowEnd = a.row_pointers[i+1]
                colStart = b.column_pointers[j]
                colEnd = b.column_pointers[j+1]
                s = 0

                while rowStart < rowEnd and colStart < colEnd:
                    aa = a.col_indices[rowStart]
                    bb = b.row_ind[colStart]
                    if aa == bb:
                        s += a.values[rowStart] * b.values[colStart]
                        rowStart += 1
                        colStart += 1
                    elif aa < bb:
                        rowStart += 1
                    else:
                        colStart += 1
                if s != 0:
                    builder.set(i, j, s)

        return builder.get()
