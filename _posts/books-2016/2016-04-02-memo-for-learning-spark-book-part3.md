---
category: books
published: false
layout: post
title: 『 读书笔记 』Learning Spark [part 3]
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


## 10. Spark Streaming

Much like Spark is built on the concept of RDDs, Spark Streaming provides an abstraction called DStreams, or discretized streams. A DStream is a sequence of data arriving over time. Internally, each DStream is represented as a sequence of RDDs arriving at each time step (hence the name “discretized”). DStreams can be created from various input sources, such as Flume, Kafka, or HDFS. Once built, they offer two types of operations: transformations, which yield a new DStream, and output operations, which write data to an external system. DStreams provide many of the same operations available on RDDs, plus new operations related to time, such as sliding windows.

Unlike batch programs, Spark Streaming applications need additional setup in order to operate 24/7. We will discuss checkpointing, the main mechanism Spark Streaming provides for this purpose, which lets it store data in a reliable file system such as HDFS. We will also discuss how to restart applications on failure or set them to be automatically restarted.

### 10.1 Architecture and Abstraction

Spark Streaming uses a *micro-batch* architecture, where the streaming computation is treated as a continuous series of batch computations on small batches of data. Spark Streaming receives data from various input sources and groups it into small batches. New batches are created at regular time intervals. At the beginning of each time interval a new batch is created, and any data that arrives during that interval gets added to that batch. At the end of the time interval the batch is done growing. The size of the time intervals is determined by a parameter called the batch interval. The batch interval is typically between 500 milliseconds and several seconds, as configured by the application developer. Each input batch forms an RDD, and is processed using Spark jobs to create other RDDs. The processed results can then be pushed out to external systems in batches. This high-level architecture is shown bellow:


![learning-spark-1-11.jpg](../images/learning-spark-1-11.jpg)

the programming abstraction in Spark Streaming is a discretized stream or a DStream (shown in Figure 10-2), which is a sequence of RDDs, where each RDD has one time slice of the data in the stream.

![learning-spark-1-12.png](../images/learning-spark-1-12.png)

The execution of Spark Streaming within Spark’s driver-worker components is shown in bellow. For each input source, Spark Streaming launches receivers, which are tasks running within the application’s executors that collect data from the input source and save it as RDDs. These receive the input data and replicate it (by default) to another executor for fault tolerance. This data is stored in the memory of the executors in the same way as cached RDDs. The StreamingContext in the driver program then periodically runs Spark jobs to process this data and combine it with RDDs from previous time steps.

![learning-spark-1-13.png](../images/learning-spark-1-13.png)

Spark Streaming offers the same fault-tolerance properties for DStreams as Spark has for RDDs: as long as a copy of the input data is still available, it can recompute any state derived from it using the lineage of the RDDs (i.e., by rerunning the operations used to process it). By default, received data is replicated across two nodes, as mentioned, so Spark Streaming can tolerate single worker failures. Using just lineage, however, recomputation could take a long time for data that has been built up since the beginning of the program. Thus, Spark Streaming also includes a mechanism called checkpointing that saves state periodically to a reliable filesystem (e.g., HDFS or S3). Typically, you might set up checkpointing every 5–10 batches of data. When recovering lost data, Spark Streaming needs only to go back to the last checkpoint.

### 10.2 Transformations

Transformations on DStreams can be grouped into either stateless or stateful:

- In stateless transformations the processing of each batch does not depend on the data of its previous batches. They include the common RDD transformations we have seen before, like *map(), filter(), and reduceByKey()*.
- Stateful transformations, in contrast, use data or intermediate results from previous batches to compute the results of the current batch. They include transformations based on sliding windows and on tracking state across time.

#### 10.2.1 Stateless Transformations

Stateless transformations are simple RDD transformations being applied on every batch[every RDD in a DStream]. Note that key/value DStream transformations like *reduceByKey()* are made available in Scala by *import StreamingContext._*. In Java, as with RDDs, it is necessary to create a JavaPairDStream using *mapToPair()*.

