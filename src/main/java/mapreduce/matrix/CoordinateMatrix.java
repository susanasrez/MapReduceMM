package mapreduce.matrix;

import mapreduce.Matrix;

import java.util.Comparator;
import java.util.List;

public class CoordinateMatrix {

    public final int size;
    public final List<Coordinate> coordinates;

    public CoordinateMatrix(int size, List<Coordinate> coordinates) {
        this.size = size;
        this.coordinates = coordinates;
    }

    public int size() {
        return size;
    }

    public double get(int i, int j) {
        return coordinates.stream()
                .filter(c->c.i() == i & c.j() == j)
                .findFirst()
                .map(Coordinate::value)
                .orElse(0.0);
    }

    public Matrix getByRows() {
        coordinates.sort(new CoordinateComparator());
        return (Matrix) new CoordinateMatrix(size, coordinates);
    }

    public Matrix getSortCol() {
        coordinates.sort(new CoordinateComparatorByJ());
        return (Matrix) new CoordinateMatrix(size, coordinates);
    }

    private static class CoordinateComparator implements Comparator<Coordinate> {
        public int compare(Coordinate c1, Coordinate c2) {
            return Integer.compare(c1.i(), c2.i());
        }
    }

    private static class CoordinateComparatorByJ implements Comparator<Coordinate> {
        public int compare(Coordinate c1, Coordinate c2) {
            return Integer.compare(c1.j(), c2.j());
        }
    }
}