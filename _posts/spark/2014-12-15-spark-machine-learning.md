---
category: spark
published: false
layout: post
title: ［touch spark］6. 使用Spark分析来做一些机器学习的事情
description: 哇，初步体验BDAS---the Berkeley Data Analytics Stack
---  


##   
## 1. 写在前面  
　　BDAS---the Berkeley Data Analytics Stack，不得不说，老美真的好厉害，一下子就呼出个BDAS，霸气外漏啊，不过人家有底气啊，没办法，有才就是任性。这次初步通过一个机器学习的例子再来体会一下spark。

## 2. 这次准备干嘛  
　　这次我们只是体验一下spark在机器学习应用方面一个极小的例子，所以提前准备好了数据。也是用wikipedia的数据wikistats_20090505-07_restricted。  
　　在应用机器学习前，我们首先要分析处理一下数据。即对每一条数据生成一些特征来描述这条数据对特性。在我们下面这个例子里，每条数据由文章ID和相应对统计数据组成。我们将会对每条数据生成24个特征值，学名叫一个24维的特征向量。这里我们用到的这个特征向量很简单，就是每篇文章在每一天每一个小时的浏览量，所以这个特征向量是24维的。  
　　在[这里](../using-amazon-aws-1)回顾下我们的数据文件里每条wiki流量数据的格式如下。 

- date_time: 以YYYYMMDD-HHMMSS格式表示的访问时间，且以小时为单位；  
- project_code：表示对应的页面所使用的语言；  
- page_title：表示访问的wiki标题；  
- num_hits：表示从date_time起一小时内的浏览量；  
- page_size： 表示以字节为单位，这个页面的大小；  

　　下面，我们就在REPL中来建立我们的训练数据。

## 3. 训练数据准备   

### 3.1 载入原始数据   

    val data = sc.textFile("/wikistats_20090505-07_restricted")

### 3.2 数据转换  
　　我们对每一条wiki流量数据做处理，结果是一个两元素的tuple。第一个元素代表文章ID，由project_code和page_title构成，第二个元素是一个键值对，其健是以小时为单位对时间，值是对应的一个小时内的浏览量。关于代码有几点需要说明的，第一是data.map以RDD里的每行数据为输入，先把每行数据拆分成5个元素并分别赋值给dateTime, projectCode, pageTitle, numViews, numBytes这5个变量，然后把hour初始化为int型，然后组合成(element1, key->value)这种形式。  
　　代码如下：  

    val featureMap = data.map(line => {
      val Array(dateTime, projectCode, pageTitle, numViews, numBytes) = 
                 line.trim.split("\\s+")
      val hour = dateTime.substring(9, 11).toInt
      (projectCode+" "+pageTitle, hour -> numViews.toInt)
    })

　　现在我们来计算每篇文章每个小时的平均浏览量。比如说文章A在第一天的第1小时内的浏览量是100，在第二天的第1小时内的浏览量是200，第三天的第1小时内的浏览量是300，那么这篇文章的第1小时平均浏览量就是(100+200+300)/3=200。easy吧，哈哈。  
　　这段代码就有点难度了，具体看代码里的注视吧，这样说起来比较清晰。  
　　代码如下：  

    // 先groupByKey再map，groupByKey后每条featureMap数据是一个两元素的tuple，其中
    // 第一个元素是文章ID，第二个元素是这篇文章这一天内每个小时内的浏览量的键值对。
    val featureGroup = featureMap.groupByKey.map(grouped => {
        // 把每条featureMap的数据拆分成article和hoursViews
      val (article, hoursViews) = grouped
        // 新建两个数组变量，每个数组24个元素，初始化为0
      val sums = Array.fill[Int](24)(0)
      val counts = Array.fill[Int](24)(0)
        // 把每篇文章这几天每个小时的浏览量求和后暂存在counts和sums里
      for((hour, numViews) <- hoursViews) {
        counts(hour) += 1
        sums(hour) += numViews
      }
        // 计算每个小时的平均浏览量，暂存在avgs里，avgs是一个Double类型的数组
        // 其中avgs最后应该是有24个元素的，代表这篇文章这段时间来的小时平均浏览量
      val avgs: Array[Double] =
        for((sum, count) <- sums zip counts) yield
          if(count > 0) sum/count.toDouble else 0.0
        // 构建RDD，这个map操作后每条RDD数据是一个键值对，其键是文章ID，值是
        // 该文章这段时间的小时平均浏览量数组
      article -> avgs
    })

　　现在，假设我们只需要那些有过浏览历史的数据，所以要简单的做个筛选。  
    val featureGroupFiltered = featureGroup.filter(t => t._2.forall(_ > 0))

　　现在我们有了每篇文章平均每小时的浏览量，可是这个特征依然不够明显。我们需要对其做一个归一化的处理，这样可以知道每篇文章在一天的哪个时间段内最流行了。关于归一化，知乎的这个[帖子](http://www.zhihu.com/question/20455227)说得不错。  

    val featurizedRDD = featureGroupFiltered.map(t => {
      val avgsTotal = t._2.sum
      t._1 -> t._2.map(_ /avgsTotal)
    })

### 3.3 数据缓存  
　　现在这些数据已经经过层层处理，可以先缓存下来供以后玩了。这里有两种缓存方法，一是缓存到内存里，二是存储到磁盘上，以后再从磁盘上读取。这里我们先缓存到内存里了，同时也缓存到磁盘上。其中缓存到磁盘上的格式也是一条一条的文章流量数据，格式如：文章ID#以逗号","分割的24小时的浏览热度值。

    featurizedRDD.cache.map(t => t._1 + "#" + t._2.mkString(",")).saveAsTextFile("/wikistats_featurized")
　　


## 扫一扫     

![2014-12-15-spark-machine-learning.md](../../images/share/2014-12-15-spark-machine-learning.md.jpg)