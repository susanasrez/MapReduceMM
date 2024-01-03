package sequential;

import matrixmultiplication.Matrix;
import matrixmultiplication.MatrixBuilder;
import matrixmultiplication.checker.Checker;
import matrixmultiplication.matrixbuilder.CoordinateMatrixGenerator;
import matrixmultiplication.matrixbuilder.DenseMatrixBuilder;
import matrixmultiplication.operators.MatrixMultiplication;
import matrixmultiplication.operators.densematrixmultiplication.DenseMatrixMultiplication;

import java.util.ArrayList;
import java.util.List;

public class SequentialTime {

    public static void main(String[] args) {
        List<Integer> N = new ArrayList<>(List.of(8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096));
        MatrixMultiplication multiplier = new DenseMatrixMultiplication();

        for (Integer n: N) {

            Matrix matrixA = CoordinateMatrixGenerator.generateRandomCoordinateMatrix(n, 0.7);
            MatrixBuilder builder = new DenseMatrixBuilder(n);
            builder.setMatrix(matrixA);
            Matrix matrix = builder.get();

            long start = System.currentTimeMillis();
            Matrix result = multiplier.multiply(matrix, matrix);
            long end = System.currentTimeMillis();

            double elapsedTime = (double) (end - start);
            System.out.println("N = " + n + " Time = " + elapsedTime + " milliseconds");
            boolean check = Checker.testDense(matrix, matrix, result);
            System.out.println("The multiplication is "+ check);
            System.out.println("-----------------------------------------------------------");

            matrixA = null;
            builder = null;
            matrix = null;
            result = null;
        }
    }

}
