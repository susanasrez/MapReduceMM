class CRSMatrix:

    def __init__(self, rows_ptr, cols, vals):
        self.rows_ptr = rows_ptr
        self.cols = cols
        self.vals = vals
    
    def display_matrix(self):
        print("rows: ", self.rows_ptr)
        print("cols: ", self.cols)
        print("vals: ", self.vals)
