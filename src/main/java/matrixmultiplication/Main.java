package matrixmultiplication;

import matrixmultiplication.matrixbuilder.CoordinateMatrixGenerator;
import matrixmultiplication.matrixbuilder.DenseMatrixBuilder;
import matrixmultiplication.writer.txt.WriteTxt;
import matrixmultiplication.writer.Writer;


public class Main {

    public static void main(String[] args) {
        Matrix a = CoordinateMatrixGenerator.generateRandomCoordinateMatrix(3, 0.5);
        MatrixBuilder builder = new DenseMatrixBuilder(3);
        builder.setMatrix(a);
        Matrix matrix = builder.get();
        matrix.display();

        Writer writer = new WriteTxt();
        String filePath = "./src/main/resources/matrixA.txt";
        writer.writeMatrix(matrix, filePath);
        String filePath2 = "./src/main/resources/matrixB.txt";
        writer.writeMatrix(matrix, filePath2);
    }
}
