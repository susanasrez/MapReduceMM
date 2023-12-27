import subprocess
from writer.writeMatrix import MatrixWriter
import os
from matrixBuilders.coordinate_matrix_generator import CoordinateMatrixGenerator
from matrixBuilders.compressedRowbuilder import CompressedRowMatrixBuilder
from matrixBuilders.compressedColumnbuilder import CompressedColumnMatrixBuilder
from matrixBuilders.densematrixgenerator import DenseMatrixBuilder
from operations.original.denseMultiplication import DenseMatrixMultiplication
from matrixBuilders.transformations import MatrixTransformations
from operations.original.sparseMultiplication import SparseMatrixMultiplication


def obtain_route():
    route = os.path.abspath(os.getcwd()).split('\\')
    route.pop()
    route = '/'.join(route)
    route = route + '/results/matrix.txt'
    return route


N = 3
density = 0.5
matrix = CoordinateMatrixGenerator.generate_random_coordinate_matrix(N, density)
matrix.display()

transform = MatrixTransformations()
matrix1 = transform.transform(matrix)

DenseMatrixMultiplication().multiply(matrix1, matrix1).display()


matrixA = transform.transformCOO_CRS(matrix)
matrixB = transform.transformCOO_CCS(matrix)

MatrixWriter(matrixA, matrixB, './results/matrix_sparse.txt').write_to_file_Sparse()

SparseMatrixMultiplication().multiply(matrixA, matrixB).display()

#MatrixWriter(matrixA, matrixB, './results/matrix.txt').write_to_file_dense()

#file = './results/matrix.txt'
#script_path = './operations/mapReduce/matrixmultiplicationDense.py'
#subprocess.call(['python', script_path, '--size', str(N), file])


file = './results/matrix_sparse.txt'
script_path = './operations/mapReduce/matrixmultiplicationSparse.py'
subprocess.call(['python', script_path, '--size', str(N), file])