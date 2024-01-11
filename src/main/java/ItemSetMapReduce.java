import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import java.io.IOException;
import java.util.*;


public class ItemSetMapReduce extends Configured implements Tool {

    private static final int SET_SIZE = 2;
    private static final int MIN_COUNT = 2;
    public static void main(String[] args) throws Exception {
        int res = ToolRunner.run(new Configuration(), new ItemSetMapReduce(), args);
        System.exit(res);
    }

    @Override
    public int run(String[] args) throws Exception {
        Configuration configuration = new Configuration();
        Job job = Job.getInstance(configuration, "algorithm-frequent-item-set");

        job.setJarByClass(ItemSetMapReduce.class);

        job.setMapperClass(ItemSetMapper.class);
        job.setReducerClass(ItemSetReducer.class);

        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

        TextInputFormat.addInputPath(job, new Path(args[0]));
        TextOutputFormat.setOutputPath(job, new Path(args[1]));

        return job.waitForCompletion(true) ? 0 : 1;
    }

    public static class ItemSetMapper extends Mapper<Object, Text, Text, IntWritable>{

        @Override
        public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
            String[] items = value.toString().split("\\s+");
            Set<String> uniqueItems = new HashSet<>(Arrays.asList(items));
            List<String> sortedItems = new ArrayList<>(uniqueItems);
            Collections.sort(sortedItems);
            combine(sortedItems, new LinkedList<>(), 0, context);
        }

        private void combine(List<String> items, LinkedList<String> combined, int start, Context context) throws IOException, InterruptedException {
            if (combined.size() == SET_SIZE) {
                context.write(new Text(String.join(" - ", combined)), new IntWritable(1));
                return;
            }
            for (int i = start; i < items.size(); ++i) {
                combined.addLast(items.get(i));
                combine(items, combined, i + 1, context);
                combined.removeLast();
            }
        }
    }

    public static class ItemSetReducer extends Reducer<Text, IntWritable, Text, IntWritable> {

        @Override
        public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
            int count = 0;
            for (IntWritable val : values) {
                count += val.get();
            }
            if (count >= MIN_COUNT) {
                context.write(key, new IntWritable(count));
            }
        }
    }
}
