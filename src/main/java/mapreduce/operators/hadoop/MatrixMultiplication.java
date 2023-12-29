package mapreduce.operators.hadoop;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;

import java.io.IOException;

public class MatrixMultiplication {

    public static class MatrixMapper extends Mapper<Object, Text, Text, Text> {

        @Override
        protected void map(Object key, Text value, Context context) throws IOException, InterruptedException {
            String[] tokens = value.toString().split(" ");
            String matrix = tokens[0];
            int row = Integer.parseInt(tokens[1]);
            int column = Integer.parseInt(tokens[2]);
            float val = Float.parseFloat(tokens[3]);
            int size = context.getConfiguration().getInt("matrix.size", 3);

            if (matrix.equals("A")) {
                for (int k = 0; k < size; k++) {
                    context.write(new Text(row + " " + k), new Text("A " + column + " " + val));
                }
            } else if (matrix.equals("B")) {
                for (int i = 0; i < size; i++) {
                    context.write(new Text(i + " " + column), new Text("B " + row + " " + val));
                }
            }
        }
    }

    public static class MatrixReducer extends Reducer<Text, Text, Text, FloatWritable> {

        @Override
        protected void reduce(Text key, Iterable<Text> values, Context context) throws IOException, InterruptedException {
            int size = context.getConfiguration().getInt("matrix.size", 3);
            float[] A = new float[size];
            float[] B = new float[size];

            for (Text val : values) {
                String[] tokens = val.toString().split(" ");
                String matrix = tokens[0];
                int pos = Integer.parseInt(tokens[1]);
                float value = Float.parseFloat(tokens[2]);

                if (matrix.equals("A")) {
                    A[pos] = value;
                } else if (matrix.equals("B")) {
                    B[pos] = value;
                }
            }

            float result = 0.0f;
            for (int i = 0; i < size; i++) {
                result += A[i] * B[i];
            }

            context.write(key, new FloatWritable(result));
        }
    }

    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        String inputPath= "C:\\Users\\Susana\\Desktop\\Universidad\\Tercero\\Primer\\BD\\MapReduceMM\\Java\\src\\main\\resources\\matrices.txt";
        String outputPath = "C:\\Users\\Susana\\Desktop\\Universidad\\Tercero\\Primer\\BD\\MapReduceMM\\Java\\src\\main\\resources\\resultado.txt";

        conf.setInt("matrix.size", Integer.parseInt(String.valueOf(3))); // Tamaño de la matriz

        Job job = Job.getInstance(conf, "Matrix Multiplication");
        job.setJarByClass(MatrixMultiplication.class);
        job.setInputFormatClass(TextInputFormat.class);
        job.setOutputFormatClass(TextOutputFormat.class);
        job.setMapperClass(MatrixMapper.class);
        job.setReducerClass(MatrixReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(FloatWritable.class);

        TextInputFormat.addInputPath(job, new Path(inputPath));
        TextOutputFormat.setOutputPath(job, new Path(outputPath));

        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}