package mapreduce.matrixbuilders;

import mapreduce.Matrix;
import mapreduce.MatrixBuilder;
import mapreduce.matrix.CoordinateMatrix;
import mapreduce.matrix.DenseMatrix;

public class DenseMatrixBuilder implements MatrixBuilder {
    private final int size;
    private final int[][] values;

    public DenseMatrixBuilder(int size) {
        this.size = size;
        this.values = new int[size][size];
    }

    @Override
    public void set(int i, int j, int value) {
        values[i][j] = value;
    }

    @Override
    public void setMatrix(Matrix coordinateMatrix) {
        CoordinateMatrix coordMatrix = (CoordinateMatrix) coordinateMatrix;
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                int value = coordMatrix.get(i, j);
                set(i, j, value);
            }
        }
    }

    @Override
    public Matrix get() {
        return new DenseMatrix(values);
    }
}
