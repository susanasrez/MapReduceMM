package mapreduce.writer;

import mapreduce.Matrix;

import java.io.FileWriter;
import java.io.IOException;

public class Writer {

    public static void writeMatrixToFile(Matrix matrixA, Matrix matrixB, String filePath) {
        try (FileWriter writer = new FileWriter(filePath)) {
            int sizeA = matrixA.size();
            int sizeB = matrixB.size();

            for (int i = 0; i < sizeA; i++) {
                for (int j = 0; j < sizeA; j++) {
                    int valueA = matrixA.get(i, j);
                    if (valueA != 0) {
                        writer.write("A " + i + " " + j + " " + valueA + "\n");
                    }
                }
            }

            for (int i = 0; i < sizeB; i++) {
                for (int j = 0; j < sizeB; j++) {
                    int valueB = matrixB.get(i, j);
                    if (valueB != 0) {
                        writer.write("B " + i + " " + j + " " + valueB + "\n");
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
