---
category: books
published: false
layout: post
title: 『 读书笔记 』Learning Spark [part 1]
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

In fact, many other Spark operations automatically result in an RDD with known partitioning information, and many operations other than *join()* will take advantage of this information. For example, *sortByKey()* and *groupByKey()* will result in *range-partitioned and hash-partitioned* RDDs, respectively. On the other hand, operations like *map() cause the new RDD to forget the parent’s partitioning information*, because such operations could theoretically modify the key of each record. The next few sections describe how to determine how an RDD is partitioned, and exactly how partitioning affects the various Spark operations.

If we created an RDD of *(Int, Int)* pairs, which initially have no partitioning information. We then created a second RDD by hash-partitioning the first. If we actually wanted to use partitioned in further operations, then we should have appended *persist()* to the third line of input, in which partitioned is defined. This is for the same reason that we needed *persist()* for userData in the previous example: *without persist(), subsequent RDD actions will evaluate the entire lineage of partitioned, which will cause pairs to be hash-partitioned over and over*.

*Operations That Benefit from Partitioning*:

Many of Spark’s operations involve shuffling data by key across the network. All of these will benefit from partitioning. As of Spark 1.0, the operations that benefit from partitioning are *cogroup(), groupWith(), join(), leftOuterJoin(), rightOuterJoin(), groupByKey(), reduceByKey(), combineByKey(), and lookup()*.

For operations that act on a single RDD, such as *reduceByKey()*, running on a pre-partitioned RDD will cause all the values for each key to be computed locally on a single machine, requiring only the final, locally reduced value to be sent from each worker node back to the master. For binary operations, such as *cogroup() and join()*, pre-partitioning will cause at least one of the RDDs (the one with the known partitioner) to not be shuffled. If both RDDs have the same partitioner, and if they are cached on the same machines (e.g., one was created using mapValues() on the other, which preserves keys and partitioning) or if one of them has not yet been computed, then no shuffling across the network will occur.


## 5. Loading and Saving Your Data

### 5.1 File Formats

![learning-spark-1-4.jpg](../images/learning-spark-1-4.jpg)

#### 5.1.1 Text Files

When we load a single text file as an RDD, each input line becomes an element in the RDD. We can also load multiple whole text files at the same time into a pair RDD by using `wholeTextFiles`, with the key being the name and the value being the contents of each file.

*TIP*: 

Spark supports reading all the files in a given directory and doing wildcard expansion on the input (e.g., part-*.txt). This is useful since large datasets are often spread across multiple files, especially if other files (like success markers) may be in the same directory.


#### 5.1.2 JSON 

JSON is a popular semistructured data format. The simplest way to load JSON data is by loading the data as a text file and then mapping over the values with a JSON parser. Likewise, we can use our preferred JSON serialization library to write out the values to strings, which we can then write out. In Java and Scala we can also work with JSON data using a custom Hadoop format. “JSON” also shows how to load JSON data with Spark SQL.


#### 5.1.3 Comma-Separated Values and Tab-Separated Values

Comma-separated value (CSV) files are supposed to contain a fixed number of fields per line, and the fields are separated by a comma (or a tab in the case of tab-separated value, or TSV, files). Records are often stored one per line, but this is not always the case as records can sometimes span lines. CSV and TSV files can sometimes be inconsistent, most frequently with respect to handling newlines, escaping, and rendering non-ASCII characters, or noninteger numbers. CSVs cannot handle nested field types natively, so we have to unpack and pack to specific fields manually.

Unlike with JSON fields, each record doesn’t have field names associated with it; instead we get back row numbers. It is common practice in single CSV files to make the first row’s column values the names of each field.

Loading CSV/TSV data is similar to loading JSON data in that we can first load it as text and then process it.


#### 5.1.4 SequenceFiles

SequenceFiles are a popular Hadoop format composed of flat files with key/value pairs. SequenceFiles have sync markers that allow Spark to seek to a point in the file and then resynchronize with the record boundaries. This allows Spark to efficiently read SequenceFiles in parallel from multiple nodes. SequenceFiles are a common input/output format for Hadoop MapReduce jobs as well, so if you are working with an existing Hadoop system there is a good chance your data will be available as a SequenceFile.


### 5.2 File Compression

