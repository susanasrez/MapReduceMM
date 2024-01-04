package hadoop;

import matrixmultiplication.Matrix;
import matrixmultiplication.MatrixBuilder;
import matrixmultiplication.checker.Checker;
import matrixmultiplication.matrixbuilder.CoordinateMatrixGenerator;
import matrixmultiplication.matrixbuilder.DenseMatrixBuilder;
import matrixmultiplication.operators.hadoop.Multiply;
import matrixmultiplication.writer.Writer;
import matrixmultiplication.writer.txt.WriteTxt;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.time.Duration;
import java.time.Instant;
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
        List<Integer> N = new ArrayList<>(List.of(8, 16, 32, 64, 128, 256, 512, 1024));

        for (Integer n: N){
            Matrix a = CoordinateMatrixGenerator.generateRandomCoordinateMatrix(n, 0.7);
            MatrixBuilder builder = new DenseMatrixBuilder(n);
            builder.setMatrix(a);
            Matrix matrix = builder.get();

            Instant start = Instant.now();
            writeMatrices(matrix);
            Instant end = Instant.now();
            Duration time = Duration.between(start, end);
            System.out.println("N = " + n + " Write time = " + time.toMillis() + " milliseconds");

            long start2 = System.currentTimeMillis();
            String[] multiplyArgs = new String[]{filePathA, filePathB, temp , resultPath};
            Multiply.main(multiplyArgs);
            long end2 = System.currentTimeMillis();
            double elapsedTime = (double) (end2 - start2);
            System.out.println("N = " + n + " Time = " + elapsedTime + " milliseconds");


            String path = resultPath + "/part-r-00000";
            boolean check = Checker.testHadoop(matrix, path);
            System.out.println("The multiplication is "+ check);
            System.out.println("-----------------------------------------------------------");

            delete();


        }
    }

    public static void writeMatrices(Matrix matrix){
        Writer writer = new WriteTxt();
        writer.writeMatrix(matrix, filePathA);
        writer.writeMatrix(matrix, filePathB);
    }

    public static void delete() throws IOException {
        Path temporary = Paths.get(temp);
        Files.walk(temporary)
                .sorted((x, y) -> y.toString().length() - x.toString().length())
                .forEach(route -> {
                    try {
                        Files.delete(route);
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                });
        Path res = Paths.get(resultPath);
        Files.walk(res)
                .sorted((x, y) -> y.toString().length() - x.toString().length())
                .forEach(route -> {
                    try {
                        Files.delete(route);
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                });
    }

}
