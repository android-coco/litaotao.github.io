---
category: books
published: false
layout: post
title: book-4. Learning Spark 阅读笔记
description: 仅仅是记录我个人的读书记录，看官不必在意～
---

## 
## 0. 写在前面
代码示例在 [databricks/github](https://github.com/databricks/learning-spark)

## 1. Chapter 1. Introduction to Data Analysis with Spark

### What is Apache Spark

- Designed to be fast and general-purpose.
- Extends MP model, more computations, interactive query, streaming.
- Run computations in memory, also do well in data on disk.
- Easy to use, Python, Java, Scala and SQL, can access HDFS and Cassandra and so on.

### A Unified Stack

- Spark contains mutiple closely integrated components.
- Tight integration's benefits.
    + All components in the stack benefit from improvments at the lower layers.
    + The cost associated with running the stack are minimized.
    + Build app that seamlessly combine different models.
- Spark stack grpah:

![spark-stack.jpg](../images/spark-stack.jpg)

### Spark Core

- The basic functionality of spark:
    + Task scheduling
    + Memory management
    + Fault recovery
    + Interacting with storage system
    + RDD definition

## 2. Chapter 2. Downloading Spark and Getting Started

- Spark itself is written in scala, and runs on the Java Virtual Machine. Need Java 6 or newer, if write Python, need Python 2.6 or 2.7, does not yet support Python 3.

### Using IPython

- IPYTHON: set this environment variable to 1 will use the IPython shell to access Spark when ./bin/pyspark
- IPYTHON_OPTS: set this environment variable to "notebook" will use the IPython notebook to access Spark when ./bin/pyspark

### Introduction to Core Spark Concepts

- Driver program: Contains the app's main function and defines distributed datasets on the cluster, then applies operations to them. In shells, the driver program is the Spark shell itself.
- Driver program access Spark through a SparkContext object, which represents a connection to a computing cluster.

## 3. Chatper 3. Programming with RDDs

- An RDD is simple a distributed collection of elements, in Spark all work is expressed as either creating new RDDs, transforming RDDs or calling operations on RDDs to compute a result.
- Two ways to create RDDs: 
    + Loading an external dataset;  
    + Parallelizing a collection in your driver program, not that widely used since it required that you have your entire dataset in memeory on one machine;
- RDD.filter() does not mutate the existing inputRDD, it just retures a pointer to an entirely new RDD, inputRDD can still be reused later in the program. For example, the execute graph of printing the error and warn message in a logfile is as bellow:

```
errorsRDD = inputRDD.filter(lambda x: "error" in x)
warningRDD = inputRDD.filter(lambda x: "warn" in x)
badLinesRDD = errorsRDD.union(warningRDD)
```

![learning-spark-1.jpg](../../images/learning-spark-1.jpg)

- Actions: The operations that return a final value to the driver program or write data to an external storage system. Should note that each time we call a new action, the entire RDD must be computed "from scratch", to avoid this inefficiency, users can persist intermediate results.
- Lazy evaluation: Spark will not begin to execute until it sees an action. 

### Persistence(Cache)

- If wish to use the same RDD mutiple times, Spark will recompute the RDD and all of its dependencies each time we call an action on the RDD, it's expensive for iterative algorithm, so that we need persist or cache data.
- The for cache level, defined in pyspark.StorageLevel or org.apache.spark.storage.StorageLevel:

![learning-spark-2.jpg](../../images/learning-spark-2.jpg)

- The default persist() will store the data in the JVM heap as unserialized objects, in Python, we always serialize the data persist stores, so the default is instead stored in the JVM heap as pickled objects, when write data out to disk or off-heap storage, the data is also always serialized. Off-heap caching is experimental and uses Tachyon.

- The ability to always recompute an RDD is actually why RDDs are called "resilient", when a machine holding RDD data losts, it can be recomputed the missing data.

## 4. Chapter 4. Working with Key/Value Pairs

- Key/Value RDDs are commonly used to perform aggregations, and often we'll do some initial ETL(extract, transform, load) to get our data into a key/value format.
- The advanced feature that lets users control the layout of pair RDDs across nodes is partitioning. Using controllable partitioning, applications can sometimes greatly reduce communications costs by ensuring that data will be accessed together and will be on the same node. 

### Data Partitioning(Advanced)

- Partitioning is important but not necessary for all applications, for if a given RDD is scanned only once, there is not point in partitioning it in advance. It's very useful when a dataset is reused multiple times in key-oriented operations such as joins. 
- There is a good example in the book, bellow is the comparison: 
    + Before

![learning-spark-3.jpg](../images/learning-spark-3.jpg)
![learning-spark-4.jpg](../images/learning-spark-4.jpg)

+ After

![learning-spark-5.jpg](../images/learning-spark-5.jpg)
![learning-spark-6.jpg](../images/learning-spark-6.jpg)

- partitionBy() is a transformation, RDDs can never be modified once created. Therefore need to persist and save as userData the result of partitionBy(), not the original sequenceFile(). Also, the 100 passed to partitionBy represents the number of partitions, which will control how many parallel tasks perform further operations on the RDD, in general, make this at least as large as the number of cores in your cluster.
- There is a PageRand example in this chapter.

## 5. Chapter 5. Loading and Saving Your Data

This chapter will cover three common sets of data sources:

- File formats and filesystems;
- Structured data sources through Spark SQL;
- Databases and key/value stores;

### File Formats

![learning-spark-7.jpg](../images/learning-spark-7.jpg)

- Spark supports reading all the files in a given directory and doing wildcard expansion on the input(e.g., part-*.txt).
- Use sc.textFile or sc.wholeTextFiles to load text files.
- Use saveAsTextFile to outputting files to a directory of file.

### JSON

- The simplest way to load JSON data is by loading the data as a text file and then mapping over the values with a JSON parser.
- Use accumulators to keep track of the number of errors.
- Save as json is much simpler, bellow is how to load and save as json in Python.

```
### load from json
import json
data = input.map(lambda x: json.loads(x))

### save as json
(data.filter(lambda x: x["lovesPandas"]).map(lambda x: json.dumps(x)).saveAsTextFile(outputFile))
```

### Comma-Separated Values and Tab-Separated Values
### SequenceFiles

- SequenceFiles are a popular Hadoop format composed of flat files with key/value pairs. It's a common input/output format for Hadoop MR jobs.
- Hadoop's RecordReader reuses the same object for each record, so directly calling cache on an RDD you read in like this can fail; instead, add a simple map() operation and cache its result. Furthermore, many Hadoop Writable classes do not implement java.io.Serializable, so for them to work in RDDs we need to convert them with a map() anyway. 
- Use sequenceFile(path, keyClass, valueClass, minPartitions) to load sequenceFiles, make sure that keyClass and valueClass should be the Writable class. e.g in Python:

```
data = sc.sequenceFile(inFile, 'org.apache.hadoop.io.Text', 'org.apache.hadoop.io.IntWritable')
```

### Hadoop Input and Output Formats
### File Compression
### Local FS

- Load data from 'local' fs required that all the files are available at the same path on all nodes in your cluster. 
- Some network filesystems are exposed to the user as a regular filesystem, if your data is already in one of these systems, can use it as an input by specifying a file:// path, Spark will handle it as long as the filesystem is mounted at the same path on each node. 
- If your file isn't already on all nodes in the cluster, you can load it locally on the driver without going through Spark and then call parallelize to distribute the contents to workers. This approach can be slow, so recommend put files in a shared filesystem, like HDFS, NFS or S3.  

### HDFS

- HDFS is designed to work on commodity hardware and be resilient to node failure while providing high data throughout. Using Spark with HDFS is as simple as specifying hdfs://master:port/path for your input and output.
- The HDFS protocol changes across Hadoop versions, so if you run a version of Spark that is compiled for a different version it will fail.

### Structured Data with Spark SQL

- Give Spark SQL a sql query to run on the data source, and we get back an RDD of Row objects, one per record.
