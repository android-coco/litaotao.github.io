---
category: spark
published: false
layout: post
title: ［touch spark］5. spark 集群配置
description: first try spark cluster in company
---  


##   
## 1. 写在前面  
　　因为ssh到AWC EC2实在太慢了，而且公司也建立了spark集群，所以以后都在公司内部的spark集群上实践了。不出意外的话，touch spark这个系列以后都会基于公司的spark集群来记录的。安全起见，其中一些敏感信息当然会省略咯，所以如果朋友们有什么不清楚的地方欢迎随时交流啊，交流方式在我的[resume](../resume/)里有写，谢谢大家。  

##   
## 2. 已知步骤  

1. 解压客户端到/usr/local;
2. 配置 /etc/hosts 增加：  

[你的本机IP]    [你的本机IP]
[master_node]    sh-demo-hadoop-01  
[slave_node1]    sh-demo-hadoop-02  
[slave_node2]    sh-demo-hadoop-03  
[slave_node3]    sh-demo-hadoop-04  
[slave_node4]    sh-demo-hadoop-05  
[slave_node5]    sh-demo-hadoop-06  
[slave_node6]    sh-demo-hadoop-07  
[slave_node7]    sh-demo-hadoop-08  
[slave_node8]    sh-demo-hadoop-09  
[slave_node9]    sh-demo-hadoop-10  

其中，你的本机是driver node，master_node是master node，slave_node1-9是worker/executor node。

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



## 扫一扫     

![2014-12-10-first-try-spark-in-company.md](../../images/share/2014-12-10-first-try-spark-in-company.md.jpg)