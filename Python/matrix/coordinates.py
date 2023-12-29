
class Coordinate():

    def __init__(self, i, j, value):
        self.i = i
        self.j = j
        self.value = value
    
    def toString(self):
        return "i: " + str(self.i) + ", j: " + str(self.j) + ", value: " + str(self.value)