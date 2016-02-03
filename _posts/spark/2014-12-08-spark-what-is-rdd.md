---
category: spark
published: false
layout: post
title: ［touch spark］4. spark RDD 之：什么是RDD
description: 要想学好spark，怎么能不先搞清楚RDD的来龙去脉呢～～～	
---  



##  
## 1. 什么是RDD 
　　先看下源码里是怎么描述RDD的。  
>>  
Internally, each RDD is characterized by five main properties:  
A list of partitions  
A function for computing each split   
A list of dependencies on other RDDs  
Optionally, a Partitioner for key-value RDDs (e.g. to say that the RDD is hash-partitioned)   
Optionally, a list of preferred locations to compute each split on (e.g. block locations for an HDFS file)   

　　每个RDD有5个主要的属性：  

- 一组分片（partition），即数据集的基本组成单位  
- 一个计算每个分片的函数  
- 对parent RDD的依赖，这个依赖描述了RDD之间的lineage  
- 对于key-value的RDD，一个Partitioner，这是可选择的  
- 一个列表，存储存取每个partition的preferred位置。对于一个HDFS文件来说，存储每个partition所在的块的位置。这也是可选择的  

　　把上面这5个主要的属性总结一下，可以得出RDD的大致概念。首先要知道，RDD大概是这样一种表示数据集的东西，它具有以上列出的一些属性。是spark项目组设计用来表示数据集的一种数据结构。而spark项目组为了让RDD能handle更多的问题，又规定RDD应该是只读的，分区记录的一种数据集合中。可以通过两种方式来创建RDD：一种是基于物理存储中的数据，比如说磁盘上的文件；另一种，也是大多数创建RDD的方式，即通过其他RDD来创建【以后叫做转换】而成。而正因为RDD满足了这么多特性，所以spark把RDD叫做Resilient Distributed Datasets，中文叫做弹性分布式数据集。很多文章都是先讲RDD的定义，概念，再来说RDD的特性。我觉得其实也可以倒过来，通过RDD的特性反过来理解RDD的定义和概念，通过这种由果溯因的方式来理解RDD也未尝不可。反正对我个人而言这种方式是挺好的。  

## 2. 理解RDD的几个关键概念   
　　本来我是想参考RDD的论文和自己的理解来整理这篇文章的，可是后来想想这样是不是有点过于细致了。我想，认识一个新事物，在时间、资源有限的情况下，不必锱铢必较，可以先focus on几个关键点，到后期应用的时候再步步深入。  
　　所以，按照我个人的理解，我认为想用好spark，必须要理解RDD，而为了理解RDD，我认为只要了解下面几个RDD的几个关键点就能handle很多情况下的问题了。所以，下面所有列到的点，都是在我个人看来很重要的，但也许有所欠缺，大家如果想继续深入，可以看第三部分列出的参考资料，谢谢。
　　
### 2.1 RDD的背景及解决的痛点问题   
　　按照RDD的paper来讲，RDD的设计是为了充分利用分布式系统中的内存资源，使得提升一些特定的应用的效率。这里所谓的特定的应用没有明确定义，但可以理解为一类应用到迭代算法，图算法等需要重复利用数据的应用类型；除此之外，RDD还可以应用在交互式大数据处理方面。所以，我们这里需要明确一下：RDD并不是万能的，也不是什么带着纱巾的少女那样神奇。简单的理解，就是一群大牛为了解决一个问题而设计的一个特定的数据结构，that's all。

### 2.2 What is DAG - 趣说有向无环图
　　DAG - Direct Acyclic Graph，有向五无图，好久没看图片了，先发个图片来理解理解吧。
![DAG](../../images/dag.jpg)  
　　要理解DAG，只需弄明白三个概念就可以毕业了，首先，我们假设上图图二中的A,B,C,D,E都代表spark里不同的RDD：    

- 图：图是表达RDD Lineage信息的一个结构，在spark中，大部分RDD都是通过其他RDD进行转换而来的，比如说上图图二中，B和D都是通过A转换而来的，而C是通过B转换而来，E的话是通过B和D一起转换来的。
- 有向：有向就更容易理解了，简单来说就是linage是一个top-down的结构，而且是时间序列上的top-down结构，这里不是很好理解，我们在下面讲“无环”这个概念是一起说明。
- 无环：这里就是重点要理解的地方了，我猜想spark的优化器在这里也发挥了很大的作用。首先，我们先理解一下无环的概念，假设有图三中左下B,D,E这样一个RDD转换图，那当我们的需要执行D.collect操作的时候，就会引发一个死循环了。不过，仔细想过的话，就会知道，“无环”这个问题其实已经在“有向”这个概念中提现了，上面说的“有向”，其实更详细的说是一个时间上的先来后到，即祖先与子孙的关系，是不可逆的。举个例子，我们按照时间序列分析一下图下左下的B,D,E三个RDD：

	1. B通过某种方式初始化了第一个RDD【这里我们抛却A,C不谈】；
	2. D通过某种转换从B生成第二个RDD；
	3. E通过某种转换从D生成第三个RDD；
	4. 现在B这个RDD已经存在了，所以根本无从说明B是从E通过转换生成的，为啥，因为B已经存在了；

