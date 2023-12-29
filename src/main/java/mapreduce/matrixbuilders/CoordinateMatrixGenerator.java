package mapreduce.matrixbuilders;

import mapreduce.Matrix;
import mapreduce.MatrixBuilder;
import mapreduce.matrix.Coordinate;
import mapreduce.matrix.CoordinateMatrix;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class CoordinateMatrixGenerator implements MatrixBuilder {

    public static CoordinateMatrix generateRandomCoordinateMatrix(int n, double density) {
        if (density < 0.0 || density > 1.0) {
            throw new IllegalArgumentException("Density must be in the range [0, 1].");
        }

        List<Coordinate> coordinates = new ArrayList<>();
        Random random = new Random();
        int totalNonZeroElements = (int) Math.round(n * n * density);

        for (int i = 0; i < totalNonZeroElements; i++) {
            int row = 0, col = 0;
            boolean isUnique = false;
            while (!isUnique) {
                row = random.nextInt(n);
                col = random.nextInt(n);
                isUnique = !containsCoordinate(coordinates, row, col);
            }

            double value = random.nextDouble();
            coordinates.add(new Coordinate(row, col, value));
        }

        return new CoordinateMatrix(n, coordinates);
    }

    private static boolean containsCoordinate(List<Coordinate> coordinates, int row, int col) {
        for (Coordinate coordinate : coordinates) {
            if (coordinate.i() == row && coordinate.j() == col) {
                return true;
            }
        }
        return false;
    }

    @Override
    public void set(int i, int j, double value) {
    }

    @Override
    public void setMatrix(Matrix c) {
    }

    @Override
    public Matrix get() {
        return null;
    }
}