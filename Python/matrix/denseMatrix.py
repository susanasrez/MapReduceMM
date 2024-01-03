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

    @staticmethod
    def read_from_file(filePath):
        try:
            with open(filePath, 'r') as file:
                lines = file.readlines()
                values = []
                for line in lines:
                    row = [int(x) for x in line.strip().split()]
                    values.append(row)
                return DenseMatrix(values)
        except FileNotFoundError:
            raise Exception("File not found: " + filePath)
        