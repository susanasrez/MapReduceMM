class MatrixWriter:
    def __init__(self, matrix_a, filename):
        self.matrix_a = matrix_a
        self.filename = filename
        self.size = matrix_a.size

    
    def write_to_file_dense(self):
        file = open(self.filename, 'w')
        for i in range(self.size):
            for j in range(self.size):
                file.write(str(i) + ' ' + str(j) + ' ' + str(self.matrix_a.get(i, j)) + '\n')
        file.close()
    