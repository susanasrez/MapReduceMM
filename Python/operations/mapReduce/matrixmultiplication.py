from mrjob.job import MRJob
import sys

class MRMatrixMultiplication(MRJob):

    def mapper(self, _, line):
        matrix, i, j, value = line.split()
        i, j = int(i), int(j)

        if matrix == 'A':
            for k in range(2):
                yield (i, k), ('A', j, float(value))
        else:
            for k in range(2):
                yield (k, j), ('B', i, float(value))

    def reducer(self, key, values):
        elements_A = {}
        elements_B = {}

        for matrix, index, value in values:
            if matrix == 'A':
                elements_A[index] = value
            else:
                elements_B[index] = value

        sum_product = sum(elements_A[k] * elements_B.get(k, 0) for k in elements_A)
        yield key, sum_product

if __name__ == '__main__':
    file = sys.argv[1]
    MRMatrixMultiplication(args=[file]).run()
