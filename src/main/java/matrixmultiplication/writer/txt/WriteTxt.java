package matrixmultiplication.writer.txt;

import matrixmultiplication.Matrix;
import matrixmultiplication.writer.Writer;

import java.io.FileWriter;
import java.io.IOException;

public class WriteTxt implements Writer {

    @Override
    public void writeMatrix(Matrix matrix, String filePath) {
        try (FileWriter writer = new FileWriter(filePath)) {
            int size = matrix.size();
            for (int i = 0; i < size; i++) {
                for (int j = 0; j < size; j++) {
                    double value = matrix.get(i, j);
                    writer.write(i + "," + j + "," + value + "\n");
                }
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
