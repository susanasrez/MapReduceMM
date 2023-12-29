package mapreduce;

public interface MatrixBuilder {
    void set(int i, int j, double value);

    void setMatrix(Matrix c);

    Matrix get();
}
