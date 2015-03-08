---
category: books
published: false
layout: post
title: book-3. spark专刊笔记之：spark最佳学习路径
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

- Application：spark的应用程序，包含一个driver program和若干executor；
- SparkContext：spark应用程序的入口，负责调度各个运算资源，协调各个worker node上的executor；
- Driver Program：运行Application的main函数并创建SparkContext；
- Executor：为Application运行在worker node上的一个进程，该进程负责运行task，并且负责将数据存在内存或者磁盘上；每个Application都会申请各自的Executor来处理任务；
- Cluster manager：在集群上获取资源的外部服务；
- Worker node：集群中任何可以运行Application的节点，运行一个或多个Executor进程；
- Task：运行在Executor上的工作单元；
- Job：SparkContext提交的具体Action操作，常和Action对应；
- Stage：每个Job会被拆分为很多组task，每组任务被称为stage，也称taskSet；
- RDD：是Resilient distributed datasets的简称，中文为弹性分布式数据集，是spark的核心模块和类；
- DAGScheduler：根据Job构建基于stage的DAG，并提交stage给taskScheduler；

### 2.2 程序运行流程分析
　　这里详细参考pdf的P14。

### 2.3 spark-submit参数说明
　　这里详细参考pdf的P35。    
　　在spark【版本1.0.0】中支持三种配置方式：代码中的SparkConf，命令行参数或者环境变量配置文件spark-env.sh，以及属性配置文件spark.conf。在生产环境中，参数尽量配置在文件中方便查看和管理，另外spark参数选取的优先级是：SaprkConf > 命令行参数 > 配置文件。   
　　一个spark-submit提交执行的流程分析：详细参考pdf的P40。
