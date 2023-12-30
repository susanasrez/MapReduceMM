package mapreduce.operators.hadoop;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.MultipleInputs;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;

public class Initializer {

    public static void setUp(String[] args) throws Exception {

        Job job = Job.getInstance();
        job.setJobName("MapReduceInput");
        job.setJarByClass(Initializer.class);

        MultipleInputs.addInputPath(job, new Path(args[0]), TextInputFormat.class, MatrixMultiplicationHadoop.MatriceMapperM.class);
        MultipleInputs.addInputPath(job, new Path(args[1]), TextInputFormat.class, MatrixMultiplicationHadoop.MatriceMapperN.class);
        job.setReducerClass(MatrixMultiplicationHadoop.ReducerMxN.class);

        job.setMapOutputKeyClass(IntWritable.class);
        job.setMapOutputValueClass(Element.class);

        job.setOutputKeyClass(Pair.class);
        job.setOutputValueClass(DoubleWritable.class);

        job.setOutputFormatClass(TextOutputFormat.class);

        FileOutputFormat.setOutputPath(job, new Path(args[2]));

        job.waitForCompletion(true);

        Job job2 = Job.getInstance();
        job2.setJobName("MapReduceOutput");
        job2.setJarByClass(Initializer.class);

        job2.setMapperClass(MatrixMultiplicationHadoop.MapMxN.class);
        job2.setReducerClass(MatrixMultiplicationHadoop.ReduceMxN.class);

        job2.setMapOutputKeyClass(Pair.class);
        job2.setMapOutputValueClass(DoubleWritable.class);

        job2.setOutputKeyClass(Pair.class);
        job2.setOutputValueClass(DoubleWritable.class);

        job2.setInputFormatClass(TextInputFormat.class);
        job2.setOutputFormatClass(TextOutputFormat.class);

        FileInputFormat.setInputPaths(job2, new Path(args[2]));
        FileOutputFormat.setOutputPath(job2, new Path(args[3]));

        job2.waitForCompletion(true);
    }
}
