<<<<<<< HEAD
class MatrixWriter:
    def __init__(self, matrix_a, matrix_b, filename):
        self.matrix_a = matrix_a
        self.matrix_b = matrix_b
        self.filename = filename

    def write_to_file_Dense(self):
        with open(self.filename, 'w') as file:
            for i in range(self.matrix_a.N):
                for j in range(self.matrix_a.N):
                    value = self.matrix_a.matrix[i][j]
                    if value != 0:
                        file.write(f'A {i} {j} {value}\n')

            for i in range(self.matrix_b.N):
                for j in range(self.matrix_b.N):
                    value = self.matrix_b.matrix[i][j]
                    if value != 0:
                        file.write(f'B {i} {j} {value}\n')
    
    def write_to_file_COO(self):
        with open(self.filename, 'w') as file:
            for element in self.matrix_a.elements:
                file.write(f'A {element[0]} {element[1]} {element[2]}\n')

            for element in self.matrix_b.elements:
=======
class MatrixWriter:
    def __init__(self, matrix_a, matrix_b, filename):
        self.matrix_a = matrix_a
        self.matrix_b = matrix_b
        self.filename = filename

    def write_to_file_Dense(self):
        with open(self.filename, 'w') as file:
            for i in range(self.matrix_a.N):
                for j in range(self.matrix_a.N):
                    value = self.matrix_a.matrix[i][j]
                    if value != 0:
                        file.write(f'A {i} {j} {value}\n')

            for i in range(self.matrix_b.N):
                for j in range(self.matrix_b.N):
                    value = self.matrix_b.matrix[i][j]
                    if value != 0:
                        file.write(f'B {i} {j} {value}\n')
    
    def write_to_file_COO(self):
        with open(self.filename, 'w') as file:
            for element in self.matrix_a.elements:
                file.write(f'A {element[0]} {element[1]} {element[2]}\n')

            for element in self.matrix_b.elements:
>>>>>>> de04ad2f6ef91015c4474ce6a213a0486b842092
                file.write(f'B {element[0]} {element[1]} {element[2]}\n')