Keep in mind that although these functions look like they’re applying to the whole stream, internally *each DStream is composed of multiple RDDs (batches)*, and each stateless transformation applies separately to each RDD. For example, *reduceByKey()* will reduce data within each time step, but not across time steps. The stateful transformations we cover later allow combining data across time.

Stateless transformations can also combine data from multiple DStreams, again within each time step. For example, key/value DStreams have the same join-related transformations as RDDs—namely, *cogroup(), join(), leftOuterJoin()*, and so on (see “Joins”). We can use these operations on DStreams to perform the underlying RDD operations separately on each batch.

#### 10.2.2 Stateful Transformations

Stateful transformations are operations on DStreams that track data across time; that is, some data from previous batches is used to generate the results for a new batch. The two main types are windowed operations, which act over a sliding window of time periods, and *updateStateByKey()*, which is used to track state across events for each key.

Stateful transformations require checkpointing to be enabled in your StreamingContext for fault tolerance. We will discuss checkpointing in more detail in “24/7 Operation”, but for now, you can enable it by passing a directory to *ssc.checkpoint()*.

#### 10.2.3 Windowed Transformations

Windowed operations compute results across a longer time period than the StreamingContext’s batch interval, by combining results from multiple batches. 

All windowed operations need two parameters, *window duration and sliding duration*, both of which must be a multiple of the StreamingContext’s batch interval. The window duration controls how many previous batches of data are considered, namely the last windowDuration/batchInterval. If we had a source DStream with a batch interval of 10 seconds and wanted to create a sliding window of the last 30 seconds (or last 3 batches) we would set the windowDuration to 30 seconds. The sliding duration, which defaults to the batch interval, controls how frequently the new DStream computes results. If we had the source DStream with a batch interval of 10 seconds and wanted to compute our window only on every second batch, we would set our sliding interval to 20 seconds. 

The simplest window operation we can do on a DStream is *window()*, which returns a new DStream with the data for the requested window. In other words, each RDD in the DStream resulting from *window()* will contain data from multiple batches, which we can then process with count(), transform(), and so on. 

![learning-spark-1-14.png](../images/learning-spark-1-14.png)

While we can build all other windowed operations on top of *window()*, Spark Streaming provides a number of other windowed operations for efficiency and convenience. First, *reduceByWindow()* and *reduceByKeyAndWindow()* allow us to perform reductions on each window more efficiently. They take a single reduce function to run on the whole window, such as *+*. In addition, they have a special form that allows Spark to compute the reduction incrementally, by considering only which data is coming into the window and which data is going out. This special form requires an inverse of the reduce function, such as *-* for *+*. It is much more efficient for large windows if your function has an inverse.

![learning-spark-1-15.png](../images/learning-spark-1-15.png)

#### 10.2.4 Updatestatebykey Transformations

Sometimes it’s useful to maintain state across the batches in a DStream. *updateStateByKey()* enables this by providing access to a state variable for DStreams of *key/value pairs*. Given a DStream of (key, event) pairs, it lets you construct a new DStream of (key, state) pairs by taking a function that specifies how to update the state for each key given new events. 

To use *updateStateByKey()*, we provide a function *update(events, oldState)* that takes in the events that have arrived for a key and its previous state, and returns a newState to store for it. This function’s signature is as follows:

- events is a list of events that arrived in the current batch (may be empty).
- oldState is an optional state object, stored within an Option; it might be missing if there was no previous state for the key.
- newState, returned by the function, is also an Option; we can return an empty Option to specify that we want to delete the state.

The result of *updateStateByKey()* will be a new DStream that contains an RDD of (key, state) pairs on each time step.


### 10.3 Output Operations

Much like lazy evaluation in RDDs, if no output operation is applied on a DStream and any of its descendants, then those DStreams will not be evaluated. And if there are no output operations set in a StreamingContext, then the context will not start.