　　够清楚了吗，啥，还不够清楚，好，那我告诉你，B是小明他爷爷，D是小明他爸爸，E是小明自己，你说小明他爷爷能是小明通过某种方式转换出现在这个世界上的吗？

### 2.3 What is Data Locality - RDD的位置可见性   
　　这个问题就不重复造轮子了，直接引用Quora上的一个[问答了](https://www.quora.com/How-do-I-make-clear-the-concept-of-RDD-in-Spark)。
>
RDD is a dataset which is distributed, that is, it is divided into "partitions". Each of these partitions can be present in the memory or disk of different machines. If you want Spark to process the RDD, then Spark needs to launch one task per partition of the RDD. Its best that each task be sent to the machine have the partition that task is supposed to process. In that case, the task will be able to read the data of the partition from the local machine. Otherwise, the task would have to pull the partition data over the network from a different machine, which is less efficient. This scheduling of tasks (that is, allocation of tasks to machines) such that the tasks can read data "locally" is known as "locality aware scheduling".

### 2.4 What is Lazy Evaluation - 神马叫惰性求值 
　　本来不想叫“惰性求值”的，看到“惰”这个字实在是各种不爽，实际上，我觉得应该叫"后续求值"，"按需计算"，"晚点搞"这类似的，哈哈。这几天一直在想应该怎么简单易懂地来表达Lazy Evaluation这个概念，本来打算引用MongoDB的Cursor来类比一下的，可总觉得还是小题大做了。这个概念就懒得解释了，主要是觉得太简单了，没有必要把事情搞得这么复杂，哈哈。


### 2.5 What is Narrow/Wide Dependency - RDD的宽依赖和窄依赖 
　　首先，先从原文看看宽依赖和窄依赖各自的定义。
>
　　**narrow dependencies**: where each partition of the parent RDD is used by at most one partition of the child RDD, **wide dependencis**, where multiple child partitions may depend on it.

　　按照[这篇RDD论文中文译文](http://shiyanjun.cn/archives/744.html)的解释，窄依赖是指子RDD的每个分区依赖于常数个父分区（即与数据规模无关）；宽依赖指子RDD的每个分区依赖于所有父RDD分区。暂且不说这样理解是否有偏差，我们先来从两个方面了解下计算一个窄依赖的子RDD和一个宽依赖的RDD时具体都有什么区别，然后再回顾这个定义。  

- 计算方面：
	- 计算窄依赖的子RDD：可以在某一个计算节点上直接通过父RDD的某几块数据（通常是一块）计算得到子RDD某一块的数据；
	- 计算宽依赖的子RDD：子RDD某一块数据的计算必须等到它的父RDD所有数据都计算完成之后才可以进行，而且需要对父RDD的计算结果进行hash并传递到对应的节点之上；

- 容错恢复方面：
	+ 窄依赖：当父RDD的某分片丢失时，只有丢失的那一块数据需要被重新计算；  
	+ 宽依赖：当父RDD的某分片丢失时，需要把父RDD的所有分区数据重新计算一次，计算量明显比窄依赖情况下大很多；  

## 3. 尚未提到的一些重要概念  
　　还有一些基本概念上面没有提到，一些是因为自己还没怎么弄清楚，一些是觉得重要但是容易理解的，所以就先不记录下来了。比如说：粗粒度、细粒度；序列化和反序列化等。
　　


## 4. 参考资料  
- [Spark技术内幕：究竟什么是RDD](http://blog.csdn.net/anzhsoft/article/details/39851421)   
- [Resilient Distributed Datasets: A Fault-Tolerant Abstraction for
In-Memory Cluster Computing](http://www.cs.berkeley.edu/~matei/papers/2012/nsdi_spark.pdf)    
- [RDD 论文中文版](http://shiyanjun.cn/archives/744.html )

　　


## 扫一扫     

![2014-12-08-spark-what-is-rdd.md](../../images/share/2014-12-08-spark-what-is-rdd.md.jpg)