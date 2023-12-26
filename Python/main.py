<<<<<<< HEAD
import subprocess
from generator.densematrixgenerator import RandomDenseMatrix
from generator.coordinate_matrix_generator import CoordinateMatrixGenerator
from writer.writeMatrix import MatrixWriter
import os
from operations.original.matrixmultiplier import MatrixMultiply
from writer.writeOriginal import WriteOriginal

def obtain_route():
    route = os.path.abspath(os.getcwd()).split('\\')
    route.pop()
    route = '/'.join(route)
    route = route + '/results/matrix.txt'
    return route


N = 2
density = 0.5
matrixA = CoordinateMatrixGenerator(N, density).matrix
matrixB = CoordinateMatrixGenerator(N, density).matrix
matrixC = MatrixMultiply.multiplyCOO(matrixA, matrixB)
matrixC.display_matrix()

#route = obtain_route()
#MatrixWriter(matrixA, matrixB, './results/matrix.txt').write_to_file_COO()

#file = './results/matrix.txt'
#subprocess.call(['python', './operations/mapReduce/matrixmultiplication.py', file])


=======
import subprocess
from generator.densematrixgenerator import RandomDenseMatrix
from generator.coordinate_matrix_generator import CoordinateMatrixGenerator
from writer.writeMatrix import MatrixWriter
import os
from operations.original.matrixmultiplier import MatrixMultiply
from writer.writeOriginal import WriteOriginal

def obtain_route():
    route = os.path.abspath(os.getcwd()).split('\\')
    route.pop()
    route = '/'.join(route)
    route = route + '/results/matrix.txt'
    return route


N = 2
density = 0.5
matrixA = CoordinateMatrixGenerator(N, density).matrix
matrixB = CoordinateMatrixGenerator(N, density).matrix
matrixC = MatrixMultiply.multiplyCOO(matrixA, matrixB)
matrixC.display_matrix()

#route = obtain_route()
#MatrixWriter(matrixA, matrixB, './results/matrix.txt').write_to_file_COO()

#file = './results/matrix.txt'
#subprocess.call(['python', './operations/mapReduce/matrixmultiplication.py', file])


>>>>>>> de04ad2f6ef91015c4474ce6a213a0486b842092
