import numpy
import  pyspark
from pyspark import SparkConf,SparkContext


conf = SparkConf().setMaster("local[2]").setAppName("spark_wordcount")
sc = SparkContext(conf=conf)

# textFile方法可以读文件和文件夹
counts = sc.textFile('hellocount').flatMap(lambda line:line.split(' ')).map(lambda x:(x,1))\
    .reduceByKey(lambda a,b:a+b)  # a、b 分别为两个 kv（k 相同 v 相加）
output = counts.collect()


output_array = numpy.array(output)

print(output_array.shape)


print(output,output_array)



def saveFile():
    '''
    为了防止数据覆盖，输出的路径不能存在同名的文件、文件夹
    :return:
    '''
    counts.saveAsTextFile("hellocount_output")


saveFile()

sc.stop()

