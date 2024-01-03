import subprocess
import json
from writer.writeMatrix import MatrixWriter
import os
from matrixBuilders.coordinate_matrix_generator import CoordinateMatrixGenerator
from matrixBuilders.densematrixgenerator import DenseMatrixBuilder
from operations.original.denseMultiplication import DenseMatrixMultiplication
from matrixBuilders.transformations import MatrixTransformations
from checker.checker import Checker

N = 3
density = 0.5
matrix = CoordinateMatrixGenerator.generate_random_coordinate_matrix(N, density)
matrix.display()

transform = MatrixTransformations()
matrix1 = transform.transform(matrix)

c = DenseMatrixMultiplication().multiply(matrix1, matrix1)

