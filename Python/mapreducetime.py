from matrixBuilders.coordinate_matrix_generator import CoordinateMatrixGenerator
from writer.writeMatrix import MatrixWriter
from matrixBuilders.transformations import MatrixTransformations
from matrix.denseMatrix import DenseMatrix
from checker.checker import Checker
import subprocess, time, gc

#N = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576,2097152]
#N = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]  
N = 8
density = 0.7
script_path = './operations/mapReduce/matrixmultiplicationDense.py'
filePath = "./results/test.txt"

def test_map_reduce():
    for n in N:
        matrix = CoordinateMatrixGenerator.generate_random_coordinate_matrix(n, density)
        transform = MatrixTransformations()
        matrixA = transform.transform(matrix)
        
        print("Writing to file...")
        start = time.time()
        writer = MatrixWriter(matrixA, matrixA, filePath)
        writer.write_to_file_dense()
        end = time.time()
        elapsed_time = (end - start)
        print("N = " + str(n) + " Writing Time = " + str(elapsed_time) + " seconds")

        
        start = time.time()
        subprocess.call(['python', script_path, '--size', str(N), filePath])
        end = time.time()
        elapsed_time = (end - start)
        print("N = " + str(n) + " Time = " + str(elapsed_time) + " seconds")

        result = DenseMatrix.read_result(filePath)
        result.display()
        Checker.test_dense(matrixA, matrixA, result)

        print("----------------------------------------------------------------------------------")

        del matrix
        del matrixA
        del result
        del transform
        gc.collect()


if __name__ == "__main__":
    test_map_reduce()