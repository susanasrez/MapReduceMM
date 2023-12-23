from denseMatrix.randomMatrix import RandomMatrixGenerator
from operands.matrixMultiply import MatrixMultiplyMR

if __name__ == '__main__':
    N = 4
    density = 0.6

    generator = RandomMatrixGenerator(N, density)
    matrix_A = generator.generate_matrix()
    matrix_B = generator.generate_matrix()

    job = MatrixMultiplyMR(args=['--matrixA', 'matrixA.txt', '--matrixB', 'matrixB.txt'])

    with open('matrixA.txt', 'w') as file_A, open('matrixB.txt', 'w') as file_B:
        for row in matrix_A:
            file_A.write(','.join(map(str, row)) + '\n')
        for row in matrix_B:
            file_B.write(','.join(map(str, row)) + '\n')

    job.run()
