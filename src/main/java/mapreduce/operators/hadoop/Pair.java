package mapreduce.operators.hadoop;

import org.apache.hadoop.io.WritableComparable;

import java.io.DataInput;
import java.io.DataOutput;
import java.io.IOException;

class Pair implements WritableComparable<Pair> {
    int row;
    int col;

    Pair() {
        row = 0;
        col = 0;
    }

    Pair(int row, int col) {
        this.row = row;
        this.col = col;
    }

    @Override
    public void readFields(DataInput input) throws IOException {
        row = input.readInt();
        col = input.readInt();
    }

    @Override
    public void write(DataOutput output) throws IOException {
        output.writeInt(row);
        output.writeInt(col);
    }

    @Override
    public int compareTo(Pair compare) {
        if (row > compare.row) {
            return 1;
        } else if (row < compare.row) {
            return -1;
        } else {
            if (col > compare.col) {
                return 1;
            } else if (col < compare.col) {
                return -1;
            }
        }
        return 0;
    }

    public String toString() {
        return row + " " + col + " ";
    }
}

