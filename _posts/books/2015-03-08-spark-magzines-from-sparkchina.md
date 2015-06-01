---
category: books
published: false
layout: post
title: spark专刊笔记之：spark最佳学习路径
description: 仅仅是记录我个人的读书记录，看官不必在意～
---


## 
## 1. 前言
　　基于RDD，spark成功地构建起了一体化，多元化的大数据处理体系。在“One stack to rule them all”的思想的引领下，spark成功地使用spark sql，spark streaming，mlib，graphx近乎完美滴解决了大数据中的batch processing，streaming processing，ad-hoc query三大核心问题，而且在spark中，spark sql，spark streaming，mlib和graphx四大子框架【库】之间可以无缝地共享数据和操作，这是当今任何大数据平台都无可匹敌的优势。

## 2. spark最佳学习路径
　　MapReduce作为一个并行计算框架，它提供了一个包含Map和Reduce两阶段的并行处理模型和过程，提供了一个并行化编程模型和接口，可以方便地写出大数据并行处理程序。
　　spark是一个通用的大规模数据快速处理引擎，可以简单地理解为spark就是一个大数据分布式处理框架。也可以理解为spark是基于map reduce算法实现的分布式计算框架，但不同的是spark的中间输出和结果输出可以保持在内存中，从而不再需要读写HDFS，因此spark能更好滴用于数据挖掘与机器学习等需要迭代的map reduce算法中。
　　基于spark内存的计算比hadoop mapreduce快100倍以上【最大的原因是存储介质改为内存】，基于磁盘的计算也要快10倍以上【最大的原因是spark里RDD和DAG的概念】。
　　spark的优势是：快速，易用【多语言继承】，通用【one stack to rule them tall】，继承hadoop，社区活跃。

### 2.1 相关术语

- Application：用户编写的spark应用程序，包含一个driver program和分布在集群中多个节点上运行的executor；
- Driver：使用Driver这一概念的分布式框架很多，比如hive等。spark中的driver即运行上述application的main()函数并创建sparkcontext，创建sparkcontext的目的是为了准备spark应用程序的运行环境。在spark中由sparkcontext负责和clustermanager通信，进行资源的申请，任务的分配和监控等。当executor部分运行完毕后，driver同时负责将sparkcontext关闭，通常用sparkcontext代表driver。
- SparkContext：spark应用程序的入口，负责调度各个运算资源，协调各个worker node上的executor；
- Executor：为Application运行在worker node上的一个进程，该进程负责运行task，并且负责将数据存在内存或者磁盘上；每个Application都会申请各自的Executor来处理任务；
- Cluster manager：在集群上获取资源的外部服务；
- Worker node：集群中任何可以运行Application的节点，运行一个或多个Executor进程。在standalone模式中指的就是通过slave文件配置的worker节点，在spark on yarn模式中指的就是nodemanager节点；
- Task：运行在Executor上的工作单元，多个task组成一个stage，而task的调度及管理等由厦门的taskscheduler负责；
- Job：包含多个task组成的并行计算，往往由spark action触发，一个application可能会产生多个job；
- Stage：每个Job会被拆分为很多组task，每组任务被称为stage，也称taskSet。stage的划分和调度由下面的DAGSeheduler负责，stage有非最终的stage即shuffle map stage和最终的stage即result stage两种。stage的边界就是发生shuffle的地方；
- RDD：是Resilient distributed datasets的简称，中文为弹性分布式数据集，是spark的核心模块和类。它表示已被分区、序列化的、不可变的、有容错机制的并且能够被并行操作的数据集合。其存储级别可以是内存，也可以是磁盘，可通过spark.storage.StorageLevel属性配置；
- 共享变量：在spark application运行时，可能需要共享一些变量，提供task或driver等实用。spark提供了两种共享变量，一种是可以缓存到各个节点的广播变量，一种是只支持加法操作、可以实现求和的累加变量；
- 宽依赖：或称为ShuffleDependency，跟hadoop mapreduce中shuffle的数据依赖相同，款依赖需要计算所有父RDD对应分区的数据，然后在节点之间进行shuffle；
- 窄依赖：或称为NarrowDependency，指某个具体的RDD，其分区partition a最多被父RDD中的一个分区partition b依赖。窄依赖又分为1:1和N:1两种。
- DAGScheduler：根据Job构建基于stage的DAG，并提交stage给taskScheduler；

