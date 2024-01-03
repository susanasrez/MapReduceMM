from matrixBuilders.coordinate_matrix_generator import CoordinateMatrixGenerator
from operations.original.denseMultiplication import DenseMatrixMultiplication
from matrixBuilders.transformations import MatrixTransformations
import time
from Checker.checker import Checker
import gc

N = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
density = 0.7

for n in N:
    #medir tiempo de creación
    matrix = CoordinateMatrixGenerator.generate_random_coordinate_matrix(n, density)
    transform = MatrixTransformations()
    matrixA = transform.transform(matrix)

    print("Multiplying...")
    start = time.time()
    result = DenseMatrixMultiplication().multiply(matrixA, matrixA)
    end = time.time()
    elapsed_time = (end - start) * 1000
    print("N = " + str(n) + " Time = " + str(elapsed_time) + " milliseconds")
    Checker.test_dense(matrixA, matrixA, result)
    print("----------------------------------------------------------------------------------")
    
    del matrix
    del matrixA
    del result
    del transform
    gc.collect()


    
    
