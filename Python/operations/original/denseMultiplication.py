from matrix.denseMatrix import DenseMatrix

class DenseMatrixMultiplication():
    def multiply(self, matrix_a, matrix_b):
        a = matrix_a
        b = matrix_b
        c = [[0.0] * a.size for _ in range(b.size)]

        for i in range(a.size):
            for j in range(a.size):
                for k in range(b.size):
                    c[i][j] += a.get(i, k) * b.get(k, j)

        return DenseMatrix(c)
