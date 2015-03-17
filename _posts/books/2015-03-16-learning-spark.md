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