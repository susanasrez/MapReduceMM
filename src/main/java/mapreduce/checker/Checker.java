package mapreduce.checker;

import mapreduce.Matrix;
import mapreduce.matrix.DenseMatrix;
import mapreduce.operators.MatrixMultiplication;
import mapreduce.operators.matrixmultiplication.DenseMatrixMultiplication;

public class Checker {

    public static boolean testDense(Matrix a, Matrix b, Matrix c) {
        MatrixMultiplication multiplier = new DenseMatrixMultiplication();
        Matrix ab = multiplier.multiply(a, b);
        Matrix ab_c = multiplier.multiply(ab, c);
        Matrix bc = multiplier.multiply(b, c);
        Matrix a_bc = multiplier.multiply(a, bc);
        return areMatricesEqual(ab_c, a_bc);
    }

    public static boolean areMatricesEqual(Matrix matrix1, Matrix matrix2) {
        double epsilon = 1E-8;
        DenseMatrix a = (DenseMatrix) matrix1;
        DenseMatrix b = (DenseMatrix) matrix2;
        for (int i = 0; i < a.size(); i++) {
            for (int j = 0; j < a.size(); j++) {
                if ((Math.abs(a.get(i, j) - b.get(i, j)) > epsilon)) {
                    return false;
                }
            }
        }
        return true;
    }
}
