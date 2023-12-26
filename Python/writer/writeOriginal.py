<<<<<<< HEAD

class WriteOriginal:

    def __init__(self, path):
        self.path = path
    
    def writeDense(self, matrix):
        file = open(self.path, 'w')
        for i in range(matrix.N):
            for j in range(matrix.N):
                file.write(str(matrix.matrix[i][j]) + ' ')
            file.write('\n')
        file.close()
=======

class WriteOriginal:

    def __init__(self, path):
        self.path = path
    
    def writeDense(self, matrix):
        file = open(self.path, 'w')
        for i in range(matrix.N):
            for j in range(matrix.N):
                file.write(str(matrix.matrix[i][j]) + ' ')
            file.write('\n')
        file.close()
>>>>>>> de04ad2f6ef91015c4474ce6a213a0486b842092
