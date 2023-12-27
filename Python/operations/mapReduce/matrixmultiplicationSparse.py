from mrjob.job import MRJob
from mrjob.step import MRStep

class SparseMatrixMultiplication(MRJob):

    def configure_args(self):
        super(SparseMatrixMultiplication, self).configure_args()
        self.add_passthru_arg('-n', '--size', type=int, default=3, help='Size of the matrix (N)')

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer)
        ]

    def mapper(self, _, line):
        N = self.options.size
        elements = [int(x) for x in line.split()]

        if self.get_current_line_number() <= 3:
            # Matrix A in CRS format
            row_ptr = elements
            for i in range(len(row_ptr) - 1):
                for idx in range(row_ptr[i], row_ptr[i+1]):
                    for k in range(N):
                        yield (i, k), ('A', idx, 1)  # Assuming value is 1 for simplicity

        else:
            # Matrix B in CSS format
            col_ptr = elements
            for j in range(len(col_ptr) - 1):
                for idx in range(col_ptr[j], col_ptr[j+1]):
                    for i in range(N):
                        yield (i, j), ('B', idx, 1)  # Assuming value is 1 for simplicity

    def reducer(self, key, values):
        N = self.options.size
        A = [0] * N
        B = [0] * N

        for matrix, pos, value in values:
            if matrix == 'A':
                A[pos] = value
            else:
                B[pos] = value

        yield key, sum(a * b for a, b in zip(A, B))

if __name__ == '__main__':
    SparseMatrixMultiplication.run()