Frequently when working with Big Data, we find ourselves needing to use compressed data to save storage space and network overhead. With most Hadoop output formats, we can specify a compression codec that will compress the data. As we have already seen, Spark’s native input formats (textFile and sequenceFile) can automatically handle some types of compression for us. When you’re reading in compressed data, there are some compression codecs that can be used to automatically guess the compression type.

These compression options apply only to the Hadoop formats that support compression, namely those that are written out to a filesystem. The database Hadoop formats generally do not implement support for compression, or if they have compressed records that is configured in the database itself.

Choosing an output compression codec can have a big impact on future users of the data. With distributed systems such as Spark, we normally try to read our data in from multiple different machines. To make this possible, each worker needs to be able to find the start of a new record. Some compression formats make this impossible, which requires a single node to read in all of the data and thus can easily lead to a bottleneck. Formats that can be easily read from multiple machines are called “splittable.” Table 5-3 lists the available compression options.


![learning-spark-1-5.jpg](../images/learning-spark-1-5.jpg)

*WARNING*:

While Spark’s textFile() method can handle compressed input, it automatically disables splittable even if the input is compressed such that it could be read in a splittable way. If you find yourself needing to read in a large single-file compressed input, consider skipping Spark’s wrapper and instead use either newAPIHadoopFile or hadoopFile and specify the correct compression codec.


### 5.3 File Systems

Spark supports a large number of filesystems for reading and writing to, which we can use with any of the file formats we want.

#### 5.3.1 Local/Regular FS

`While Spark supports loading files from the local filesystem, it requires that the files are available at the same path on all nodes in your cluster.`

Some network filesystems, like NFS, AFS, and MapR’s NFS layer, are exposed to the user as a regular filesystem. If your data is already in one of these systems, then you can use it as an input by just specifying a `file:// path`; Spark will handle it as long as the filesystem is mounted at the same path on each node.

If your file isn’t already on all nodes in the cluster, you can load it locally on the driver without going through Spark and then call parallelize to distribute the contents to workers. This approach can be slow, however, so we recommend putting your files in a shared filesystem like HDFS, NFS, or S3.


#### 5.3.2 Amazon S3

Amazon S3 is an increasingly popular option for storing large amounts of data. S3 is especially fast when your compute nodes are located inside of Amazon EC2, but can easily have much worse performance if you have to go over the public Internet.

To access S3 in Spark, you should first set the `AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY` environment variables to your S3 credentials. You can create these credentials from the Amazon Web Services console. Then pass a path starting with `s3n:// to Spark’s` file input methods, of the form `s3n://bucket/path-within-bucket`. As with all the other filesystems, Spark supports wildcard paths for S3, such as `s3n://bucket/my-files/*.txt`.

If you get an S3 access permissions error from Amazon, make sure that the account for which you specified an access key has both “read” and “list” permissions on the bucket. Spark needs to be able to list the objects in the bucket to identify the ones you want to read.

#### 5.3.3 HDFS

The Hadoop Distributed File System (HDFS) is a popular distributed filesystem with which Spark works well. HDFS is designed to work on commodity hardware and be resilient to node failure while providing high data throughput. Spark and HDFS can be collocated on the same machines, and Spark can take advantage of this data locality to avoid network overhead.

Using Spark with HDFS is as simple as specifying `hdfs://master:port/path` for your input and output.

*WARNING*:

The HDFS protocol changes across Hadoop versions, so if you run a version of Spark that is compiled for a different version it will fail. By default Spark is built against Hadoop 1.0.4. If you build from source, you can specify SPARK_HADOOP_VERSION= as a environment variable to build against a different version; or you can download a different precompiled version of Spark. You can determine the value by running hadoop version.


### 5.4 Structured Data with Spark SQL

Spark SQL is a component added in Spark 1.0 that is quickly becoming Spark’s preferred way to work with structured and semistructured data. By structured data, we mean data that has a schema, that is, a consistent set of fields across data records. Spark SQL supports multiple structured data sources as input, and because it understands their schema, it can efficiently read only the fields you require from these data sources. 


### 5.5 Databases

Spark can access several popular databases using either their Hadoop connectors or custom Spark connectors. 


## 6. Advanced Spark Programming

### 6.1 Accumulators

