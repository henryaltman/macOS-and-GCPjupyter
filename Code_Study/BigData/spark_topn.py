import pyspark
from pyspark import SparkContext,SparkConf
import numpy as np

conf = SparkConf().setMaster("local[4]").setAppName("spark_Top5")
sc = SparkContext(conf=conf)

count = \
     sc.textFile('data/page_views.dat').map(lambda x:x.split('\t')).map(lambda x:(x[5],1))\
    .reduceByKey(lambda a,b:a+b).map(lambda x:(x[1],x[0])).sortByKey(False)\
    .map(lambda x:(x[1],x[0])).take(5)


count_array = np.array(count)

print(count,count_array)

# action（take） 操作过后不再是 RDD 对象因此不能用saveAsTextFile方法
# count.saveAsTextFile("top5_output")

sc.stop()