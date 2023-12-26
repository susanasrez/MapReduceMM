<<<<<<< HEAD
import random
from model.denseMatrix import DenseMatrix

class RandomDenseMatrix:
    def __init__(self, N, density):
        self.N = N
        self.density = density
        self.matrix = self.generate_dense_matrix()

    def generate_dense_matrix(self):
        matrix = [[0] * self.N for _ in range(self.N)]
        num_elements = int(self.N * self.N * self.density)

        for _ in range(num_elements):
            while True:
                i, j = random.randint(0, self.N - 1), random.randint(0, self.N - 1)
                if matrix[i][j] == 0:
                    matrix[i][j] = random.randint(0, 20)
                    break

        return DenseMatrix(matrix, self.N)
=======
import random
from model.denseMatrix import DenseMatrix

class RandomDenseMatrix:
    def __init__(self, N, density):
        self.N = N
        self.density = density
        self.matrix = self.generate_dense_matrix()

    def generate_dense_matrix(self):
        matrix = [[0] * self.N for _ in range(self.N)]
        num_elements = int(self.N * self.N * self.density)

        for _ in range(num_elements):
            while True:
                i, j = random.randint(0, self.N - 1), random.randint(0, self.N - 1)
                if matrix[i][j] == 0:
                    matrix[i][j] = random.randint(0, 20)
                    break

        return DenseMatrix(matrix, self.N)
>>>>>>> de04ad2f6ef91015c4474ce6a213a0486b842092
