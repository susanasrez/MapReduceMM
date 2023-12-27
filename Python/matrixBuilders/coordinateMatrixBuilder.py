from matrix.coomatrix import CoordinateMatrix
from matrix.coordinates import Coordinate

class CoordinateMatrixBuilder():
    def __init__(self, size):
        self.size = size
        self.coordinates = []

    def set(self, i, j, value):
        coordinate = Coordinate(i, j, value)
        self.set_Coordinate(coordinate)
    
    def set_Coordinate(self, coordinate):
        self.coordinates.append(coordinate)

    def get(self):
        return CoordinateMatrix(self.size, self.coordinates).getByRows()

    def getByCols(self):
        return CoordinateMatrix(self.size, self.coordinates).getSortCol()
