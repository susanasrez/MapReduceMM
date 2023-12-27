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
    
    def write_to_file_COO(self):
        with open(self.filename, 'w') as file:
                for label, matrix in [("A", self.matrix_a), ("B", self.matrix_b)]:
                    for i in range(self.size):
                        for j in range(self.size):
                            value = matrix.get(i, j)
                            if value != 0:
                                file.write(f"{label} {i} {j} {value}\n")

    def write_to_file_Sparse(self):
        with open(self.filename, 'w') as file:

            file.write(" ".join(map(str, self.matrix_a.row_pointers)) + "\n")
            file.write(" ".join(map(str, self.matrix_a.col_indices)) + "\n")
            file.write(" ".join(map(str, self.matrix_a.values)) + "\n")

            file.write(" ".join(map(str, self.matrix_b.column_pointers)) + "\n")
            file.write(" ".join(map(str, self.matrix_b.row_ind)) + "\n")
            file.write(" ".join(map(str, self.matrix_b.values)) + "\n")
    
