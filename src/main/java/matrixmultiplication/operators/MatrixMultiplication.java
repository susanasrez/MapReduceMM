package matrixmultiplication.operators;

import matrixmultiplication.Matrix;

public interface MatrixMultiplication {
    Matrix multiply(Matrix matrix_a, Matrix matrix_b);
}