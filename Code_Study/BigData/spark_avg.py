from pyspark import SparkConf,SparkContext


conf = SparkConf()
sc = SparkContext(conf=conf)

age_data = sc.textFile('data/sample_age_data.txt').map(lambda x:x.split(' ')[1])

# reduce()直接将元素的值进行累积操作（如累加），reducebykey()按 k 将 v 进行累积操作（如同 key 累加）
total_age = age_data.map(lambda age:int(age)).reduce(lambda a,b:a+b)

counts = age_data.count()

avg_age = total_age/counts

print(total_age, counts, avg_age)

sc.stop()