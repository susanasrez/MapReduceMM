from matrixBuilders.coordinate_matrix_generator import CoordinateMatrixGenerator
from writer.writeMatrix import MatrixWriter
from matrixBuilders.transformations import MatrixTransformations
from matrix.denseMatrix import DenseMatrix
from Checker.checker import Checker
import subprocess, time, gc

N = [8, 16, 32, 64, 128, 256, 512, 1024]

density = 0.7
script_path = './operations/mapReduce/mapreducemultiplication.py'
filePath = "./results/matrix.txt"
resultsPath = "./results/result.txt"

def test_map_reduce():
    for n in N:
        matrix = CoordinateMatrixGenerator.generate_random_coordinate_matrix(n, density)
        transform = MatrixTransformations()
        matrixA = transform.transform(matrix)
        
        print("Writing to file...")
        start = time.time()
        writer = MatrixWriter(matrixA, filePath)
        writer.write_to_file_dense()
        end = time.time()
        elapsed_time = (end - start)
        print("N = " + str(n) + " Writing Time = " + str(elapsed_time) + " seconds")


        print("Multiplying...")
        subprocess.run(['python', script_path, '--size', str(n), filePath])

        start = time.time()
        with open(resultsPath, 'w') as output_file:
            process = subprocess.Popen(['python', script_path, '--size', str(n), filePath], stdout=output_file)
            process.wait()
        
        
        end = time.time()
        elapsed_time = (end - start)
        print("N = " + str(n) + " Time = " + str(elapsed_time) + " seconds")

        result = DenseMatrix.read_result(resultsPath, n)
        Checker.test_dense(matrixA, matrixA, result)

        print("----------------------------------------------------------------------------------")
        print(" ")

        del matrix
        del matrixA
        del result
        del transform
        gc.collect()


if __name__ == "__main__":
    test_map_reduce()