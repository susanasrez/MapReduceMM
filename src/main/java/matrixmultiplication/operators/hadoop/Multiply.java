package matrixmultiplication.operators.hadoop;

import java.io.IOException;
import java.util.ArrayList;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.*;
import org.apache.hadoop.mapreduce.lib.output.*;
import org.apache.hadoop.util.ReflectionUtils;

public class Multiply {

    public static class MatrixAMapper extends Mapper<Object,Text,IntWritable, Component> {

        @Override
        public void map(Object key, Text value, Context context)
                throws IOException, InterruptedException {
            String readLine = value.toString();
            String[] stringTokens = readLine.split(",");

            int index = Integer.parseInt(stringTokens[0]);
            double elementValue = Double.parseDouble(stringTokens[2]);

            Component e = new Component(0, index, elementValue);

            IntWritable keyValue = new IntWritable(Integer.parseInt(stringTokens[1]));
            context.write(keyValue, e);
        }
    }

    public static class MatrixBMapper extends Mapper<Object,Text,IntWritable, Component> {

        @Override
        public void map(Object key, Text value, Context context)
                throws IOException, InterruptedException {
            String readLine = value.toString();
            String[] stringTokens = readLine.split(",");

            int index = Integer.parseInt(stringTokens[1]);
            double elementValue = Double.parseDouble(stringTokens[2]);

            Component e = new Component(1,index, elementValue);

            IntWritable keyValue = new IntWritable(Integer.parseInt(stringTokens[0]));
            context.write(keyValue, e);
        }
    }

    public static class ReducerMatrix extends Reducer<IntWritable, Component, PairOfIndexes, DoubleWritable> {

        @Override
        public void reduce(IntWritable key, Iterable<Component> values, Context context)
                throws IOException, InterruptedException {

            ArrayList<Component> M = new ArrayList<Component>();
            ArrayList<Component> N = new ArrayList<Component>();

            Configuration conf = context.getConfiguration();

            for(Component element : values) {

                Component tempElement = ReflectionUtils.newInstance(Component.class, conf);
                ReflectionUtils.copy(conf, element, tempElement);

                if (tempElement.target == 0) {
                    M.add(tempElement);
                } else if(tempElement.target == 1) {
                    N.add(tempElement);
                }
            }

            for(int i=0;i<M.size();i++) {
                for(int j=0;j<N.size();j++) {

                    PairOfIndexes p = new PairOfIndexes(M.get(i).index,N.get(j).index);
                    double multiplyOutput = M.get(i).value * N.get(j).value;

                    context.write(p, new DoubleWritable(multiplyOutput));
                }
            }
        }
    }

    public static class MapperMatrix extends Mapper<Object, Text, PairOfIndexes, DoubleWritable> {
        @Override
        public void map(Object key, Text value, Context context)
                throws IOException, InterruptedException {

            String readLine = value.toString();
            String[] pairValue = readLine.split(" ");

            PairOfIndexes p = new PairOfIndexes(Integer.parseInt(pairValue[0]),Integer.parseInt(pairValue[1]));
            DoubleWritable val = new DoubleWritable(Double.parseDouble(pairValue[2]));

            context.write(p, val);
        }
    }

    public static class ReduceSum extends Reducer<PairOfIndexes, DoubleWritable, PairOfIndexes, DoubleWritable> {
        @Override
        public void reduce(PairOfIndexes key, Iterable<DoubleWritable> values, Context context)
                throws IOException, InterruptedException {

            double sum = 0.0;
            for(DoubleWritable value : values) {
                sum += value.get();
            }

            context.write(key, new DoubleWritable(sum));
        }
    }

    public static void main(String[] args) throws Exception {
        Configuration conf1 = new Configuration();
        Job job1 = Job.getInstance(conf1, "MapIntermediate");

        job1.setJarByClass(Multiply.class);

        MultipleInputs.addInputPath(job1, new Path(args[0]), TextInputFormat.class, MatrixAMapper.class);
        MultipleInputs.addInputPath(job1, new Path(args[1]), TextInputFormat.class, MatrixBMapper.class);

        job1.setReducerClass(ReducerMatrix.class);

        job1.setMapOutputKeyClass(IntWritable.class);
        job1.setMapOutputValueClass(Component.class);

        job1.setOutputKeyClass(PairOfIndexes.class);
        job1.setOutputValueClass(DoubleWritable.class);

        job1.setOutputFormatClass(TextOutputFormat.class);

        FileOutputFormat.setOutputPath(job1, new Path(args[2]));

        if (!job1.waitForCompletion(true)) {
            System.exit(1);
        }

        Configuration conf2 = new Configuration();
        Job job2 = Job.getInstance(conf2, "MapFinalOutput");

        job2.setJarByClass(Multiply.class);

        job2.setMapperClass(MapperMatrix.class);
        job2.setReducerClass(ReduceSum.class);

        job2.setMapOutputKeyClass(PairOfIndexes.class);
        job2.setMapOutputValueClass(DoubleWritable.class);

        job2.setOutputKeyClass(PairOfIndexes.class);
        job2.setOutputValueClass(DoubleWritable.class);

        job2.setInputFormatClass(TextInputFormat.class);
        job2.setOutputFormatClass(TextOutputFormat.class);

        FileInputFormat.setInputPaths(job2, new Path(args[2]));
        FileOutputFormat.setOutputPath(job2, new Path(args[3]));
        job2.waitForCompletion(true);
    }
}