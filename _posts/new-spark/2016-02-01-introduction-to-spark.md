---
layout: post
published: true
title: 『 Spark 』1. spark 简介
description: things you need know before you touch Spark and before you decide to use spark in your next project.
---


  
## 写在前面

本系列是综合了自己在学习spark过程中的理解记录 ＋ 对参考文章中的一些理解 ＋ 个人实践spark过程中的一些心得而来。写这样一个系列仅仅是为了梳理个人学习spark的笔记记录，并非为了做什么教程，所以一切以个人理解梳理为主，没有必要的细节就不会记录了。若想深入了解，最好阅读参考文章和官方文档。

其次，本系列是基于目前最新的 spark 1.6.0 系列开始的，spark 目前的更新速度很快，记录一下版本好还是必要的。

## 1. 如何向别人介绍 spark

***Apache Spark™ is a fast and general engine for large-scale data processing.***

Apache Spark is a fast and general-purpose cluster computing system.    
It provides high-level APIs in `Java, Scala, Python and R`, and an optimized engine that supports general execution graphs.    
It also supports a rich set of higher-level tools including :    

- Spark SQL for SQL and structured data processing, extends to DataFrames and DataSets    
- MLlib for machine learning    
- GraphX for graph processing    
- Spark Streaming for stream data processing    

## 2. spark 诞生的一些背景

![introduction-to-spark-1.jpg](../images/introduction-to-spark-1.jpg)
![introduction-to-spark-2.jpg](../images/introduction-to-spark-2.jpg)

Spark started in 2009, open sourced 2010, unlike the various specialized systems[hadoop, storm], Spark’s goal was to : 

- generalize MapReduce to support new apps within same engine
    + it's perfectly compatible with hadoop, can run on Hadoop, Mesos, standalone, or in the cloud. It can access diverse data sources including HDFS, Cassandra, HBase, and S3.

- speed up iteration computing over hadoop.
    + use memory + disk instead of disk as data storage medium
    + design a new programming modal, RDD, which make the data processing more graceful [RDD transformation, action, distributed jobs, stages and tasks]

![introduction-to-spark-4.jpg](../images/introduction-to-spark-4.jpg)
![introduction-to-spark-5.jpg](../images/introduction-to-spark-5.jpg)


## 3. 为何选用 spark


- designed, implemented and used as libs, instead of specialized systems;
    + much more useful and maintainable

![introduction-to-spark-3.jpg](../images/introduction-to-spark-3.jpg)

- from history, it is designed and improved upon hadoop and storm, it has perfect genes;
- documents, community, products and trends;
- it provides sql, dataframes, datasets, machine learning lib, graph computing lib and activitily growth 3-party lib, easy to use, cover lots of use cases in lots field;
- it provides ad-hoc exploring, which boost your data exploring and pre-processing and help you build your data ETL, processing job;

## 4. Next

下一篇，通过几个例子来介绍 spark 的基本编程模式。

## 参考文章

- [Intro to Apache Spark](http://stanford.edu/~rezab/sparkclass/slides/itas_workshop.pdf)


## 本系列文章链接

- [『 Spark 』1. spark 简介 ](../introduction-to-spark)
- [『 Spark 』2. spark 基本概念解析 ](../spark-questions-concepts)


