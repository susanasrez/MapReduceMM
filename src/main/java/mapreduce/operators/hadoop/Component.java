package mapreduce.operators.hadoop;

import org.apache.hadoop.io.Writable;

import java.io.DataInput;
import java.io.DataOutput;
import java.io.IOException;

class Component implements Writable {
    int target;
    int index;
    double value;

    Component() {
        target = 0;
        index = 0;
        value = 0.0;
    }

    Component(int tag, int index, double value) {
        this.target = tag;
        this.index = index;
        this.value = value;
    }

    @Override
    public void readFields(DataInput input) throws IOException {
        target = input.readInt();
        index = input.readInt();
        value = input.readDouble();
    }

    @Override
    public void write(DataOutput output) throws IOException {
        output.writeInt(target);
        output.writeInt(index);
        output.writeDouble(value);
    }
}
