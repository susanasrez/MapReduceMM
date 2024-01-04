package matrixmultiplication.operators.densematrixmultiplication;

import matrixmultiplication.Matrix;
import matrixmultiplication.matrix.DenseMatrix;
import matrixmultiplication.operators.MatrixMultiplication;

public class DenseMatrixMultiplication implements MatrixMultiplication {

    @Override
    public Matrix multiply(Matrix matrix_a, Matrix matrix_b) {
        DenseMatrix a = (DenseMatrix) matrix_a;
        DenseMatrix b = (DenseMatrix) matrix_b;
        int[][] c = new int[a.size()][b.size()];
        for (int i = 0; i < a.size(); i++) {
            for (int j = 0; j < a.size();j++) {
                for (int k = 0; k < b.size(); k++) {
                    c[i][j] += a.get(i, k) * b.get(k, j);
                }
            }
        }
        return new DenseMatrix(c);
    }
}
