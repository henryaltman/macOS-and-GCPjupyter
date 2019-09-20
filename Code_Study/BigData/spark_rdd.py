import pyspark
from pyspark import SparkConf, SparkContext




data_str = ["hello spark", "hello lover", "hello world"]
data_num = [1,2,3,4,5]




if __name__ == '__main__':
    conf = SparkConf().setMaster("local[2]").setAppName("spark0401")
    sc = SparkContext(conf=conf)


    def my_map():
        rdd1 = sc.parallelize(data_num)
        rdd2 = rdd1.map(lambda x:x+1)
        print(rdd2.collect())
        # [2, 3, 4, 5, 6]

    def my_map2():
        rdd1 = sc.parallelize(data_str)
        rdd2 = rdd1.map(lambda x:(x,1))
        print(rdd2.collect())
        # [('hello spark', 1), ('hello lover', 1), ('hello world', 1)]


    def my_filter():
        rdd1 = sc.parallelize(data_num)
        rdd2 = rdd1.filter(lambda x: x > 3)
        print(rdd2.collect())
        # [4, 5]


    def my_flatMap():  # 与 map 函数的区别是 map 总是返回相同元素的数据集、flatMap 则不一定（都同时对每个元素操作）
        rdd1 = sc.parallelize(data_str)
        rdd2 = rdd1.flatMap(lambda line: line.split(" "))
        print(rdd2.collect())
        # ['hello', 'spark', 'hello', 'lover', 'hello', 'world']


    def my_groupBy():
        rdd1 = sc.parallelize(data_str)
        rdd2 = rdd1.flatMap(lambda x: x.split(" ")).map(lambda x: (x, 1))
        rdd3 = rdd2.groupByKey()
        print(rdd3.collect())
        # [('world', <pyspark.resultiterable.ResultIterable object at 0x1133efeb8>), ('hello', <pyspark.resultiterable.ResultIterable object at 0x113407438>), ('spark', <pyspark.resultiterable.ResultIterable object at 0x113407b70>), ('lover', <pyspark.resultiterable.ResultIterable object at 0x113407780>)]
        print(rdd3.map(lambda x: {x[0]: list(x[1])}).collect())
        # [{'world': [1]}, {'hello': [1, 1, 1]}, {'spark': [1]}, {'lover': [1]}]


    def my_reduceByKey():  # 对元素为kv对的RDD中Key相同的元素的value进行reduce（同 k 合并成新 kv）
        rdd1 = sc.parallelize(data_str)
        rdd2 = rdd1.flatMap(lambda x: x.split(" ")).map(lambda x: (x, 1))
        rdd3 = rdd2.reduceByKey(lambda a, b: a + b)
        print(rdd3.collect())
        # [('world', 1), ('hello', 3), ('spark', 1), ('lover', 1)]


    def my_sort():
        rdd1 = sc.parallelize(data_str)
        rdd2 = rdd1.flatMap(lambda x: x.split(" ")).map(lambda x: (x, 1))
        rdd3 = rdd2.reduceByKey(lambda a, b: a + b)
        # rdd4 = rdd3.sortByKey().collect()
        # [('world', 1), ('hello', 3), ('spark', 1), ('lover', 1)]
        rdd4 = rdd3.map(lambda x:(x[1], x[0])).sortByKey()
        print(rdd4.collect())
        # [(1, 'world'), (1, 'spark'), (1, 'lover'), (3, 'hello')]
        rdd4 = rdd3.map(lambda x: (x[1], x[0])).sortByKey().map(lambda x: (x[1], x[0]))
        print(rdd4.collect())
        # [('world', 1), ('spark', 1), ('lover', 1), ('hello', 3)]


    def my_union():
        a = sc.parallelize([1,2,3])
        b = sc.parallelize([3,4,5])
        print(a.union(b).collect())
        # [1, 2, 3, 3, 4, 5]


    def my_distinct():
        a = sc.parallelize([1, 2, 3])
        b = sc.parallelize([2, 3, 4])
        print(a.union(b).distinct().collect())
        # [4, 1, 2, 3]

    def my_join():
        a = sc.parallelize([('A','a1'),('C','c1'),('D','d1'),('F','f1'),('F','f2')])
        b = sc.parallelize([('A','a2'),('C','c2'),('C','c3'),('E','e1')])
        print(a.join(b).collect())
        # 内连接，以共有的元素为准，作一次二元组合
        # [('A', ('a1', 'a2')), ('C', ('c1', 'c2')), ('C', ('c1', 'c3'))]
        print(a.leftOuterJoin(b).collect())
        # 左连接，以左边的表为准，作一次二元组合，若右边的表没有则补上 None
        # [('A', ('a1', 'a2')), ('F', ('f1', None)), ('F', ('f2', None)), ('C', ('c1', 'c2')), ('C', ('c1', 'c3')), ('D', ('d1', None))]
        print(a.rightOuterJoin(b).collect())
        # 右连接，以右边的表为准，作一次二元组合，若左边的表没有则补上 None左
        # [('A', ('a1', 'a2')), ('C', ('c1', 'c2')), ('C', ('c1', 'c3')), ('E', (None, 'e1'))]
        print(a.fullOuterJoin(b).collect())
        # 全连接，用两边全部元素，作二元组合，任一边没有的则补上 None
        # [('A', ('a1', 'a2')), ('F', ('f1', None)), ('F', ('f2', None)), ('C', ('c1', 'c2')), ('C', ('c1', 'c3')), ('D', ('d1', None)), ('E', (None, 'e1'))]


    def my_action():
        rdd = sc.parallelize(data_num)
        rdd.count()
        rdd.take(3)
        rdd.max()
        rdd.min()
        rdd.sum()
        print()
        print(rdd.reduce(lambda x,y:x+y))
        # 15
        print(rdd.foreach(lambda x:print(x)))
        # 1
        # 2
        # 3
        # 4
        # 5
        # None



    my_map()
    my_map2()
    my_filter()
    my_flatMap()
    my_groupBy()
    my_reduceByKey()
    my_sort()
    print('==================================='*2)
    my_union()
    my_distinct()
    my_join()
    my_action()

    sc.stop()