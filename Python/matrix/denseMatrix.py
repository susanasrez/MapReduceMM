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
    
    @staticmethod
    def read_result(filePath,n):
        try:
            with open(filePath, 'r') as file:
                lines = file.readlines()
                matrix = [[0.0 for _ in range(n)] for _ in range(n)]
                for line in lines:
                    parts = line.strip().split("\t")
                    coordinates = parts[0].strip("[]").split(",")
                    row, col = int(coordinates[0]), int(coordinates[1]) 
                    value = float(parts[1])
                    matrix[row][col] = value
                return DenseMatrix(matrix)
        except FileNotFoundError:
            raise Exception("File not found: " + filePath)

        