When we normally pass functions to Spark, such as a *map()* function or a condition for *filter()*, they can use variables defined outside them in the driver program, but each task running on the cluster gets a new copy of each variable, and updates from these copies are not propagated back to the driver. Spark’s shared variables, accumulators and broadcast variables, relax this restriction for two common types of communication patterns: aggregation of results and broadcasts.

Our first type of shared variable, accumulators, provides a simple syntax for aggregating values from worker nodes back to the driver program. One of the most common uses of accumulators is to count events that occur during job execution for debugging purposes. 

{% highlight python %}

# Accumulator empty line count in Python

file = sc.textFile(inputFile)
# Create Accumulator[Int] initialized to 0
blankLines = sc.accumulator(0)

def extractCallSigns(line):
    global blankLines   # Make the global variable accessible
    if (line == ""):
        blankLines += 1
    return line.split(" ")

callSigns = file.flatMap(extractCallSigns)
callSigns.saveAsTextFile(outputDir + "/callsigns")
print "Blank lines: %d" % blankLines.value

{% endhighlight %}

To summarize, accumulators work as follows:

- We create them in the driver by calling the *SparkContext.accumulator(initialValue)* method, which produces an accumulator holding an initial value. The return type is an *org.apache.spark.Accumulator[T]* object, where *T* is the type of initialValue.
- Worker code in Spark closures can add to the accumulator with its *+=* method (or add in Java).
- The driver program can call the *value* property on the accumulator to access its value (or call *value() and setValue()* in Java).

Note that tasks on worker nodes cannot access the accumulator’s *value()*, from the point of view of these tasks, accumulators are write-only variables. This allows accumulators to be implemented efficiently, without having to communicate every update.

#### 6.1.1 Accumulators and Fault Tolerance

Spark automatically deals with failed or slow machines by re-executing failed or slow tasks. For example, if the node running a partition of a *map()* operation crashes, Spark will rerun it on another node; and even if the node does not crash but is simply much slower than other nodes, Spark can preemptively launch a “speculative” copy of the task on another node, and take its result if that finishes. Even if no nodes fail, Spark may have to rerun a task to rebuild a cached value that falls out of memory. The net result is therefore that the same function may run multiple times on the same data depending on what happens on the cluster.

How does this interact with accumulators? The end result is that for accumulators used in actions, Spark applies each task’s update to each accumulator only once. Thus, if we want a reliable absolute value counter, regardless of failures or multiple evaluations, we must put it inside an action like *foreach()*.

For accumulators used in RDD transformations instead of actions, this guarantee does not exist. An accumulator update within a transformation can occur more than once. One such case of a probably unintended multiple update occurs when a cached but infrequently used RDD is first evicted from the LRU cache and is then subsequently needed. This forces the RDD to be recalculated from its lineage, with the unintended side effect that calls to update an accumulator within the transformations in that lineage are sent again to the driver. Within transformations, accumulators should, consequently, be used only for debugging purposes.

While future versions of Spark may change this behavior to count the update only once, the current version (1.2.0) does have the multiple update behavior, so accumulators in transformations are recommended only for debugging purposes.


#### 6.1.2 Custom Accumulators

So far we’ve seen how to use one of Spark’s built-in accumulator types: integers (Accumulator[Int]) with addition. Out of the box, Spark supports accumulators of type Double, Long, and Float. In addition to these, Spark also includes an API to define custom accumulator types and custom aggregation operations (e.g., finding the maximum of the accumulated values instead of adding them). Custom accumulators need to extend AccumulatorParam, which is covered in the Spark API documentation. Beyond adding to a numeric value, we can use any operation for add, provided that operation is commutative and associative. For example, instead of adding to track the total we could keep track of the maximum value seen so far.


### 6.2 Broadcast Variables

Spark’s second type of shared variable, broadcast variables, allows the program to efficiently send a large, read-only value to all the worker nodes for use in one or more Spark operations. They come in handy, for example, if your application needs to send a large, read-only lookup table to all the nodes, or even a large feature vector in a machine learning algorithm.

Recall that Spark automatically sends all variables referenced in your closures to the worker nodes. While this is convenient, it can also be inefficient because :

- the default task launching mechanism is optimized for small task sizes
- you might, in fact, use the same variable in multiple parallel operations, but Spark will send it separately for each operation. 

