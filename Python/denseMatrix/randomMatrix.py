import random

class RandomMatrixGenerator:
    def __init__(self, N, density):
        self.N = N
        self.density = density

    def generate_matrix(self):

        matrix = []
        for i in range(self.N):
            row = []
            for j in range(self.N):
                if random.random() < self.density:
                    value = random.randint(1, 10)
                else:
                    value = 0
                row.append(value)
            matrix.append(row)

        return matrix

    def print_matrix(self, matrix):
        for row in matrix:
            print(" ".join(map(str, row)))

