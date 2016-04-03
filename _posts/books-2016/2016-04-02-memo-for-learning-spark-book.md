---
category: books
published: false
layout: post
title: 『 读书笔记 』Learning Spark
description: 好书，应该从不嫌旧
---


## 写在前面

这本书是在 2015.02 就出版的，那个时候 spark 应该还只是 1.1 左右，最近准备看一两本讲 spark 的高质量的书，算是梳理一下自己的思维。期间因为觉得这本书出版得太早，可能会缺少 spark 现在的很多 feature，所以选了另外一本在 gitbook 上开源的书。可是看了这本 learning spark 后，发现两本书还是有很大的差别。虽然必须承认这本书出版得较早，里面缺少了一些 spark 的新 feature，但是这完全不影响你学习 spark，掌握 spark 的里里外外。我比较推荐这本书作为 spark 初学者的入门书，而且这本书还是 spark 的作者 Matei 合著的，在很多问题的解释上会比其他人解释得更浅显易懂。

spark 的知识点很多，也很细碎，初学者需要通读几遍再加上亲身实践，才能把这些细小的知识点串起来，慢慢开始深入了解 spark，inside out。这篇读书笔记是我在读 learning spark 时候记录的书中的一些知识点，供以后 review 用，当然大家也可以参考参考。

书籍简介：

