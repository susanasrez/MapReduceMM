package mapreduce.operators.hadoop;
import java.io.IOException;
import java.util.ArrayList;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.util.ReflectionUtils;


public class MatrixMultiplicationHadoop {

    public static class MatriceMapperM extends Mapper<Object,Text,IntWritable,Element> {

        @Override
        public void map(Object key, Text value, Context context)
                throws IOException, InterruptedException {
            String readLine = value.toString();
            String[] stringTokens = readLine.split(",");

            int index = Integer.parseInt(stringTokens[0]);
            int elementValue = Integer.parseInt(stringTokens[2]);

            Element e = new Element(0, index, elementValue);

            IntWritable keyValue = new IntWritable(Integer.parseInt(stringTokens[1]));
            context.write(keyValue, e);
        }
    }

    public static class MatriceMapperN extends Mapper<Object,Text,IntWritable,Element> {

        @Override
        public void map(Object key, Text value, Context context)
                throws IOException, InterruptedException {
            String readLine = value.toString();
            String[] stringTokens = readLine.split(",");

            int index = Integer.parseInt(stringTokens[1]);
            int elementValue = Integer.parseInt(stringTokens[2]);

            Element e = new Element(1,index, elementValue);

            IntWritable keyValue = new IntWritable(Integer.parseInt(stringTokens[0]));
            context.write(keyValue, e);
        }
    }

    public static class ReducerMxN extends Reducer<IntWritable,Element, Pair, DoubleWritable> {

        @Override
        public void reduce(IntWritable key, Iterable<Element> values, Context context)
                throws IOException, InterruptedException {

            ArrayList<Element> M = new ArrayList<Element>();
            ArrayList<Element> N = new ArrayList<Element>();

            Configuration conf = context.getConfiguration();

            for(Element element : values) {

                Element tempElement = ReflectionUtils.newInstance(Element.class, conf);
                ReflectionUtils.copy(conf, element, tempElement);

                if (tempElement.tag == 0) {
                    M.add(tempElement);
                } else if(tempElement.tag == 1) {
                    N.add(tempElement);
                }
            }

            for(int i=0;i<M.size();i++) {
                for(int j=0;j<N.size();j++) {

                    Pair p = new Pair(M.get(i).index,N.get(j).index);
                    double multiplyOutput = M.get(i).value * N.get(j).value;

                    context.write(p, new DoubleWritable(multiplyOutput));
                }
            }
        }
    }

    public static class MapMxN extends Mapper<Object, Text, Pair, DoubleWritable> {
        @Override
        public void map(Object key, Text value, Context context)
                throws IOException, InterruptedException {

            String readLine = value.toString();
            String[] pairValue = readLine.split(" ");

            Pair p = new Pair(Integer.parseInt(pairValue[0]),Integer.parseInt(pairValue[1]));
            DoubleWritable val = new DoubleWritable(Double.parseDouble(pairValue[2]));

            context.write(p, val);
        }
    }

    public static class ReduceMxN extends Reducer<Pair, DoubleWritable, Pair, DoubleWritable> {
        @Override
        public void reduce(Pair key, Iterable<DoubleWritable> values, Context context)
                throws IOException, InterruptedException {

            double sum = 0.0;
            for(DoubleWritable value : values) {
                sum += value.get();
            }

            context.write(key, new DoubleWritable(sum));
        }
    }


}