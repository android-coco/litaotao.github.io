---
layout: post
published: false
title: 『 Spark 』7. 使用 Spark DataFrame 进行大数据分析
description: know more, do better 
---  



## 写在前面

本系列是综合了自己在学习spark过程中的理解记录 ＋ 对参考文章中的一些理解 ＋ 个人实践spark过程中的一些心得而来。写这样一个系列仅仅是为了梳理个人学习spark的笔记记录，并非为了做什么教程，所以一切以个人理解梳理为主，没有必要的细节就不会记录了。若想深入了解，最好阅读参考文章和官方文档。

其次，本系列是基于目前最新的 spark 1.6.0 系列开始的，spark 目前的更新速度很快，记录一下版本好还是必要的。

Tips: 如果插图看起来不明显，可以：1. 放大网页；2. 新标签中打开图片，查看原图哦。


## 1. 什么是 spark dataframe

先来看看官方原汁原味的文档是怎么介绍的：

A DataFrame is `a distributed collection of data` organized into named columns. It is conceptually equivalent to a `table in a relational database` or a data frame in R/Python, but with `richer optimizations` under the hood. DataFrames can be constructed from a wide array of sources such as: `structured data files, tables in Hive, external databases, or existing RDDs`.

我们可以看到 spark dataframe 的几个关键点：

- 分布式的数据集
- 类似关系型数据库中的table，或者 excel 里的一张 sheet，或者 python/R 里的 dataframe
- 拥有丰富的操作函数，类似于 rdd 中的算子
- 一个 dataframe 可以被注册成一张数据表，然后用 sql 语言在上面操作
- 丰富的创建方式
    + 已有的RDD
    + 结构化数据文件
    + JSON数据集
    + Hive表
    + 外部数据库

## 2. 为什么要用 spark dataframe

DataFrame API 是在 R 和 Python data frame 的设计灵感之上设计的，具有以下功能特性：

- 从KB到PB级的数据量支持；
- 多种数据格式和多种存储系统支持；
- 通过Spark SQL 的 Catalyst优化器进行先进的优化，生成代码；
- 通过Spark无缝集成所有大数据工具与基础设施；
- 为Python、Java、Scala和R语言（SparkR）API；

简单来说，dataframe 能够更方便的操作数据集，而且因为其底层是通过 spark sql 的 Catalyst优化器生成优化后的执行代码，所以其执行速度会更快。总结下来就是，使用 spark dataframe 来构建 spark app，能：

- *write less : 写更少的代码* 
- *do more : 做更多的事情*
- *faster : 以更快的速度*

### 2.1 write less : 写更少的代码

### 2.2 do more : 做更多的事情

### 2.3 faster : 以更快的速度


## 3. 创建 dataframe

因为 spark sql，dataframe，datasets 都是共用 spark sql 这个库的，三者共享同样的代码优化，生成以及执行流程，所以 sql，dataframe，datasets 的入口都是 sqlContext.

- step 1 : 创建 sqlContext

下面是我自己创建 spark sc 都模版：

{% highlight python %}

sc_conf = SparkConf()
sc_conf.setAppName("03-DataFrame-01")
sc_conf.setMaster(SPARK_MASTER)
sc_conf.set('spark.executor.memory', '2g')
sc_conf.set('spark.logConf', True)
sc_conf.getAll()

try:
    sc.stop()
    time.sleep(1)
except:
    sc = SparkContext(conf=sc_conf)
    sqlContext = SQLContext(sc)

{% endhighlight %}

- step 2 : 创建 dataframe，从已有的 RDD


## 4. 操作 dataframe






## 5. 一些经验




## 2. Next

既然我们都慢慢开始深入理解 spark 的执行原理了，那下次我们就来说说 spark 的一些配置吧，然后再说说 spark 应用的优化。


## 参考文章

- [Spark SQL, DataFrames and Datasets Guide](http://spark.apache.org/docs/latest/sql-programming-guide.html#dataframes)
- [Introducing DataFrames in Spark for Large Scale Data Science](https://databricks.com/blog/2015/02/17/introducing-dataframes-in-spark-for-large-scale-data-science.html)


## 本系列文章链接

- [『 Spark 』1. spark 简介 ](../introduction-to-spark)
- [『 Spark 』2. spark 基本概念解析 ](../spark-questions-concepts)
- [『 Spark 』3. spark 编程模式 ](../spark-programming-model)
- [『 Spark 』4. spark 之 RDD ](../spark-what-is-rdd)
- [『 Spark 』5. 这些年，你不能错过的 spark 学习资源 ](../spark-resouces-blogs-paper)
- [『 Spark 』6. 深入研究 spark 运行原理之 job, stage, task](deep-into-spark-exection-model)