- 第一本介绍 spark 的书
- 由 spark 开发者写
- 完全 free，在 safaribook 上可以直接在线看：[learning spark on safaribook](https://www.safaribooksonline.com/library/view/learning-spark/9781449359034/)
- 本书代码: [code of learning spark on github](https://github.com/databricks/learning-spark)

## 0. Preface

Spark offers three main benefits. 

- First, it is easy to use—you can develop applications on your laptop, using a high-level API that lets you focus on the content of your computation. 
- Second, Spark is fast, ena‐ bling interactive use and complex algorithms. 
- third, Spark is a general engine, letting you combine multiple types of computations (e.g., SQL queries, text process‐ing, and machine learning) that might previously have required different engines. These features make Spark an excellent starting point to learn about Big Data in general.

## 1. Introduction to Data Analysis with Spark

### 1.1 What Is Apache Spark?

![learning-spark-1-1.jpg](../images/learning-spark-1-1.jpg)

- *Spark Core*

Spark Core contains the basic functionality of Spark, including components for task scheduling, memory management, fault recovery, interacting with storage systems.

- *Spark SQL*

Spark SQL is Spark’s package for working with structured data. It allows querying data via SQL as well as the Apache Hive variant of SQL—called the Hive Query Language (HQL)—and it supports many sources of data, including Hive tables, Parquet, and JSON. 

- *Spark Streaming*

Spark Streaming is a Spark component that enables processing of live streams of data. 

- *MLlib*

Spark comes with a library containing common machine learning (ML) functionality, called MLlib. 

- *GraphX*

GraphX is a library for manipulating graphs (e.g., a social network’s friend graph) and performing graph-parallel computations. 


### 1.2 Storage Layers for Spark

Spark can create distributed datasets from any file stored in the Hadoop distributed filesystem (HDFS) or other storage systems supported by the Hadoop APIs (including your local filesystem, Amazon S3, Cassandra, Hive, HBase, etc.). It’s important to remember that Spark does not require Hadoop; it simply has support for storage systems implementing the Hadoop APIs. 


## 2. Downloading Spark and Getting Started

### 2.1 Introduction to Core Spark Concepts

At a high level, every Spark application consists of a driver program that launches various parallel operations on a cluster. The driver program contains your application’s main function and defines distributed datasets on the cluster, then applies operations to them. 

Driver programs access Spark through a SparkContext object, which represents a connection to a computing cluster. 


## 3. Programming with RDDs

In Spark all work is expressed as either creating new RDDs, transforming existing RDDs, or calling operations on RDDs to compute a result.

### 3.1 RDD Basics

An RDD in Spark is simply an immutable distributed collection of objects. Each RDD is split into multiple partitions, which may be computed on different nodes of the cluster.

Users create RDDs in two ways: by loading an external dataset, or by distributing a collection of objects (e.g., a list or set) in their driver program.

To summarize, every Spark program and shell session will work as follows:

- Create some input RDDs from external data.
- Transform them to define new RDDs using transformations like filter().
- Ask Spark to persist() any intermediate RDDs that will need to be reused.
- Launch actions such as count() and first() to kick off a parallel computation, which is then optimized and executed by Spark.


### 3.2 Passing Functions to Spark

In Python, we have three options for passing functions into Spark. 

- lambda expressions

{% highlight python %}

word = rdd.filter(lambda s: "error" in s)

{% endhighlight %}

- top-level functions

{% highlight python %}

import my_personal_lib

word = rdd.filter(my_personal_lib.containsError)

{% endhighlight %}

- locally defined functions

{% highlight python %}

def containsError(s):
    return "error" in s
word = rdd.filter(containsError)

{% endhighlight %}


One issue to watch out for when passing functions is inadvertently serializing the object containing the function. When you pass a function that is the member of an object, or contains references to fields in an object (e.g., self.field), Spark sends the entire object to worker nodes, which can be much larger than the bit of information you need. Sometimes this can also cause your program to fail, if your class contains objects that Python can’t figure out how to pickle.


{% highlight python %}

### wrong way

class SearchFunctions(object):
  def __init__(self, query):
      self.query = query
  def isMatch(self, s):
      return self.query in s
  def getMatchesFunctionReference(self, rdd):
      # Problem: references all of "self" in "self.isMatch"
      return rdd.filter(self.isMatch)
  def getMatchesMemberReference(self, rdd):
      # Problem: references all of "self" in "self.query"
      return rdd.filter(lambda x: self.query in x)

### the right way

class WordFunctions(object):
  ...
  def getMatchesNoReference(self, rdd):
      # Safe: extract only the field we need into a local variable
      query = self.query
      return rdd.filter(lambda x: query in x)

{% endhighlight %}


## 4. Working with Key/Value Pairs

Using controllable partitioning, applications can sometimes greatly reduce communication costs by ensuring that data will be accessed together and will be on the same node. This can provide significant speedups. We illustrate partitioning using the PageRank algorithm as an example. Choosing the right partitioning for a distributed dataset is similar to choosing the right data structure for a local one—in both cases, data layout can greatly affect performance.

### 4.1 Motivation

Spark provides special operations on RDDs containing key/value pairs. These RDDs are called pair RDDs. Pair RDDs are a useful building block in many programs, as they expose operations that allow you to act on each key in parallel or regroup data across the network. 

### 4.2 Data Partitioning (Advanced)

The final Spark feature we will discuss in this chapter is how to control datasets’ partitioning across nodes. In a distributed program, communication is very expensive, so *laying out data to minimize network traffic can greatly improve performance*. Much like how a single-node program needs to choose the right data structure for a collection of records, Spark programs can choose to control their RDDs’ partitioning to reduce communication. Partitioning will not be helpful in all applications.for example, if a given RDD is scanned only once, there is no point in partitioning it in advance. *It is useful only when a dataset is reused multiple times in key-oriented operations such as joins*. We will give some examples shortly.

Spark’s partitioning is available on all RDDs of key/value pairs, and causes the system to group elements based on a function of each key. Although Spark does not give explicit control of which worker node each key goes to (partly because the system is designed to work even if specific nodes fail), it lets the program ensure that a set of keys will appear together on some node. For example, you might choose to hash-partition an RDD into 100 partitions so that keys that have the same hash value modulo 100 appear on the same node. Or you might range-partition the RDD into sorted ranges of keys so that elements with keys in the same range appear on the same node.

As a simple example, consider an application that keeps a large table of user information in memory—say, an RDD of (UserID, UserInfo) pairs, where UserInfo contains a list of topics the user is subscribed to. The application periodically combines this table with a smaller file representing events that happened in the past five minutes—say, a table of (UserID, LinkInfo) pairs for users who have clicked a link on a website in those five minutes. For example, we may wish to count how many users visited a link that was not to one of their subscribed topics. We can perform this combination with Spark’s join() operation, which can be used to group the UserInfo and LinkInfo pairs for each UserID by key. Our application would look like bellow:

{% highlight python %}

// Initialization code; we load the user info from a Hadoop SequenceFile on HDFS.
// This distributes elements of userData by the HDFS block where they are found,
// and doesn't provide Spark with any way of knowing in which partition a
// particular UserID is located.
val sc = new SparkContext(...)
val userData = sc.sequenceFile[UserID, UserInfo]("hdfs://...").persist()

// Function called periodically to process a logfile of events in the past 5 minutes;
// we assume that this is a SequenceFile containing (UserID, LinkInfo) pairs.
def processNewLogs(logFileName: String) {
  val events = sc.sequenceFile[UserID, LinkInfo](logFileName)
  val joined = userData.join(events)// RDD of (UserID, (UserInfo, LinkInfo)) pairs
  val offTopicVisits = joined.filter {
    case (userId, (userInfo, linkInfo)) => // Expand the tuple into its components
      !userInfo.topics.contains(linkInfo.topic)
  }.count()
  println("Number of visits to non-subscribed topics: " + offTopicVisits)
}

{% endhighlight %}

This code will run fine as is, but it will be inefficient. This is because the *join()* operation, called each time *processNewLogs()* is invoked, does not know anything about how the keys are partitioned in the datasets. By default, this operation will hash all the keys of both datasets, sending elements with the same key hash across the network to the same machine, and then join together the elements with the same key on that machine. Because we expect the userData table to be much larger than the small log of events seen every five minutes, this wastes a lot of work: the userData table is hashed and shuffled across the network on every call, even though it doesn’t change.

![learning-spark-1-2.jpg](../images/learning-spark-1-2.jpg)

Fixing this is simple: just use the *partitionBy()* transformation on userData to hash-partition it at the start of the program. We do this by passing a spark.HashPartitioner object to partitionBy, as shown bellow:

{% highlight python  %}

val sc = new SparkContext(...)
val userData = sc.sequenceFile[UserID, UserInfo]("hdfs://...")
                 .partitionBy(new HashPartitioner(100))   // Create 100 partitions
                 .persist()

{% endhighlight  %}

The *processNewLogs()* method can remain unchanged: the events RDD is local to *processNewLogs()*, and is used only once within this method, so there is no advantage in specifying a partitioner for events. Because we called *partitionBy()* when building userData, Spark will now know that it is hash-partitioned, and calls to *join()* on it will take advantage of this information. In particular, when we call *userData.join(events)*, Spark will shuffle only the events RDD, sending events with each particular UserID to the machine that contains the corresponding hash partition of userData. The result is that a lot less data is communicated over the network, and the program runs significantly faster.

![learning-spark-1-3.jpg](../images/learning-spark-1-3.jpg)

Note that *partitionBy()* is a transformation, so it always returns a new RDD—it does not change the original RDD in place. RDDs can never be modified once created. Therefore it is important to persist and save as userData the result of *partitionBy()*, not the original *sequenceFile()*. Also, the 100 passed to *partitionBy()* represents the number of partitions, which will control how many parallel tasks perform further operations on the RDD (e.g., joins); in general, make this at least as large as the number of cores in your cluster.

*WARNING* :

Failure to persist an RDD after it has been transformed with *partitionBy()* will cause subsequent uses of the RDD to repeat the partitioning of the data. Without persistence, use of the partitioned RDD will cause reevaluation of the RDDs complete lineage. That would negate the advantage of *partitionBy()*, resulting in repeated partitioning and shuffling of data across the network, similar to what occurs without any specified partitioner.















## 参考文章

- [learning spark on safaribook](https://www.safaribooksonline.com/library/view/learning-spark/9781449359034/)
- [code of learning spark on github](https://github.com/databricks/learning-spark)
- [spark-summit](https://spark-summit.org/)