Once we’ve debugged our program, we can also use output operations to save results. Spark Streaming has similar *save()* operations for DStreams, each of which takes a directory to save files into and an optional suffix. The results of each batch are saved as subdirectories in the given directory, with the time and the suffix in the filename. 

### 10.4. Input Sources

#### 10.4.1 Stream of Files

Since Spark supports reading from any Hadoop-compatible filesystem, Spark Streaming naturally allows a stream to be created from files written in a directory of a Hadoop-compatible filesystem. This is a popular option due to its support of a wide variety of backends, especially for log data that we would copy to HDFS anyway. For Spark Streaming to work with the data, it needs to have a consistent date format for the directory names and the files have to be created atomically (e.g., by moving the file into the directory Spark is monitoring).

#### 10.4.2 Apache Kafka

Apache Kafka is popular input source due to its speed and resilience. Using the native support for Kafka, we can easily process the messages for many topics. To use it, we have to include the Maven artifact spark-streaming-kafka_2.10 to our project. The provided KafkaUtils object works on StreamingContext and JavaStreamingContext to create a DStream of your Kafka messages. Since it can subscribe to multiple topics, the DStream it creates consists of pairs of topic and message. To create a stream, we will call the *createStream()* method with our streaming context, a string containing comma-separated ZooKeeper hosts, the name of our consumer group (a unique name), and a map of topics to number of receiver threads to use for that topic.

#### 10.4.3 Apache Flume

#### 10.4.5 Custom Input Sources

In addition to the provided sources, you can also implement your own receiver. This is described in Spark’s documentation in the Streaming Custom Receivers guide.

#### 10.4.6 Multiple Sources and Cluster Sizing

As covered earlier, we can combine multiple DStreams using operations like *union()*. Through these operators, we can combine data from multiple input DStreams. Sometimes multiple receivers are necessary to increase the aggregate throughput of the ingestion (if a single receiver becomes the bottleneck). Other times different receivers are created on different sources to receive different kinds of data, which are then combined using joins or cogroups.

It is important to understand how the receivers are executed in the Spark cluster to use multiple ones. *Each receiver runs as a long-running task within Spark’s executors, and hence occupies CPU cores allocated to the application*. In addition, there need to be available cores for processing the data. This means that *in order to run multiple receivers, you should have at least as many cores as the number of receivers, plus however many are needed to run your computation*. For example, if we want to run 10 receivers in our streaming application, then we have to allocate at least 11 cores.

Do not run Spark Streaming programs locally with master configured as "local" or "local[1]". This allocates only one CPU for tasks and if a receiver is running on it, there is no resource left to process the received data. Use at least "local[2]" to have more cores.

### 10.5 24/7 Operation

One of the main advantages of Spark Streaming is that it provides strong fault tolerance guarantees. As long as the input data is stored reliably, Spark Streaming will always compute the correct result from it, offering “exactly once” semantics (i.e., as if all of the data was processed without any nodes failing), even if workers or the driver fail.

To run Spark Streaming applications 24/7, you need some special setup. The first step is setting up checkpointing to a reliable storage system, such as HDFS or Amazon S3. In addition, we need to worry about the fault tolerance of the driver program (which requires special setup code) and of unreliable input sources. This section covers how to perform this setup.

#### 10.5.1 Checkpointing

Checkpointing is the main mechanism that needs to be set up for fault tolerance in Spark Streaming. It allows Spark Streaming to periodically save data about the application to a reliable storage system, such as HDFS or Amazon S3, for use in recovering. Specifically, checkpointing serves two purposes:

- Limiting the state that must be recomputed on failure. As discussed in *Architecture and Abstraction*, Spark Streaming can recompute state using the lineage graph of transformations, but checkpointing controls how far back it must go.
- Providing fault tolerance for the driver. If the driver program in a streaming application crashes, you can launch it again and tell it to recover from a checkpoint, in which case Spark Streaming will read how far the previous run of the program got in processing the data and take over from there.

