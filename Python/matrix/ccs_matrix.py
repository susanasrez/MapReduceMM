class CompressorCCSMatrix():
    def __init__(self, size, column_pointers, row_indices, values):
        self.size = size
        self.column_pointers = column_pointers
        self.row_ind = row_indices
        self.values = values

    def size(self):
        return self.size

    def get(self, i, j):
        col_start = self.column_pointers[j]
        col_end = self.column_pointers[j + 1]

        for k in range(col_start, col_end):
            if self.row_ind[k] == i:
                return self.values[k]

        return 0.0
    
    def display(self):
        print("Size: " + str(self.size))
        print("Column pointers: ")
        print(self.column_pointers)
        print("Row indices: ")
        print(self.row_ind)
        print("Values: ")
        print(self.values)
