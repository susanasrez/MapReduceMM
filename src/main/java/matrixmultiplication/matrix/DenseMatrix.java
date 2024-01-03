package matrixmultiplication.matrix;
import matrixmultiplication.Matrix;

public class DenseMatrix implements Matrix {
    private final int[][] values;

    public DenseMatrix(int[][] values) {
        this.values = values;
    }

    @Override
    public int size() {
        return values.length;
    }

    @Override
    public int get(int i, int j) {
        return values[i][j];
    }

    @Override
    public void display(){
        int numCols = values[0].length;

        for (int[] value : values) {
            for (int j = 0; j < numCols; j++) {
                System.out.print(value[j] + " ");
            }
            System.out.println();
        }
    }
}