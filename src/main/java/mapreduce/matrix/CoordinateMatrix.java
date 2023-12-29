package mapreduce.matrix;

import mapreduce.Matrix;
import java.util.List;

public class CoordinateMatrix implements Matrix{

    public final int size;
    public final List<Coordinate> coordinates;

    public CoordinateMatrix(int size, List<Coordinate> coordinates) {
        this.size = size;
        this.coordinates = coordinates;
    }

    public int size() {
        return size;
    }

    public int get(int i, int j) {
        return coordinates.stream()
                .filter(c->c.i() == i & c.j() == j)
                .findFirst()
                .map(Coordinate::value)
                .orElse(0);
    }

    @Override
    public void display() {
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                double value = get(i, j);
                System.out.println("i = " + i + ", j = " + j + ", value = " + value);
            }
        }
    }

}