For these reasons, checkpointing is important to set up in any production streaming application. You can set it by passing a path (either HDFS, S3, or local filesystem) to the *ssc.checkpoint()* method.

#### 10.5.2 Driver Fault Tolerance

Tolerating failures of the driver node requires a special way of creating our StreamingContext, which takes in the checkpoint directory. Instead of simply calling new StreamingContext, we need to use the *StreamingContext.getOrCreate()* function. 

{% highlight scala %}

def createStreamingContext() = {
  ...
  val sc = new SparkContext(conf)
  // Create a StreamingContext with a 1 second batch size
  val ssc = new StreamingContext(sc, Seconds(1))
  ssc.checkpoint(checkpointDir)
}
...
val ssc = StreamingContext.getOrCreate(checkpointDir, createStreamingContext _)

{% endhighlight %}

When this code is run the first time, assuming that the checkpoint directory does not yet exist, the *StreamingContext* will be created when you call the factory function. In the factory, you should set the checkpoint directory. After the driver fails, if you restart it and run this code again, *getOrCreate()* will reinitialize a StreamingContext from the checkpoint directory and resume processing.

In addition to writing your initialization code using *getOrCreate()*, you will need to actually restart your driver program when it crashes. On most cluster managers, Spark does not automatically relaunch the driver if it crashes, so you need to monitor it using a tool like monit and restart it. The best way to do this is probably specific to your environment. One place where Spark provides more support is the Standalone cluster manager, which supports a *--supervise* flag when submitting your driver that lets Spark restart it. You will also need to pass *--deploy-mode cluster* to make the driver run within the cluster and not on your local machine.

When using this option, you will also want the Spark Standalone master to be fault-tolerant. You can configure this using ZooKeeper, as described in the Spark documentation. With this setup, your application will have no single point of failure.

Finally, note that when the driver crashes, executors in Spark will also restart. This may be changed in future Spark versions, but it is expected behavior in 1.2 and earlier versions, as the executors are not able to continue processing data without a driver. Your relaunched driver will start new executors to pick up where it left off.

#### 10.5.3 Worker Fault Tolerance

For failure of a worker node, Spark Streaming uses the same techniques as Spark for its fault tolerance. All the data received from external sources is replicated among the Spark workers. All RDDs created through transformations of this replicated input data are tolerant to failure of a worker node, as the RDD lineage allows the system to recompute the lost data all the way from the surviving replica of the input data.

#### 10.5.4 Receiver Fault Tolerance

The fault tolerance of the workers running the receivers is another important consideration. In such a failure, Spark Streaming restarts the failed receivers on other nodes in the cluster. However, whether it loses any of the received data depends on the nature of the source (whether the source can resend data or not) and the implementation of the receiver (whether it updates the source about received data or not). For example, with Flume, one of the main differences between the two receivers is the data loss guarantees. With the receiver-pull-from-sink model, Spark removes the elements only once they have been replicated inside Spark. For the push-to-receiver model, if the receiver fails before the data is replicated some data can be lost. In general, for any receiver, you must also consider the fault-tolerance properties of the upstream source (transactional, or not) for ensuring zero data loss.

In general, receivers provide the following guarantees:

- All data read from a reliable filesystem (e.g., with StreamingContext.hadoopFiles) is reliable, because the underlying filesystem is replicated. Spark Streaming will remember which data it processed in its checkpoints and will pick up again where it left off if your application crashes.
- For unreliable sources such as Kafka, push-based Flume, or Twitter, Spark replicates the input data to other nodes, but it can briefly lose data if a receiver task is down. In Spark 1.1 and earlier, received data was replicated in-memory only to executors, so it could also be lost if the driver crashed (in which case all executors disconnect). In Spark 1.2, received data can be logged to a reliable filesystem like HDFS so that it is not lost on driver restart.