A broadcast variable is simply an object of type *spark.broadcast.Broadcast[T]*, which wraps a value of type T. We can access this value by calling *value* on the Broadcast object in our tasks. The value is sent to each node only once, using an efficient, BitTorrent-like communication mechanism.

*Optimizing Broadcasts*:

When we are broadcasting large values, it is important to choose a data serialization format that is both fast and compact, because the time to send the value over the network can quickly become a bottleneck if it takes a long time to either serialize a value or to send the serialized value over the network. 

the process of using broadcast variables is simple:

- Create a *Broadcast[T]* by calling SparkContext.broadcast on an object of type T. Any type works as long as it is also Serializable.
- Access its value with the *value* property (or *value()* method in Java).
- The variable will be sent to each node only once, and should be treated as read-only (updates will not be propagated to other nodes).

### 6.3 Working on a Per-Partition Basis

Working with data on a per-partition basis allows us to avoid redoing setup work for each data item. Operations like opening a database connection or creating a random-number generator are examples of setup steps that we wish to avoid doing for each element. Spark has per-partition versions of map and foreach to help reduce the cost of these operations by letting you run code only once for each partition of an RDD.

When operating on a per-partition basis, Spark gives our function an Iterator of the elements in that partition. To return values, we return an Iterable. In addition to mapPartitions(), Spark has a number of other per-partition operators. Bellow is an example of a partition-based operation `mapPartitions`:

{% highlight python %}

```
mapPartitions(f, preservesPartitioning=False)
Return a new RDD by applying a function to each partition of this RDD.
```

>>> rdd = sc.parallelize([1, 2, 3, 4], 2)
>>> def f(iterator): yield sum(iterator)
>>> rdd.mapPartitions(f).collect()
[3, 7]

{% endhighlight %}

### 6.4 Piping to External Programs

Spark provides a *pipe()* method on RDDs. Spark’s *pipe()* lets us write parts of jobs using any language we want as long as it can read and write to Unix standard streams. With *pipe()*, you can write a transformation of an RDD that reads each RDD element from standard input as a String, manipulates that String however you like, and then writes the result(s) as Strings to standard output. The interface and programming model is restrictive and limited, but sometimes it’s just what you need to do something like make use of a native code function within a map or filter operation.

### 6.5 Numeric RDD Operations

## 7. Running on a Cluster

### 7.1 Spark Runtime Architecture

In distributed mode, Spark uses a master/slave architecture with one central coordinator and many distributed workers. The central coordinator is called the driver. The driver communicates with a potentially large number of distributed workers called executors. The driver runs in its own Java process and each executor is a separate Java process. A driver and its executors are together termed a Spark application.

A Spark application is launched on a set of machines using an external service called a cluster manager. As noted, Spark is packaged with a built-in cluster manager called the Standalone cluster manager. Spark also works with Hadoop YARN and Apache Mesos, two popular open source cluster managers.

![learning-spark-1-6.jpg](../images/learning-spark-1-6.jpg)

#### 7.1.1 The Driver

The driver is the process where the main() method of your program runs. It is the process running the user code that creates a SparkContext, creates RDDs, and performs transformations and actions.

*When the driver runs, it performs two duties*:

- Converting a user program into tasks

The Spark driver is responsible for converting a user program into units of physical execution called tasks. At a high level, all Spark programs follow the same structure: they create RDDs from some input, derive new RDDs from those using transformations, and perform actions to collect or save data. A Spark program implicitly creates a logical directed acyclic graph (DAG) of operations. When the driver runs, it converts this logical graph into a physical execution plan.

Spark performs several optimizations, such as `pipelining` map transformations together to merge them, and converts the execution graph into a set of stages. Each stage, in turn, consists of multiple tasks. The tasks are bundled up and prepared to be sent to the cluster. Tasks are the smallest unit of work in Spark; a typical user program can launch hundreds or thousands of individual tasks.

- Scheduling tasks on executors

Given a physical execution plan, a Spark driver must coordinate the scheduling of individual tasks on executors. When executors are started they register themselves with the driver, so it has a complete view of the application’s executors at all times. Each executor represents a process capable of running tasks and storing RDD data.

