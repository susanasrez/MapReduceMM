package mapreduce.operators;

import mapreduce.Matrix;

public interface MatrixMultiplication {
    Matrix multiply(Matrix matrix_a, Matrix matrix_b);
}