package hadoop;

import matrixmultiplication.Matrix;
import matrixmultiplication.MatrixBuilder;
import matrixmultiplication.checker.Checker;
import matrixmultiplication.matrixbuilder.CoordinateMatrixGenerator;
import matrixmultiplication.matrixbuilder.DenseMatrixBuilder;
import matrixmultiplication.operators.hadoop.Multiply;
import matrixmultiplication.writer.Writer;
import matrixmultiplication.writer.txt.WriteTxt;

import java.util.ArrayList;
import java.util.List;

public class HadoopTime {

    private static String filePathA;
    private static String filePathB;
    private static String temp;
    private static String resultPath;


    public static void main(String[] args) throws Exception {
        filePathA = args[0];
        filePathB = args[1];
        temp = args[2];
        resultPath = args[3];

        test();

    }

    public static void test() throws Exception {
        List<Integer> N = new ArrayList<>(List.of(8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096));

        for (Integer n: N){
            Matrix a = CoordinateMatrixGenerator.generateRandomCoordinateMatrix(n, 0.7);
            MatrixBuilder builder = new DenseMatrixBuilder(n);
            builder.setMatrix(a);
            Matrix matrix = builder.get();

            long start = System.currentTimeMillis();
            writeMatrices(matrix);
            long end = System.currentTimeMillis();
            double time = (double) (end - start);
            System.out.println("N = " + n + "Write time = " + time + " milliseconds");

            double elapsedTime = setUp();
            System.out.println("N = " + n + " Time = " + elapsedTime + " milliseconds");
            boolean check = Checker.testHadoop(matrix, resultPath);
            System.out.println("The multiplication is "+ check);
            System.out.println("-----------------------------------------------------------");
        }
    }

    public static void writeMatrices(Matrix matrix){
        Writer writer = new WriteTxt();
        writer.writeMatrix(matrix, filePathA);
        writer.writeMatrix(matrix, filePathB);
    }

    public static double setUp() throws Exception {
        long start = System.currentTimeMillis();
        Multiply.setUp(filePathA, filePathB, temp, resultPath);
        long end = System.currentTimeMillis();
        return (double) (end - start);
    }

}
