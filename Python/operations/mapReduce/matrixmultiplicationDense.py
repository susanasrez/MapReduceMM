from mrjob.job import MRJob
from mrjob.step import MRStep

class MatrixMultiplication(MRJob):

    def configure_args(self):
        super(MatrixMultiplication, self).configure_args()
        self.add_passthru_arg('-n', '--size', type=int, default=3, help='Size of the matrix (N)')

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer)
        ]

    def mapper(self, _, line):
        N = self.options.size
        matrix, row, column, value = line.split()

        row = int(row)
        column = int(column)
        value = float(value)

        if matrix == 'A':
            for k in range(N):
                yield (row, k), ('A', column, value)
        
        elif matrix == 'B':
            for i in range(N):
                yield (i, column), ('B', row, value)

    def reducer(self, key, values):
        N = self.options.size
        A = [0]*N
        B = [0]*N

        for matrix, pos, value in values:
            if matrix == 'A':
                A[pos] = value
            else:
                B[pos] = value

        yield key, sum(a*b for a, b in zip(A, B))

if __name__ == '__main__':
    MatrixMultiplication.run()
