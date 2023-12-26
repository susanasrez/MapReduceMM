from model.denseMatrix import DenseMatrix
from model.coomatrix import COOMatrix

class MatrixMultiply:

    @staticmethod
    def multiply(matrix_a, matrix_b):
        N = matrix_a.N
        result_matrix = [[0] * N for _ in range(N)]

        for i in range(N):
            for j in range(N):
                for k in range(N):
                    result_matrix[i][j] += matrix_a.matrix[i][k] * matrix_b.matrix[k][j]

        return DenseMatrix(result_matrix, N)
    
    @staticmethod
    def multiplyCOO(matrix_a, matrix_b):
        result_elements = []
        elements_A = matrix_a.elements
        elements_B = matrix_b.elements

        for element_A in elements_A:
            for element_B in elements_B:
                if element_A[1] == element_B[0]:
                    result_value = element_A[2] * element_B[2]
                    result_elements.append((element_A[0], element_B[1], result_value))

        return COOMatrix(result_elements)