import random
from matrix.coomatrix import CoordinateMatrix
from matrix.coordinates import Coordinate

class CoordinateMatrixGenerator():
    @staticmethod
    def generate_random_coordinate_matrix(n, density):
        if density < 0.0 or density > 1.0:
            raise ValueError("Density must be in the range [0, 1].")

        coordinates = []
        total_non_zero_elements = int(round(n * n * density))
        random_instance = random.Random()

        for _ in range(total_non_zero_elements):
            row, col = 0, 0
            is_unique = False
            while not is_unique:
                row = random_instance.randint(0, n - 1)
                col = random_instance.randint(0, n - 1)
                is_unique = not CoordinateMatrixGenerator.contains_coordinate(coordinates, row, col)

            value = random_instance.randint(1, 100)
            coordinates.append(Coordinate(row, col, value))

        return CoordinateMatrix(n, coordinates)

    @staticmethod
    def contains_coordinate(coordinates, row, col):
        for coordinate in coordinates:
            if coordinate.i == row and coordinate.j == col:
                return True
        return False

    def set(self, i, j, value):
        pass

    def set_matrix(self, c):
        pass

    def get(self):
        return None
