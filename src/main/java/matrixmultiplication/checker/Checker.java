package matrixmultiplication.checker;

import matrixmultiplication.Matrix;
import matrixmultiplication.matrix.DenseMatrix;
import matrixmultiplication.operators.MatrixMultiplication;
import matrixmultiplication.operators.densematrixmultiplication.DenseMatrixMultiplication;

import java.io.*;
import java.util.Scanner;

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

    public static boolean testHadoop(Matrix matrix, String resultPath) throws IOException {
        int n = matrix.size();
        Matrix result = readResult(resultPath, n);
        return testDense(matrix, matrix, result);
    }

    public static Matrix readResult(String path, int n) throws FileNotFoundException {
        File file = new File(path);
        Scanner scanner = new Scanner(file);

        int rows = n;
        int columns = n;
        int[][] values = new int[rows][columns];

        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            String[] parts = line.split("\\s+");
            int i = Integer.parseInt(parts[0]);
            int j = Integer.parseInt(parts[1]);
            int value = Integer.parseInt(parts[2]);

            values[i][j] = value;
        }

        scanner.close();

        return new DenseMatrix(values);
    }
}
