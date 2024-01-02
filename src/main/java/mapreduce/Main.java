package mapreduce;

import mapreduce.matrixbuilders.CoordinateMatrixGenerator;
import mapreduce.matrixbuilders.DenseMatrixBuilder;
import mapreduce.writer.Writer;


public class Main {

    public static void main(String[] args) {
        Matrix a = CoordinateMatrixGenerator.generateRandomCoordinateMatrix(3, 0.5);
        MatrixBuilder builder = new DenseMatrixBuilder(3);
        builder.setMatrix(a);
        Matrix matrix = builder.get();
        matrix.display();

        String filePath = "./src/main/resources/matrixA.txt";
        Writer.writeMatrixToTxt(matrix, filePath);
        String filePath2 = "./src/main/resources/matrixB.txt";
        Writer.writeMatrixToTxt(matrix, filePath2);
    }
}
