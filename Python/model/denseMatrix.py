class DenseMatrix:

    def __init__(self, matrix, N):
        self.matrix = matrix
        self.N = N
    
    def display_matrix(self):
        for i in range(self.N):
            for j in range(self.N):
                print(self.matrix[i][j], end=' ')
            print()
        print()
        