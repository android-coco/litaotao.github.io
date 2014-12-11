---
category: spark
published: false
layout: post
title: ［touch spark］5. spark 集群配置
description: first try spark cluster in company
---  


##   
## 1. 已知步骤  

1. 解压客户端到 /usr/local  ，客户端在 \\filesvr.datayes.com\Sharefolder\to xiao\client\spark-dev.tar.gz
2. 配置 /etc/hosts 增加：  

[你的本机IP]    [你的本机IP]
10.21.208.21    sh-demo-hadoop-01  
10.21.208.22    sh-demo-hadoop-02  
10.21.208.23    sh-demo-hadoop-03  
10.21.208.24    sh-demo-hadoop-04  
10.21.208.25    sh-demo-hadoop-05  
10.21.208.26    sh-demo-hadoop-06  
10.21.208.27    sh-demo-hadoop-07  
10.21.208.28    sh-demo-hadoop-08  
10.21.208.29    sh-demo-hadoop-09  
10.21.208.30    sh-demo-hadoop-10  

其中，你的本机是driver node，10.21.208.21是master node，10.21.208.22-30是worker/executor node。

3. 测试 (所有命令都在 /usr/local/spark 下运行)  

```
a)  Spark-submit  (python + mllib)
    ./bin/spark-submit --master spark://10.21.208.21:7077  examples/src/main/python/mllib/kmeans.py hdfs://10.21.208.21:8020/tmp/kmeans_data.txt 2

b)  Spark-shell
    ./bin/spark-shell --master spark://10.21.208.21:7077
	val file=sc.textFile("hdfs://10.21.208.21:8020/tmp/kmeans_data.txt")
	val count=file.flatMap(line => line.split(" ")).map(word => (word,1)).reduceByKey(_+_)
	count.collect() 

c)  Pyspark
    ./bin/pyspark --master spark://10.21.208.21:7077
 	file = sc.textFile("hdfs://10.21.208.21:8020/tmp/kmeans_data.txt")
	counts = file.flatMap(lambda line: line.split(" ")) \
             	 .map(lambda word: (word, 1)) \
             	 .reduceByKey(lambda a, b: a + b)
	counts.collect()
```  


