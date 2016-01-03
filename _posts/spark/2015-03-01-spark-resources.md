---
layout: post
published: false
title: ［touch spark］10. Spark 学习资源集锦  
description: 我搜集、看过并认为是不错的 Spark 学习资源。
---  

##  
## 1. 写在前面  
　　实际上，学习任何一门技术，最好的学习资料肯定是官网。但是，在我学习spark的过程中，我发现有两个理由告诉我为什么学习一门技术仍然需要一些官网之外的资料：  

- 广度：官网上的资料大都focus在技术本身的实现和用法，而有很多资料会提及这门技术的应用，以及实践、应用这门技术中遇到的坑，还有由这门技术衍生出来的其他辅助技术。    
- 深度：很多资料都会解析这门技术的实现以及原理，反应到官网上，大多都是API文档或技术架构；我发现，很多在官网上理解不了的细节，可能在一些资料上描述起来更明确。

　　基于上面这两个原因，我准备把自己在学习Spark过程中有幸遇到的好的资料搜集起来，并从广度和深度两个方面来整理这些资料，希望对大家有所帮助。还有，我会整理一些和spark相关的第三方开源工具，相信这些工具在帮助大家构建基于spark的应用时会助一臂之力。   

　　所有这些我都会同步到github上：[link](https://github.com/litaotao/spark-materials)

## 2. 资源列表  

- **广度**：[spark和ipython notebook结合](http://blog.cloudera.com/blog/2014/08/how-to-use-ipython-notebook-with-apache-spark/)  
**备注**：我参考这篇文章搭建了自己基于ipython notebook的分析平台，详细记录在这篇博客上了：[当Ipython Notebook遇见Spark](../ipython-notebook-server-spark)

- **广深**：[RDD论文英文版](http://www.cs.berkeley.edu/~matei/papers/2012/nsdi_spark.pdf)   
**备注**：这篇论文绝对值得多读和深读，中文版在[这里](https://code.csdn.net/CODE_Translation/spark_matei_phd)

- 一个对Spark 2分钟的介绍视频，如果有人要你介绍Spark，按照里面的说就perfect了。[YouTube](https://www.youtube.com/watch?v=cs3_3LdCny8)

>>**Apache Spark is：**    
    + A data analytics, cluster computing framework;     
    + Fits into Hadoop open-source community, and builds on top of Hadoop Distributed File System(HDFS);    
    + Not tied to two-stage MapReduce paradigm, it's performance up to 100 times faster than Hadoop MapReduce for certain applications;           
    + Provides primitives for in-memeory cluster computing;           
    + In-memory cluster computing allows user load data to cluster's memory and queried repeatedly;          
    + Suited for machine learning algorithms;              

- **广深**：[Spark专刊之：spark最佳学习路径](http://down.51cto.com/tag-spark%E4%B8%93%E5%88%8A.html)      
- **广深**：[Spark专刊之：spark运行原理解析](http://down.51cto.com/tag-spark%E4%B8%93%E5%88%8A.html)      
**备注**：国人整理和翻译的spark学习资料，质量不错哦~



## 3. Spark相关的第三方开源工具   

- **Zeppelin**：
    + 官网：[http://zeppelin-project.org/](http://zeppelin-project.org/)

- **Hue**:  
    + 官网：[http://gethue.com/](http://gethue.com/)

- **IPyhon**:  
    + 官网：[http://ipython.org/](http://ipython.org/)

- **ISpark**:
    + Github：[https://github.com/tribbloid/ISpark](https://github.com/tribbloid/ISpark)

- **scala-notebook**:  
    + Github: [https://github.com/Bridgewater/scala-notebook](https://github.com/Bridgewater/scala-notebook)

- **spark-notebook**:  
    + Github: [https://github.com/andypetrella/spark-notebook](https://github.com/andypetrella/spark-notebook)

- **Ipython-sql**:  
    + Github: [https://github.com/catherinedevlin/ipython-sql](https://github.com/catherinedevlin/ipython-sql)

- **sparknotebook**:  
    + Github: [https://github.com/hohonuuli/sparknotebook](https://github.com/hohonuuli/sparknotebook)

- **spark-kernel**:
    + Github: [https://github.com/ibm-et/spark-kernel](https://github.com/ibm-et/spark-kernel)

- **spark-jobserver**:
    + Github: [https://github.com/spark-jobserver/spark-jobserver](https://github.com/spark-jobserver/spark-jobserver)

- **spark-packages**:
    + 官网：[http://spark-packages.org/](http://spark-packages.org/)




## 相关资源

- [official site](http://spark.apache.org/)
- [user mailing list](http://apache-spark-user-list.1001560.n3.nabble.com/)
- [spark channel on youtube](https://www.youtube.com/user/TheApacheSpark)
- [spark summit](https://spark-summit.org/)
- [meetup](http://www.meetup.com/)
- [spark third party packages](http://spark-packages.org/)
- [databricks blog](https://databricks.com/blog)
