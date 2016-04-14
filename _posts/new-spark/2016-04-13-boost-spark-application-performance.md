---
layout: post
published: false
title: 『 Spark 』9. spark 应用程序性能优化
description: know more, do better 
---  


## 写在前面

本系列是综合了自己在学习spark过程中的理解记录 ＋ 对参考文章中的一些理解 ＋ 个人实践spark过程中的一些心得而来。写这样一个系列仅仅是为了梳理个人学习spark的笔记记录，所以一切以能够理解为主，没有必要的细节就不会记录了，而且文中有时候会出现英文原版文档，只要不影响理解，都不翻译了。若想深入了解，最好阅读参考文章和官方文档。

其次，本系列是基于目前最新的 spark 1.6.0 系列开始的，spark 目前的更新速度很快，记录一下版本好还是必要的。   
最后，如果各位觉得内容有误，欢迎留言备注，所有留言 24 小时内必定回复，非常感谢。     
Tips: 如果插图看起来不明显，可以：1. 放大网页；2. 新标签中打开图片，查看原图哦。


## 1. 优化? Why? How? When? What?

![how_when_what_why.jpg](../images/how_when_what_why.jpg)

“spark 应用程序也需要优化？”，很多人可能会有这个疑问，“不是已经有代码生成器，执行优化器，pipeline 什么的了的吗？”。是的，spark 的确是有一些列强大的内置工具，让你的代码在执行时更快。但是，如果一切都依赖于工具，框架来做的话，我想那只能说明两个问题：1. 你对这个框架仅仅是知其然，而非知其所以然；2. 看来你也只是照葫芦画瓢而已，没了你，别人也可以轻轻松松的写这样一个 spark 应用程序，so you are replaceable;

在做 spark 应用程序的优化的时候，从下面几个点出发就够了：

- 为什么：因为你的资源有限，因为你的应用上生产环境了会有很多不稳定的因素，在上生产前做好优化和测试是唯一一个降低不稳定因素影响的办法；
- 怎么做：web ui ＋ log 是做优化的倚天剑和屠龙刀，能掌握好这两点就可以了；
- 何时做：应用开发成熟时，满足业务要求时，就可以根据需求和时间安排开始做了；
- 做什么：一般来说，spark 应用程序 80% 的优化，都是集中在三个地方：内存，磁盘io，网络io。再细点说，就是 driver，executor 的内存，shuffle 的设置，文件系统的配置，集群的搭建，集群和文件系统的搭建［e.g 尽量让文件系统和集群都在一个局域网内，网络更快；如果可以，可以让 driver 和 集群也在一个局域网内，因为有时候需要从 worker 返回数据到 driver］

OK，下面我们来看看一些常见的优化方法。


## 2. repartition and coalesce

[原文：](https://www.safaribooksonline.com/library/view/learning-spark/9781449359034/ch04.html)


    Spark provides the `repartition()` function, which shuffles the data 
    across the network to create a new set of partitions. Keep in mind 
    that repartitioning your data is a fairly expensive operation. Spark 
    also has an optimized version of `repartition()` called `coalesce()` 
    that allows avoiding data movement, but only if you are decreasing 
    the number of RDD partitions. To know whether you can safely call 
    coalesce(), you can check the size of the RDD using `rdd.partitions.size()` 
    in Java/Scala and `rdd.getNumPartitions()` in Python and make sure 
    that you are coalescing it to fewer partitions than it currently has.

总结：当要对 rdd 进行重新分片时，如果目标片区数量小于当前片区数量，那么用 `coalesce`，不要用 `repartition`。关于 `partition` 的更多优化细节，参考 [chapter 4 of Learning Spark](https://www.safaribooksonline.com/library/view/learning-spark/9781449359034/ch04.html)

## 3. Passing Functions to Spark

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

## 4. 



## 6. Next

这个例子还算 ok 吧，可是我每天都应用的投资策略的一部分啊，已经下血本了，各位还不打赏打赏吗？哈哈，上次简单介绍了 dataframe，下次我准备再讲讲 datasets，然后总结一下 rdd，dataframe 和 datasets 这三者之间扑朔迷离，藕断丝连的各种迷情。

## 7. 打开微信，扫一扫，点一点，棒棒的，^_^

![wechat_pay_6-6.png](../images/wechat_pay_6-6.png)


## 参考文章

- [chapter 4 of Learning Spark](https://www.safaribooksonline.com/library/view/learning-spark/9781449359034/ch04.html)
- [chapter 8 of Learning Spark](https://www.safaribooksonline.com/library/view/learning-spark/9781449359034/ch08.html)
- [Top 5 Mistakes When Writing Spark Applications](https://www.youtube.com/watch?v=WyfHUNnMutg)
- [Databricks Spark Knowledge Base](https://www.gitbook.com/book/databricks/databricks-spark-knowledge-base/details)


## 本系列文章链接

- [『 Spark 』1. spark 简介 ](../introduction-to-spark)
- [『 Spark 』2. spark 基本概念解析 ](../spark-questions-concepts)
- [『 Spark 』3. spark 编程模式 ](../spark-programming-model)
- [『 Spark 』4. spark 之 RDD ](../spark-what-is-rdd)
- [『 Spark 』5. 这些年，你不能错过的 spark 学习资源 ](../spark-resouces-blogs-paper)
- [『 Spark 』6. 深入研究 spark 运行原理之 job, stage, task](../deep-into-spark-exection-model)
- [『 Spark 』7. 使用 Spark DataFrame 进行大数据分析](../spark-dataframe-introduction)
