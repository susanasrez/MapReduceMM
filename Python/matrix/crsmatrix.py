class CompressorCRSMatrix():

    def __init__(self, size, row_pointers, col_indices, values):
        self.size = size
        self.row_pointers = row_pointers
        self.col_indices = col_indices
        self.values = values

    def size(self):
        return self.size

    def get(self, i, j):
        row_start = self.row_pointers[i]
        row_end = self.row_pointers[i]
        return next((self.values[k] for k in range(row_start, row_end) if self.col_indices[k] == j), 0)

    def display(self):
        print("Size: " + str(self.size))
        print("Row pointers: ")
        print(self.row_pointers)
        print("Col indices: ")
        print(self.col_indices)
        print("Values: ")
        print(self.values)
