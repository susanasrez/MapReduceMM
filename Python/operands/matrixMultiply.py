from mrjob.job import MRJob

class MatrixMultiplyMR(MRJob):

    def configure_args(self):
        super(MatrixMultiplyMR, self).configure_args()
        self.add_passthru_arg('--matrixA', help='Path to input matrix A')
        self.add_passthru_arg('--matrixB', help='Path to input matrix B')

    def mapper(self, _, line):
        elements = line.split(',')
        matrix_name, i, j, value = elements
        i, j, value = int(i), int(j), float(value)

        if matrix_name == 'A':
            yield (i, j), ('A', value)
        elif matrix_name == 'B':
            yield (j, i), ('B', value)

    def reducer(self, key, values):
        values = list(values)
        a_values = [value for name, value in values if name == 'A']
        b_values = [value for name, value in values if name == 'B']

        if a_values and b_values:
            result = sum(a * b for a, b in zip(a_values, b_values))
            yield key, result