### 2.2 程序运行流程分析
　　这里详细参考pdf的P14。

### 2.3 spark-submit参数说明
　　这里详细参考pdf的P35。    
　　在spark【版本1.0.0】中支持三种配置方式：代码中的SparkConf，命令行参数或者环境变量配置文件spark-env.sh，以及属性配置文件spark.conf。在生产环境中，参数尽量配置在文件中方便查看和管理，另外spark参数选取的优先级是：SaprkConf > 命令行参数 > 配置文件。   
　　一个spark-submit提交执行的流程分析：详细参考pdf的P40。

## 3. spark生态

### 3.1 spark core
　　spark core包含spark的基本功能，这些功能包括任务调度，内存管理，故障恢复以及存储系统的交互等。其中包含几个重要的概念：RDD, Stage，DAG。spark core的核心思想就是将数据集缓存在内存中，并用linage机制来进行容错。   

### 3.2 RDD
　　RDD具有自动容错，位置感知调度和可伸缩性。RDD只支持粗粒度的转换，也就是记录如何从其他RDD转换而来，以便恢复丢失的分区。其特性如下： 

- 数据存储结构不可变；
- 支持跨集群的分布式数据操作；
- 可对数据集按key进行分区；
- 提供了粗粒度的转换操作；
- 数据存储在内存中，保证了低延迟性；

### 3.3 RDD的依赖关系　  　
- 窄依赖：    
　　一个父RDD分区最多被一个子RDD分区引用，表现为一个父RDD的分区对应于一个子RDD的分区，或多个父RDD的分区对应于一个子RDD的分区。反之，也可以理解成一个父RDD的一个分区不可能对应于一个子RDD的多个分区，如map，filter，union等操作能产生窄依赖。

- 宽依赖：   
　　一个子RDD的分区依赖于父RDD的多个分区或所有分区，也就是说存在一个父RDD的一个分区对应一个子RDD的多个分区。如groupByKey等操作则产生宽依赖操作。

- Stage DAG:    
　　spark提交job后会把job生成多个stage，多个stage之间是有依赖的，stage之间的依赖就构成了DAG。对于窄依赖，spark会尽量多的将RDD放在一个stage中，而对于宽依赖，大多数时候需要shuffle操作。

### 3.4 spark streaming
　　构建在spark上处理stream数据的框架，基本原理是将stream数据分成小的时间片段，以赖斯batch批处理的方式来处理这小部分数据。

### 3.5 spark shark
　　shark即hive on shark，本质是通过hive的hql解析，把hql解析成spark上的RDD操作，然后通过hive的metadata获取数据库里的表信息，shark获取HDFS上的数据和文件并放到spark上运算。shark最大的特性就是快且与hive完全兼容。

### 3.6 spark sql
　　spark sql使用SchemaRDD来操作sql，这个功能和shark雷系，但它比shark支持更多的查询表达式。

### 3.7 Tachyon
　　Tachyon是一个高容错的分布式文件系统，允许文件以内存的速度在集群框架中进行可靠的共享，就像spark和mapreduce那样。

### 3.8 BlinkDB
　　BlinkDB是一个用于在海量数据上运行交互式sql查询的大规模并行查询引擎，他允许用户通过权衡数据精度来提升查询响应时间，其数据的精度被控制在允许的误差范围内。

### 3.9 Akka
　　Akka是一个平台，灵感来自Erlang却用scala语言实现，能更轻松地开发可扩展，实现多线程安全应用。在大多数流行语言中，并发是基于多线程之间的共享内存，使用同步方法防止写争夺来实现的。但Akka提供的并发模型是基于Actors，Actors是一个轻量级的对象，通过发送消息实现交互。每个Actors在同一时间处理最多一个消息，可以发送消息给其他Actors。

## 扫一扫     

![2015-03-08-spark-magzines-from-sparkchina.md](../../images/share/2015-03-08-spark-magzines-from-sparkchina.md.jpg)