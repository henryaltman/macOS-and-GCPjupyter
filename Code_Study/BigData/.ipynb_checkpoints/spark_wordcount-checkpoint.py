import  pyspark
from pyspark import SparkConf,SparkContext


conf = SparkConf().setMaster("local[2]").setAppName("spark_wordcount")
sc = SparkContext(conf=conf)

counts = sc.textFile('hello.txt').flatMap(lambda line:line.split(' ')).map(lambda x:(x,1))\
    .reduceByKey(lambda a,b:a+b)
output = counts.collect()


sc.stop()
