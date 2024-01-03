import random
from matrix.coomatrix import CoordinateMatrix
from matrix.coordinates import Coordinate

class CoordinateMatrixGenerator():
    
    @staticmethod
    def generate_random_coordinate_matrix(n, density):
        if density < 0.0 or density > 1.0:
            raise ValueError("Density must be in the range [0, 1].")

        total_non_zero_elements = int(round(n * n * density))
        random_instance = random.Random()

        coordinates = set()

        while len(coordinates) < total_non_zero_elements:
            row = random_instance.randint(0, n - 1)
            col = random_instance.randint(0, n - 1)
            coordinates.add((row, col))

        return CoordinateMatrix(n, [Coordinate(row, col, random_instance.randint(1, 100)) for row, col in coordinates])

    @staticmethod
    def contains_coordinate(coordinates, row, col):
        for coordinate in coordinates:
            if coordinate.i == row and coordinate.j == col:
                return True
        return False
