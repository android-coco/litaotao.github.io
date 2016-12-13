---
layout: post
published: true
title: 『 Spark 』5. 这些年，你不能错过的 spark 学习资源
description: 在品尝 spark 过程中收集的一些好文，好站 
---  

## 写在前面

本系列是综合了自己在学习spark过程中的理解记录 ＋ 对参考文章中的一些理解 ＋ 个人实践spark过程中的一些心得而来。写这样一个系列仅仅是为了梳理个人学习spark的笔记记录，所以一切以能够理解为主，没有必要的细节就不会记录了，而且文中有时候会出现英文原版文档，只要不影响理解，都不翻译了。若想深入了解，最好阅读参考文章和官方文档。

其次，本系列是基于目前最新的 spark 1.6.0 系列开始的，spark 目前的更新速度很快，记录一下版本号还是必要的。   
最后，如果各位觉得内容有误，欢迎留言备注，所有留言 24 小时内必定回复，非常感谢。     

Tips: 如果插图看起来不明显，可以：1. 放大网页；2. 新标签中打开图片，查看原图哦；3. 点击右边目录上方的 *present mode* 哦。


## 1. 书籍，在线文档

- [Learning Spark](https://www.amazon.cn/Spark%E5%BF%AB%E9%80%9F%E5%A4%A7%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90-%E7%BE%8E-%E5%8D%A1%E5%8A%B3-%E7%BE%8E-%E8%82%AF%E7%BB%B4%E5%B0%BC%E6%96%AF%E7%A7%91-%E7%BE%8E-%E6%B8%A9%E5%BE%B7%E5%B0%94-%E5%8A%A0-%E6%89%8E%E5%93%88%E9%87%8C%E4%BA%9A/dp/B016DWSEXI/ref=sr_1_1?ie=UTF8&qid=1460447269&sr=8-1&keywords=spark+%E5%BF%AB%E9%80%9F%E5%A4%A7%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90)
- [Advanced.Analytics.with.Spark](https://www.amazon.cn/Advanced-Analytics-with-Spark-Patterns-for-Learning-from-Data-at-Scale-Ryza-Sandy/dp/1491912766/ref=sr_1_3?ie=UTF8&qid=1466065861&sr=8-3&keywords=Advanced.Analytics.with.Spark)
- [Mastering Apache Spark](https://www.gitbook.com/book/jaceklaskowski/mastering-apache-spark/details)
- [Official Guide](http://spark.apache.org/docs/latest/)
- [Spark Guide by Cloudera](http://www.cloudera.com/documentation/enterprise/latest/topics/spark.html)


## 2. 网站

- [official site](http://spark.apache.org/)
- [user mailing list](http://apache-spark-user-list.1001560.n3.nabble.com/)
- [spark channel on youtube](https://www.youtube.com/user/TheApacheSpark)
- [spark summit](https://spark-summit.org/)
- [spark technology center](http://www.spark.tc/)
- [sparkhub](https://sparkhub.databricks.com/)
- [meetup](http://www.meetup.com/)
- [spark third party packages](http://spark-packages.org/)
- [databricks blog](https://databricks.com/blog)
- [http://blog.madhukaraphatak.com/](http://blog.madhukaraphatak.com/)
- [databricks docs](https://docs.cloud.databricks.com/docs/latest/sample_applications/index.html#Introduction%20(Readme).html)
- [databricks training](https://docs.cloud.databricks.com/docs/latest/courses/index.html#Introduction%20to%20Big%20Data%20with%20Apache%20Spark%20(CS100-1x)/Introduction%20(README).html)
- [cloudera blog about spark](http://blog.cloudera.com/blog/category/spark/)
- [https://0x0fff.com](https://0x0fff.com)
- [http://techsuppdiva.github.io/](http://techsuppdiva.github.io/)
- [csdn spark 知识库](http://lib.csdn.net/base/10)
- [过往记忆](http://www.iteblog.com/archives/category/spark)


## 3. Databricks Blog

- [Apache Spark 1.5 DataFrame API Highlights: Date/Time/String Handling, Time Intervals, and UDAFs](https://databricks.com/blog/2015/09/16/apache-spark-1-5-dataframe-api-highlights.html)
- [Achieving End-to-end Security for Apache Spark with Databricks](https://databricks.com/blog/2016/06/08/achieving-end-to-end-security-for-apache-spark-with-databricks.html)

>>
上面两篇是 databricks 出的关于 databricks 专业版的描述，虽然没有从根本上解决问题，但是读起来还是挺有说服力的，哈哈，因为采用了很多很细节的方案。不错不错，各位有在做云产品的，在宣传自己的安全方案时可用参考参考哦。

- [Deep Dive into Spark SQL’s Catalyst Optimizer](https://databricks.com/blog/2015/04/13/deep-dive-into-spark-sqls-catalyst-optimizer.html)
- [A Tale of Three Apache Spark APIs: RDDs, DataFrames, and Datasets](https://databricks.com/blog/2016/07/14/a-tale-of-three-apache-spark-apis-rdds-dataframes-and-datasets.html)
- [Understanding your Apache Spark application through visualization](https://databricks.com/blog/2015/06/22/understanding-your-spark-application-through-visualization.html)
- [New Visualizations for Understanding Apache Spark Streaming Applications](https://databricks.com/blog/2015/07/08/new-visualizations-for-understanding-apache-spark-streaming-applications.html)
- [An Introduction to Writing Apache Spark Applications on Databricks](https://databricks.com/blog/2016/06/15/an-introduction-to-writing-apache-spark-applications-on-databricks.html)
- [A Gentle Introduction to Apache Spark on Databricks](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/346304/2168141618055043/484361/latest.html)
- [Apache Spark on Databricks for Data Scientists](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/346304/2168141618055194/484361/latest.html)
- [ Import Notebook Apache Spark on Databricks for Data Engineers](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/346304/2168141618055109/484361/latest.html)
- [Structured Streaming In Apache Spark: A new high-level API for streaming](https://databricks.com/blog/2016/07/28/structured-streaming-in-apache-spark.html)
- [Spark SQL Supported Syntax](https://github.com/databricks/spark-sql-perf/blob/master/src/main/scala/com/databricks/spark/sql/perf/tpcds/TPCDS_1_4_Queries.scala)
- [Combining Machine Learning Frameworks with Apache Spark](http://www.slideshare.net/databricks/combining-machine-learning-frameworks-with-apache-spark)
- [Deep Dive: Memory Management in Apache Spark](http://www.slideshare.net/databricks/deep-dive-memory-management-in-apache-spark)



## 4. 文章，博客

- [RDD论文英文版](http://www.cs.berkeley.edu/~matei/papers/2012/nsdi_spark.pdf)   
- [RDD论文中文版](https://code.csdn.net/CODE_Translation/spark_matei_phd)
- [An Architecture for Fast and General Data Processing
on Large Clusters](http://www.eecs.berkeley.edu/Pubs/TechRpts/2014/EECS-2014-12.pdf)
- [How-to: Tune Your Apache Spark Jobs (Part 1)](http://blog.cloudera.com/blog/2015/03/how-to-tune-your-apache-spark-jobs-part-1/)
- [How-to: Tune Your Apache Spark Jobs (Part 2)](http://blog.cloudera.com/blog/2015/03/how-to-tune-your-apache-spark-jobs-part-2/)
- [`By 0x0fff` Spark Misconceptions](https://0x0fff.com/spark-misconceptions/)
- [`By 0x0fff` Spark Architecture](https://0x0fff.com/spark-architecture/)
- [`By 0x0fff` Spark DataFrames are faster, aren’t they?](https://0x0fff.com/spark-dataframes-are-faster-arent-they/)
- [`By 0x0fff` Spark Architecture: Shuffle](https://0x0fff.com/spark-architecture-shuffle/)
- [`By 0x0fff` Modern Data Architecture](https://0x0fff.com/modern-data-architecture/)
- [`By 0x0fff` Spark Architecture Talk](https://0x0fff.com/spark-architecture-talk/)
- [`By 0x0fff` Apache Spark Future](https://0x0fff.com/apache-spark-future/)
- [`By 0x0fff` Data Industry Trends](https://0x0fff.com/data-industry-trends/)
- [`By 0x0fff` Spark Memory Management](https://0x0fff.com/spark-memory-management/)
- [`By 0x0fff` Spark Architecture Video](https://0x0fff.com/spark-architecture-video/)
- [借助 Redis ，让 Spark 提速 45 倍！](http://dataunion.org/22985.html)
- [量化派基于Hadoop、Spark、Storm的大数据风控架构](http://www.csdn.net/article/2015-10-06/2825849)
- [基于Spark的异构分布式深度学习平台](http://geek.csdn.net/news/detail/58867)
- [你对Hadoop和Spark生态圈了解有几许？](http://www.36dsj.com/archives/40723)
- [Hadoop vs Spark](http://www.yuntoutiao.com/dongtai/5389.html)
- [雅虎开源CaffeOnSpark：基于Hadoop/Spark的分布式深度学习](http://geek.csdn.net/news/detail/57656)
- [2016 上海第二次 spark meetup: 1. spark_meetup.pdf](http://litaotao.github.io/files/1. spark_meetup.pdf)
- [2016 上海第二次 spark meetup: 2. Flink_ An unified stream engine.pdf](http://litaotao.github.io/files/2. Flink_ An unified stream engine.pdf)
- [2016 上海第二次 spark meetup: 3. Spark在计算广告领域的应用实践.pdf](http://litaotao.github.io/files/3. Spark在计算广告领域的应用实践.pdf)
- [2016 上海第二次 spark meetup: 4. splunk_spark.pdf](http://litaotao.github.io/files/4. splunk_spark.pdf)
- [基于Spark的医疗和金融大数据](https://prezi.com/w4wjzdq7y0lj/spark/)
- [Monitoring Spark with Graphite and Grafana](http://www.hammerlab.org/2015/02/27/monitoring-spark-with-graphite-and-grafana/)
- [Spark使用CombineTextInputFormat缓解小文件过多导致Task数目过多的问题](http://www.cnblogs.com/yurunmiao/p/5195754.html)
- [Databricks Empowers Enterprises to Secure Their Apache Spark Workloads](http://www.marketwired.com/press-release/databricks-empowers-enterprises-to-secure-their-apache-spark-workloads-2132605.htm)
- [Spark配置参数](http://blog.javachen.com/2015/06/07/spark-configuration.html)
- [Running Spark Python Applications](http://www.cloudera.com/documentation/enterprise/5-5-x/topics/spark_python.html)
- [How-to: Prepare Your Apache Hadoop Cluster for PySpark Jobs](http://blog.cloudera.com/blog/2015/09/how-to-prepare-your-apache-hadoop-cluster-for-pyspark-jobs/)
- [Apache Spark’s Hidden REST API](http://arturmkrtchyan.com/apache-spark-hidden-rest-api)
- [SQL, sqlContext, hiveContext]
    - [What is the difference between Apache Spark SQLContext vs HiveContext?](http://stackoverflow.com/questions/33666545/what-is-the-difference-between-apache-spark-sqlcontext-vs-hivecontext)
    - [SQL Window Functions](https://drill.apache.org/docs/sql-window-functions-introduction/)
    - [Performance Tuning SQL Queries](https://community.modeanalytics.com/sql/tutorial/sql-performance-tuning/)
    - [HIVE-vs-RDBMS](http://hadooptutorial.info/hive-vs-rdbms/)
    - [Windowing and Analytics Functions](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+WindowingAndAnalytics)
- [Spark Memory Issues]
    - [http://www.cnblogs.com/wrencai/p/4231934.html](http://www.cnblogs.com/wrencai/p/4231934.html)
    - [http://stackoverflow.com/questions/32349611/what-should-be-the-optimal-value-for-spark-sql-shuffle-partitions-or-how-do-we-i](http://stackoverflow.com/questions/32349611/what-should-be-the-optimal-value-for-spark-sql-shuffle-partitions-or-how-do-we-i)
    - [http://stackoverflow.com/questions/21138751/spark-java-lang-outofmemoryerror-java-heap-space](http://stackoverflow.com/questions/21138751/spark-java-lang-outofmemoryerror-java-heap-space)
    - [A Beginner's Guide on Troubleshooting Spark Applications](http://www.slideshare.net/jcmia1/a-beginners-guide-on-troubleshooting-spark-applications)
    - [http://www.mincoder.com/article/2381.shtml](http://www.mincoder.com/article/2381.shtml)

## 5. 视频


- [YouTube: what is apache spark](https://www.youtube.com/watch?v=cs3_3LdCny8)
- [Introduction to Spark Architecture](https://www.youtube.com/watch?v=65aV15uDKgA)

- [Top 5 Mistakes When Writing Spark Applications](https://www.youtube.com/watch?v=WyfHUNnMutg)
- [`slide` Top 5 mistakes when writing Spark applications](http://www.slideshare.net/hadooparchbook/top-5-mistakes-when-writing-spark-applications)

- [Tuning and Debugging Apache Spark](https://www.youtube.com/watch?v=kkOG_aJ9KjQ)
- [`slide` Tuning and Debugging Apache Spark](http://www.slideshare.net/pwendell/tuning-and-debugging-in-apache-spark)

- [A Deeper Understanding of Spark Internals - Aaron Davidson (Databricks)](https://www.youtube.com/watch?v=dmL0N3qfSc8)
- [`slide` A Deeper Understanding of Spark Internals - Aaron Davidson (Databricks)](https://spark-summit.org/2014/wp-content/uploads/2014/07/A-Deeper-Understanding-of-Spark-Internals-Aaron-Davidson.pdf)

- [Building, Debugging, and Tuning Spark Machine Learning Pipelines - Joseph Bradley (Databricks)](https://www.youtube.com/watch?v=OednhGRp938)
- [`slide` Building, Debugging, and Tuning Spark Machine Learning Pipelines](http://www.slideshare.net/SparkSummit/building-debugging-and-tuning-spark-machine-leaning-pipelinesjoseph-bradley)

- [Spark DataFrames Simple and Fast Analysis of Structured Data - Michael Armbrust (Databricks)](https://www.youtube.com/watch?v=xWkJCUcD55w)
- [`slide` Spark DataFrames Simple and Fast Analysis of Structured Data - Michael Armbrust (Databricks)](http://www.slideshare.net/databricks/spark-dataframes-simple-and-fast-analytics-on-structured-data-at-spark-summit-2015)

- [Spark Tuning for Enterprise System Administrators](https://www.youtube.com/watch?v=HBZuB3pPri0&feature=youtu.be)
- [`slide` Spark Tuning for Enterprise System Administrators](http://www.slideshare.net/AnyaBida/bida-sse2016final-58237248)

- [Structuring Spark: DataFrames, Datasets, and Streaming](https://www.youtube.com/watch?v=i7l3JQRx7Qw)
- [`slide` Structuring Spark: DataFrames, Datasets, and Streaming](http://www.slideshare.net/databricks/structuring-spark-dataframes-datasets-and-streaming)

- [Spark in Production: Lessons from 100+ Production Users](https://www.youtube.com/watch?v=GzG9RTRTFck)
- [`slide` Spark in Production: Lessons from 100+ Production Users](http://www.slideshare.net/databricks/spark-summit-eu-2015-lessons-from-300-production-users)

- [Production Spark and Tachyon use Cases](https://www.youtube.com/watch?v=rBrsxM091KA)
- [`slide` Production Spark and Tachyon use Cases](http://www.slideshare.net/SparkSummit/using-spark-with-tachyon-by-gene-pang)

- [SparkUI Visualization](https://www.youtube.com/watch?v=VQOKk9jJGcw&index=5&list=PL-x35fyliRwif48cPXQ1nFM85_7e200Jp)
- [`slide` SparkUI Visualization](http://www.slideshare.net/databricks/spark-summit-eu-2015-sparkui-visualization-a-lens-into-your-application)

- [
Everyday I'm Shuffling - Tips for Writing Better Spark Programs, Strata San Jose 2015](https://www.youtube.com/watch?v=Wg2boMqLjCg)
- [ `slide` Everyday I'm Shuffling - Tips for Writing Better Spark Programs, Strata San Jose 2015](http://www.slideshare.net/databricks/strata-sj-everyday-im-shuffling-tips-for-writing-better-spark-programs)

- [Large Scale Distributed Machine Learning on Apache Spark](https://www.youtube.com/watch?v=FA3ArTyXNoo)

- [Securing your Spark Applications](https://www.youtube.com/watch?v=Aups6UcGiQQ&list=PL-x35fyliRwif48cPXQ1nFM85_7e200Jp&index=1)
- [`slide` Securing your Spark Applications](http://www.slideshare.net/cloudera/securing-your-apache-spark-applications)


- [Building a REST Job Server for Interactive Spark as a Service](https://www.youtube.com/watch?v=AHYq91i-ohI)
- [`slide` Building a REST Job Server for Interactive Spark as a Service](http://www.slideshare.net/SparkSummit/building-a-rest-job-server-for-interactive-spark-as-a-service-by-romain-rigaux-and-erick-tryzelaar)


- [Exploiting GPUs for Columnar DataFrame Operations](https://www.youtube.com/watch?v=PPQRi484bNo&list=PL-x35fyliRwif48cPXQ1nFM85_7e200Jp&index=2)
- [`slide` Exploiting GPUs for Columnar DataFrame Operations](http://www.slideshare.net/SparkSummit/exploiting-gpus-for-columnar-datafrrames-by-kiran-lonikar)


- [Easy JSON Data Manipulation in Spark - Yin Huai (Databricks)](https://www.youtube.com/watch?v=MFSUAkDBSdQ)
- [`slide` Easy JSON Data Manipulation in Spark - Yin Huai (Databricks)](https://spark-summit.org/2014/wp-content/uploads/2014/07/Easy-json-Data-Manipulation-Yin-Huai.pdf)


- [Sparkling: Speculative Partition of Data for Spark Applications - Peilong Li](https://www.youtube.com/watch?v=8hn2KVC8FvA&index=6&list=PL-x35fyliRwiuc6qy9z2erka2VX8LY53x)
- [`slide` Sparkling: Speculative Partition of Data for Spark Applications - Peilong Li](https://spark-summit.org/2014/wp-content/uploads/2014/07/Sparkling-Indentification-of-Task-Skew-and-Speculative-Partition-of-Data-for-Spark-Applications-Peilong-Li.pdf)

- [Advanced Spark Internals and Tuning – Reynold Xin](https://www.youtube.com/watch?v=HG2Yd-3r4-M&list=PLTPXxbhUt-YWGNTaDj6HSjnHMxiTD1HCR&index=1)
- [`slide` Advanced Spark Internals and Tuning – Reynold Xin](https://databricks-training.s3.amazonaws.com/slides/advanced-spark-training.pdf)

- [The Future of Real Time in Spark](https://www.youtube.com/watch?v=oXkxXDG0gNk)
- [`slide` The Future of Real Time in Spark](http://www.slideshare.net/databricks/the-future-of-realtime-in-spark-58433411)

- [Spark 2 0](https://www.youtube.com/watch?v=ZFBgY0PwUeY&feature=youtu.be)
- [`slide` Spark 2 0](http://www.slideshare.net/databricks/2016-spark-summit-east-keynote-matei-zaharia)

- [Democratizing Access to Data](https://www.youtube.com/watch?v=BPotQuqFnyw&feature=youtu.be)
- [`slide` Democratizing Access to Data](http://www.slideshare.net/databricks/2016-spark-summit-east-keynote-ali-ghodsi-and-databricks-community-edition-demo)

- [Not Your Father's Database: How to Use Apache Spark Properly in Your Big Data Architecture](https://www.youtube.com/watch?v=l2YHIUucXOg&feature=youtu.be)
- [`slide` Not Your Father's Database: How to Use Apache Spark Properly in Your Big Data Architecture](http://www.slideshare.net/SparkSummit/not-your-fathers-database-by-vida-ha)

- [Disrupting Big Data with Apache Spark in the Cloud](https://www.youtube.com/watch?v=vob_kn10aNU)
- [`slide` Disrupting Big Data with Apache Spark in the Cloud](http://www.slideshare.net/JenAman/distributing-big-data-with-apache-spark-in-the-cloud)

>>
我一直很欣赏 databricks 出的 video 和 slide，结构非常清晰，这个是其中一个非常好的演讲，里面有很多值得借鉴的地方，特别是当你像别人介绍你的工作，产品的时候。[我有一个感受，很少有人能清晰，有条理的介绍自己正在做的产品，对于一些小众的产品，甚至一些职业的销售也难以做到清晰，简明的叙述。这个 video 和 slide 有很大的参考价值。我自己感觉仔细研究这些 video 和 slide 有时候比看上一两本专业讲销售的书还要管用。]

- [Getting The Best Performance With PySpark](https://www.youtube.com/watch?v=V6DkTVvy9vk)
- [`slide` Getting The Best Performance With PySpark](http://www.slideshare.net/hkarau/getting-the-best-performance-with-pyspark-spark-summit-west-2016)

- [Disrupting Big Data with Apache Spark in the Cloud](https://www.youtube.com/watch?v=4uw_obRH5eM)
- [`slide` Disrupting Big Data with Apache Spark in the Cloud](http://www.slideshare.net/JenAman/distributing-big-data-with-apache-spark-in-the-cloud)

- [Large Scale Deep Learning with TensorFlow](https://www.youtube.com/watch?v=XYwIDn00PAo)
- [`slide` Large Scale Deep Learning with TensorFlow](http://www.slideshare.net/JenAman/large-scale-deep-learning-with-tensorflow)

- [700 Queries Per Second with Updates: Spark As A Real-Time Web Service](https://sparkhub.databricks.com/video/700-queries-per-second-with-updates-spark-as-a-real-time-web-service/)
- [`slide` 700 Queries Per Second with Updates: Spark As A Real-Time Web Service](http://www.slideshare.net/SparkSummit/700-queries-per-second-with-updates-spark-as-a-realtime-web-service)
- [`blog` 700 SQL Queries per Second in Apache Spark with FiloDB](http://velvia.github.io/Spark-Concurrent-Fast-Queries/)
- [Operational Tips for Deploying Spark]()
- [`slide` Operational Tips for Deploying Spark](http://www.slideshare.net/SparkSummit/operational-tips-for-deploying-spark-by-miklos-christine)

- [Connecting Python To The Spark Ecosystem]()
- [`slide` Connecting Python To The Spark Ecosystem](http://www.slideshare.net/SparkSummit/connecting-python-to-the-spark-ecosystem)

- [Livy: A REST Web Service For Apache Spark](https://www.youtube.com/watch?v=C_3iEf_KNv8&feature=youtu.be)
- [`slide` Livy: A REST Web Service For Apache Spark](http://www.slideshare.net/JenAman/livy-a-rest-web-service-for-apache-spark)

- [Understanding Memory Management In Spark For Fun And Profit]()
- [`slide` Understanding Memory Management In Spark For Fun And Profit](http://www.slideshare.net/SparkSummit/understanding-memory-management-in-spark-for-fun-and-profit)

- [Deep Dive: Memory Management in Apache Spark]()
- [`slide` Deep Dive: Memory Management in Apache Spark](http://www.slideshare.net/databricks/deep-dive-memory-management-in-apache-spark)


- [High Performance Python on Apache Spark]()
- [`slide` High Performance Python on Apache Spark](http://www.slideshare.net/wesm/high-performance-python-on-apache-spark)

- [A Deep Dive into Structured Streaming]()
- [`slide` A Deep Dive into Structured Streaming](http://www.slideshare.net/databricks/a-deep-dive-into-structured-streaming)

- [`slide` Spark Job Server and Spark as a Query Engine (Spark Meetup 5/14)](http://www.slideshare.net/EvanChan2/spark-job-server-and-spark-as-a-query-engine-spark-meetup-514)

- [Apache spark job server example with installation](https://www.youtube.com/watch?v=JKKqAgNkHZk)

- [Productionizing Spark and the Spark REST Job Server](https://www.youtube.com/watch?v=kQGS_6TxfTk)
- [ `slide` Productionizing Spark and the Spark REST Job Server](http://www.slideshare.net/SparkSummit/productionizing-spark-and-the-rest-job-server-evan-chan)

- [Data Profiling and Pipeline Processing with Spark](https://youtu.be/r7SF5WldITk)
- [`slide` Data Profiling and Pipeline Processing with Spark](http://www.slideshare.net/SparkSummit/spark-summit-keynote-by-suren-nathan)

- [Spark at Bloomberg: Dynamically Composable Analytics](https://www.youtube.com/watch?v=iMaFRSseeNk&feature=youtu.be)
- [`slide` Spark at Bloomberg: Dynamically Composable Analytics](http://www.slideshare.net/JenAman/spark-at-bloomberg-dynamically-composable-analytics)

- [Data Storage Tips for Optimal Spark Performance - Vida Ha (Databricks)](https://www.youtube.com/watch?v=XMVyNJz4FzM&index=16&list=PL-x35fyliRwhP52fwDqULJLOnqnrN5nDs)
- [`slide` Data Storage Tips for Optimal Spark Performance-(Vida Ha, Databricks)](http://www.slideshare.net/SparkSummit/data-storage-tips-for-optimal-spark-performancevida-ha-databricks)


## 6. next

上面的资源我都会不断更新的，里面 80% 以上的都是我亲自看过并且觉得有价值的，可不是胡乱收集一通的，推荐欣赏哦。


## 7. 打开微信，扫一扫，点一点，棒棒的，^_^

![wechat_pay.png](../images/wechat_pay.png)



## 本系列文章链接

- [『 Spark 』1. spark 简介 ](http://litaotao.github.io/introduction-to-spark?s=inner)
- [『 Spark 』2. spark 基本概念解析 ](http://litaotao.github.io/spark-questions-concepts?s=inner)
- [『 Spark 』3. spark 编程模式 ](http://litaotao.github.io/spark-programming-model?s=inner)
- [『 Spark 』4. spark 之 RDD ](http://litaotao.github.io/spark-what-is-rdd?s=inner)
- [『 Spark 』5. 这些年，你不能错过的 spark 学习资源 ](http://litaotao.github.io/spark-resouces-blogs-paper?s=inner)
- [『 Spark 』6. 深入研究 spark 运行原理之 job, stage, task](http://litaotao.github.io/deep-into-spark-exection-model?s=inner)
- [『 Spark 』7. 使用 Spark DataFrame 进行大数据分析](http://litaotao.github.io/spark-dataframe-introduction?s=inner)
- [『 Spark 』8. 实战案例 ｜ Spark 在金融领域的应用 ｜ 日内走势预测](http://litaotao.github.io/spark-in-finance-and-investing?s=inner)
- [『 Spark 』9. 搭建 IPython + Notebook + Spark 开发环境](http://litaotao.github.io/ipython-notebook-spark?s=inner)
- [『 Spark 』10. spark 应用程序性能优化｜12 个优化方法](http://litaotao.github.io/boost-spark-application-performance?s=inner)
- [『 Spark 』11. spark 机器学习](http://litaotao.github.io/spark-mlib-machine-learning?s=inner)
- [『 Spark 』12. Spark 2.0 特性介绍](http://litaotao.github.io/spark-2.0-faster-easier-smarter?s=inner)
- [『 Spark 』13. Spark 2.0 Release Notes 中文版 ](http://litaotao.github.io/spark-2.0-release-notes-zh?s=inner)
- [『 Spark 』14. 一次 Spark SQL 性能优化之旅](http://litaotao.github.io/spark-sql-parquet-optimize?s=inner)