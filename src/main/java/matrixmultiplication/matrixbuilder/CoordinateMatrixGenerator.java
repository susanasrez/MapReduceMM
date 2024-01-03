package matrixmultiplication.matrixbuilder;

import matrixmultiplication.Matrix;
import matrixmultiplication.MatrixBuilder;
import matrixmultiplication.matrix.Coordinate;
import matrixmultiplication.matrix.CoordinateMatrix;

import java.util.*;

public class CoordinateMatrixGenerator implements MatrixBuilder {

    public static CoordinateMatrix generateRandomCoordinateMatrix(int n, double density) {
        if (density < 0.0 || density > 1.0) {
            throw new IllegalArgumentException("Density must be in the range [0, 1].");
        }

        List<Coordinate> coordinates = new ArrayList<>();
        Random random = new Random();
        int totalNonZeroElements = (int) Math.round(n * n * density);
        Set<Integer> usedCoordinates = new HashSet<>();

        while (coordinates.size() < totalNonZeroElements) {
            int row, col;
            do {
                row = random.nextInt(n);
                col = random.nextInt(n);
            } while (!usedCoordinates.add(row * n + col));

            int value = random.nextInt(101);
            coordinates.add(new Coordinate(row, col, value));
        }

        return new CoordinateMatrix(n, coordinates);
    }

    @Override
    public void set(int i, int j, int value) {

    }

    @Override
    public void setMatrix(Matrix c) {
    }

    @Override
    public Matrix get() {
        return null;
    }
}