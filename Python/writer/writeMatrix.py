import json

class MatrixWriter:
    def __init__(self, matrix_a, matrix_b, filename):
        self.matrix_a = matrix_a
        self.matrix_b = matrix_b
        self.filename = filename
        self.size = matrix_a.size

    
    def write_to_file_dense(self):
        file = open(self.filename, 'w')
        for i in range(self.size):
            for j in range(self.size):
                file.write('A ' + str(i) + ' ' + str(j) + ' ' + str(self.matrix_a.get(i, j)) + '\n')

        for i in range(self.size):
            for j in range(self.size):
                file.write('B ' + str(i) + ' ' + str(j) + ' ' + str(self.matrix_b.get(i, j)) + '\n')

        file.close()
    