The Spark driver will look at the current set of executors and try to schedule each task in an appropriate location, based on data placement. When tasks execute, they may have a side effect of storing cached data. The driver also tracks the location of cached data and uses it to schedule future tasks that access that data.

The driver exposes information about the running Spark application through a web interface, which by default is available at port 4040. 

#### 7.1.2 Executors

Spark executors are worker processes responsible for running the individual tasks in a given Spark job. Executors are launched once at the beginning of a Spark application and typically run for the entire lifetime of an application, though Spark applications can continue if executors fail. Executors have two roles: 

- First, they run the tasks that make up the application and return results to the driver. 
- Second, they provide in-memory storage for RDDs that are cached by user programs, through a service called the Block Manager that lives within each executor. Because RDDs are cached directly inside of executors, tasks can run alongside the cached data.

If you’ve run examples in Spark’s local mode. In this mode, the Spark driver runs along with an executor in the same Java process. This is a special case; executors typically each run in a dedicated process.

#### 7.1.3 Cluster Manager

So far we’ve discussed drivers and executors in somewhat abstract terms. But how do drivers and executor processes initially get launched? Spark depends on a cluster manager to launch executors and, in certain cases, to launch the driver. The cluster manager is a pluggable component in Spark. This allows Spark to run on top of different external managers, such as YARN and Mesos, as well as its built-in Standalone cluster manager.

#### 7.1.4 Summary

To summarize the concepts in this section, let’s walk through the exact steps that occur when you run a Spark application on a cluster:

- The user submits an application using *spark-submit*.
- *spark-submit* launches the driver program and invokes the *main()* method specified by the user.
- The driver program contacts the cluster manager to ask for resources to launch executors.
- The cluster manager launches executors on behalf of the driver program.
- The driver process runs through the user application. Based on the RDD actions and transformations in the program, the driver sends work to executors in the form of tasks.
- Tasks are run on executor processes to compute and save results.
- If the driver’s *main()* method exits or it calls *SparkContext.stop()*, it will terminate the executors and release resources from the cluster manager.


### 7.2 Deploying Applications with spark-submit

### 7.3 Packaging Your Code and Dependencies

### 7.3 Scheduling Within and Between Spark Applications

The example we just walked through involves a single user submitting a job to a cluster. In reality, many clusters are shared between multiple users. Shared environments have the challenge of scheduling: what happens if two users both launch Spark applications that each want to use the entire cluster’s worth of resources? Scheduling policies help ensure that resources are not overwhelmed and allow for prioritization of workloads.

For scheduling in multitenant clusters, Spark primarily relies on the cluster manager to share resources between Spark applications. When a Spark application asks for executors from the cluster manager, it may receive more or fewer executors depending on availability and contention in the cluster. Many cluster managers offer the ability to define queues with different priorities or capacity limits, and Spark will then submit jobs to such queues. See the documentation of your specific cluster manager for more details.

One special case of Spark applications are those that are long lived, meaning that they are never intended to terminate. An example of a long-lived Spark application is the JDBC server bundled with Spark SQL. When the JDBC server launches it acquires a set of executors from the cluster manager, then acts as a permanent gateway for SQL queries submitted by users. Since this single application is scheduling work for multiple users, it needs a finer-grained mechanism to enforce sharing policies. Spark provides such a mechanism through configurable intra-application scheduling policies. Spark’s internal Fair Scheduler lets long-lived applications define queues for prioritizing scheduling of tasks. A detailed review of these is beyond the scope of this book; the official documentation on the Fair Scheduler provides a good reference.

### 7.4 HIGH AVAILABILITY

When running in production settings, you will want your Standalone cluster to be available to accept applications even if individual nodes in your cluster go down. Out of the box, the Standalone mode will gracefully support the failure of worker nodes. If you also want the master of the cluster to be highly available, Spark supports using Apache ZooKeeper (a distributed coordination system) to keep multiple standby masters and switch to a new one when any of them fails. Configuring a Standalone cluster with ZooKeeper is outside the scope of the book, but is described in the [official Spark documentation](https://spark.apache.org/docs/latest/spark-standalone.html#high-availability).



## 参考文章

- [learning spark on safaribook](https://www.safaribooksonline.com/library/view/learning-spark/9781449359034/)
- [code of learning spark on github](https://github.com/databricks/learning-spark)
- [spark-summit](https://spark-summit.org/)



