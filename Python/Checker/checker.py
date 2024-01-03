from operations.original.denseMultiplication import DenseMatrixMultiplication

class Checker:
    @staticmethod
    def test_dense(a, b, c):
        multiplier = DenseMatrixMultiplication()
        ab = multiplier.multiply(a, b)
        ab_c = multiplier.multiply(ab, c)
        bc = multiplier.multiply(b, c)
        a_bc = multiplier.multiply(a, bc)
        bool = Checker.are_matrices_equal(ab_c, a_bc)
        print("Multiplication is right: ", bool)

    @staticmethod
    def are_matrices_equal(matrix1, matrix2):
        epsilon = 1E-8
        a = matrix1
        b = matrix2
        size = matrix1.size
        for i in range(size):
            for j in range(size):
                if abs(a.values[i][j] - b.values[i][j]) > epsilon:
                    return False
        return True
    