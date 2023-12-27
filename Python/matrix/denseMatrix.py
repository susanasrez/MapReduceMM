class DenseMatrix():
    def __init__(self, values):
        self.size = len(values)
        self.values = values

    def size(self):
        return len(self.values)

    def get(self, i, j):
        return self.values[i][j]
    
    def display(self):
        print("Size: " + str(self.size))
        print("Values: ")
        for i in range(self.size):
            print(self.values[i])
        