import random
from model.coomatrix import COOMatrix

class CoordinateMatrixGenerator:
    def __init__(self, N, density):
        self.N = N
        self.density = density
        self.matrix = self.generate_coordinate_matrix()

    def generate_coordinate_matrix(self):
        matrix = set()

        num_elements = int(self.N * self.N * self.density)

        while len(matrix) < num_elements:
            row = random.randint(0, self.N - 1)
            col = random.randint(0, self.N - 1)
            value = random.randint(1, 20)
            matrix.add((row, col, value))

        return COOMatrix(list(matrix))

