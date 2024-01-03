from matrixBuilders.coordinate_matrix_generator import CoordinateMatrixGenerator
from matrixBuilders.transformations import MatrixTransformations
from operations.original.denseMultiplication import DenseMatrixMultiplication
from checker.checker import Checker
import time, gc

densities = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
N = 512

def test_densities():
    for density in densities:
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

if __name__ == "__main__":
    test_densities()