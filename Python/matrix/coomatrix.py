from typing import List

class CoordinateMatrix():
    def __init__(self, size, coordinates):
        self.size = size
        self.coordinates = coordinates

    def size(self):
        return self.size

    def get(self, i, j):
        return next((c.value for c in self.coordinates if c.i == i and c.j == j), 0.0)

    def getByRows(self):
        self.coordinates.sort(key=lambda c: c.i)
        return CoordinateMatrix(self.size, self.coordinates)

    def getSortCol(self):
        self.coordinates.sort(key=lambda c: c.j)
        return CoordinateMatrix(self.size, self.coordinates)
    
    def display(self):
        print("Size: " + str(self.size))
        print("Coordinates: ")
        for c in self.coordinates:
            print(c.toString())
