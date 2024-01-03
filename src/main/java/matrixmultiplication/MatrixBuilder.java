package matrixmultiplication;

public interface MatrixBuilder {
    void set(int i, int j, int value);

    void setMatrix(Matrix c);

    Matrix get();
}
