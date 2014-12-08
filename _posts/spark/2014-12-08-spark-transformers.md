---
category: spark
published: false
layout: post
title: ［touch spark］5. spark RDD transformation 学习
description: 总结spark transformation，了解spark编程内涵～～～	
---  

![transfomers](../../images/transfomers.jpg)

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

## 2. RDD transfomation 一览  
　　ok，了解了RDD的含义，我们可以来看看神马叫transformation了，中文叫转换。上面提到RDD可以由两种方式创建，而在实际应用中，一般第一种方式都是用于新建一个RDD的时候，大多数时候都是通过第二种方式来生成一个新的RDD。so，想想这里我们应该怎么来根据一个已存在的RDD来transform出另一个新的RDD呢？当然就是根据一些规则，比如说筛选，映射，分组等等，而用于支撑这些规则的函数，就叫做RDD的transformation。  
　　下面我们通过下面这张表来看看RDD都支持哪些规则的transformation吧。 这些是[官方](http://spark.apache.org/docs/latest/programming-guide.html#transformations)列出的一些常用的transformation，我原本想把所有transformation列出来的，可考虑到2/8原则，想想下面这些在实际应用中应该足够了。如果真的需要其他transformation的时候，相比彼时你的功力应该已到阅读、贡献源码的级别了。也就不需要再参考我下面将要写的东西了。   
　　这些transformation中有一些是我不太熟悉的，所以这里记录一下我不太熟悉的那些转换函数的用法，仅供个人参考哦。


| No | Transformation  |  Meaning | 
|---|---|---|
| 1 | map(func)  | Return a new distributed dataset formed by passing each element of the source through a function func.  | 
| 2 | filter(func) | Return a new dataset formed by selecting those elements of the source on which func returns true. |
| 3 | flatMap(func) | Similar to map, but each input item can be mapped to 0 or more output items (so func should return a Seq rather than a single item). |
| 4 | mapPartitions(func) | Similar to map, but runs separately on each partition (block) of the RDD, so func must be of type Iterator<T> => Iterator<U> when running on an RDD of type T. |
| 5 | mapPartitionsWithIndex(func) | Similar to mapPartitions, but also provides func with an integer value representing the index of the partition, so func must be of type (Int, Iterator<T>) => Iterator<U> when running on an RDD of type T. |
| 6 | sample(withReplacement, fraction, seed) | Sample a fraction fraction of the data, with or without replacement, using a given random number generator seed. |
| | | |
| | | |


## 3. RDD transfomation  
　　RDD 的transformation有几个和scala里的函数组合子一样，其他的我估计也是基于scala的组合子来写的。所以，为了方便起见，能用scala来展现的，我就用scala来写；不可以的，我再用spark来写示例。下面提到的transformation更新到[spark 1.1.1版本](http://spark.apache.org/docs/latest/programming-guide.html#transformations)。要想查看最新版本的，可以上[官网](http://spark.apache.org/)和[官方API文档](http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.rdd.RDD)。这里顺带提一下，说到transformation，网上几乎每篇说spark的文章都会用到下面这张图。可是我真的想说，这张图可是Matei这哥们2012年发的[RDD论文](https://www.cs.berkeley.edu/~matei/papers/2012/nsdi_spark.pdf)里的啊，spark更新的速度也许比大多数人换对象的速度还快啊，好多东西已经变了。大家以后要是发这张图，就该说明出处和版本吧，免得大家误解transformation和actions就那几种类型啊。
![trans-action-2012](../../images/trans-action-2012.png)


## 3.1 RDD transfomation － flatMap  
　　flatMap可以理解成map和flat的组合。他处理一个嵌套列表，对其中每个列表中的元素执行map，然后对每个列表执行flat，最后返回一个列表。
　　所以，我们也可以先flatten一个列表，再对列表里的每个元素做mapping；当然也可以对嵌套列表里的每个元素做mapping，再对列表做flatten。看下面的例子就明白了：  

```
// flatMap operation
scala> val test = List(List(1,2,3,4,5), List(10,20,30,40,50))
test: List[List[Int]] = List(List(1, 2, 3, 4, 5), List(10, 20, 30, 40, 50))

scala> val test1 = test.flatMap( x => x.map(_ * 2))
test1: List[Int] = List(2, 4, 6, 8, 10, 20, 40, 60, 80, 100)

// flat first, then mapping
scala> val tset2 = test.flatten
tset2: List[Int] = List(1, 2, 3, 4, 5, 10, 20, 30, 40, 50)

scala> val test3 = test.flatten.map(_*2)
test3: List[Int] = List(2, 4, 6, 8, 10, 20, 40, 60, 80, 100)

// mapping first, then flat
scala> val test4 = test.map( x => x.map(_*2))
test4: List[List[Int]] = List(List(2, 4, 6, 8, 10), List(20, 40, 60, 80, 100))

scala> val test5 = test.map(x => x.map(_*2)).flatten
test5: List[Int] = List(2, 4, 6, 8, 10, 20, 40, 60, 80, 100)
```  

## 3.2 RDD transfomation － mapPartitions  
　　

## 3.3 RDD transfomation － mapPartitionsWithIndex  
　　


## 3.3 RDD transfomation －  sample

　　


## 4，一些资源  
- [RDD](http://blog.csdn.net/anzhsoft/article/details/39851421)  
- [scala school from twitter](https://twitter.github.io/scala_school/zh_cn/collections.html#flatMap)