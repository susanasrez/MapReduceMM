from mrjob.job import MRJob
from mrjob.step import MRStep
import time
import numpy as np

class MatrixMultiplication(MRJob):

    def configure_args(self):
        super(MatrixMultiplication, self).configure_args()
        self.add_passthru_arg('-n', '--size', type=int, default=4, help='Size of the matrix (N)')

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer)
        ]

    def mapper(self, _, line):
        N = self.options.size
        row, column, value = map(float, line.split())

        for k in range(N):
            yield (int(row), k), ('A', int(column), value)

    def reducer(self, key, values):
        N = self.options.size
        A = np.zeros(N)

        for matrix, pos, value in values:
            A[pos] = value

        result = np.dot(A, A)
        yield key, result

if __name__ == '__main__':
    start = time.time()
    MatrixMultiplication.run()
    end = time.time()
    elapsed_time = (end - start)
    print("Time = " + str(elapsed_time) + " seconds")