To summarize, therefore, the best way to ensure all data is processed is to use a reliable input source (e.g., HDFS or pull-based Flume). This is generally also a best practice if you need to process the data later in batch jobs: it ensures that your batch jobs and streaming jobs will see the same data and produce the same results.

#### 10.5.6 Processing Guarantees

Due to Spark Streaming’s worker fault-tolerance guarantees, it can provide exactly-once semantics for all transformations—even if a worker fails and some data gets reprocessed, the final transformed result (that is, the transformed RDDs) will be the same as if the data were processed exactly once.

However, when the transformed result is to be pushed to external systems using output operations, the task pushing the result may get executed multiple times due to failures, and some data can get pushed multiple times. Since this involves external systems, it is up to the system-specific code to handle this case. We can either use transactions to push to external systems (that is, atomically push one RDD partition at a time), or design updates to be idempotent operations (such that multiple runs of an update still produce the same result). For example, Spark Streaming’s saveAs...File operations automatically make sure only one copy of each output file exists, by atomically moving a file to its final destination when it is complete.

### 10.6 Streaming UI

### 10.7 Performance Considerations

#### 10.7.1 Batch and Window Sizes

The most common question is what minimum batch size Spark Streaming can use. In general, 500 milliseconds has proven to be a good minimum size for many applications. The best approach is to start with a larger batch size (around 10 seconds) and work your way down to a smaller batch size. If the processing times reported in the Streaming UI remain consistent, then you can continue to decrease the batch size, but if they are increasing you may have reached the limit for your application.

In a similar way, for windowed operations, the interval at which you compute a result (i.e., the slide interval) has a big impact on performance. Consider increasing this interval for expensive computations if it is a bottleneck.

#### 10.7.2 Level of Parallelism

A common way to reduce the processing time of batches is to increase the parallelism. There are three ways to increase the parallelism:

- Increasing the number of receivers

Receivers can sometimes act as a bottleneck if there are too many records for a single machine to read in and distribute. You can add more receivers by creating multiple input DStreams (which creates multiple receivers), and then applying union to merge them into a single stream.

- Explicitly repartitioning received data

If receivers cannot be increased anymore, you can further redistribute the received data by explicitly repartitioning the input stream (or the union of multiple streams) using DStream.repartition.

- Increasing parallelism in aggregation

For operations like *reduceByKey()*, you can specify the parallelism as a second parameter, as already discussed for RDDs.

#### 10.7.3 Garbage Collection and Memory Usage

Another aspect that can cause problems is Java’s garbage collection. You can minimize unpredictably large pauses due to GC by enabling Java’s Concurrent Mark-Sweep garbage collector. The Concurrent Mark-Sweep garbage collector does consume more resources overall, but introduces fewer pauses.

We can control the GC by adding *-XX:+UseConcMarkSweepGC to the spark.executor.extraJavaOptions* configuration parameter. 

In addition to using a garbage collector less likely to introduce pauses, you can make a big difference by reducing GC pressure. Caching RDDs in serialized form (instead of as native objects) also reduces GC pressure, which is why, by default, RDDs generated by Spark Streaming are stored in serialized form. Using Kryo serialization further reduces the memory required for the in-memory representation of cached data.

Spark also allows us to control how cached/persisted RDDs are evicted from the cache. By default Spark uses an *LRU [least recentyly used] cache*. Spark will also explicitly evict RDDs older than a certain time period if you set *spark.cleaner.ttl*. By preemptively evicting RDDs that we are unlikely to need from the cache, we may be able to reduce the GC pressure.



## 参考文章

- [learning spark on safaribook](https://www.safaribooksonline.com/library/view/learning-spark/9781449359034/)
- [code of learning spark on github](https://github.com/databricks/learning-spark)
- [spark-summit](https://spark-summit.org/)



