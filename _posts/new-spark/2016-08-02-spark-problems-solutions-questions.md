---
layout: post
published: false
title: 『 Spark 』Spark 实践过程中遇到过的那些问题
description: 再不记下来真的就忘掉了
---  


## 写在前面

本系列是综合了自己在学习spark过程中的理解记录 ＋ 对参考文章中的一些理解 ＋ 个人实践spark过程中的一些心得而来。写这样一个系列仅仅是为了梳理个人学习spark的笔记记录，所以一切以能够理解为主，没有必要的细节就不会记录了，而且文中有时候会出现英文原版文档，只要不影响理解，都不翻译了。若想深入了解，最好阅读参考文章和官方文档。

其次，本系列是基于目前最新的 spark 1.6.0 系列开始的，spark 目前的更新速度很快，记录一下版本号还是必要的。   
最后，如果各位觉得内容有误，欢迎留言备注，所有留言 24 小时内必定回复，非常感谢。

Tips: 如果插图看起来不明显，可以：1. 放大网页；2. 新标签中打开图片，查看原图哦；3. 点击右边目录上方的 *present mode* 哦。

## 1. 网络联通

Driver, Master, Worker 之间一定要互相都能连通。driver 最好不要用虚拟机，会出各种问题。


## 2. bad substitution

![bad_substitution_1.jpg](../images/bad_substitution_1.jpg)
![bad_substitution_2.jpg](../images/bad_substitution_2.jpg)

https://community.hortonworks.com/questions/23699/bad-substitution-error-running-spark-on-yarn.html

## 3. Too many open files

>>

16/09/05 23:26:56 WARN scheduler.TaskSetManager: Lost task 20.0 in stage 188.0 (TID 28165, dn04.wmcloud-stg.com): java.io.FileNotFoundException: /tmp/hadoop/yarn/local/usercache/hdfs/appcache/application_1469778541624_0119/blockmgr-194e6761-1597-45b8-86a0-429b75309dad/34/temp_shuffle_c691ac43-df11-4815-863c-0f6cf581fbdd (Too many open files)

这类情况是在 rdd 数据量特别大，且有 shuffle 需求的时候容易出现的，原因是 shuffle 的时候需要创建一些临时文件，原始数据集比较大的话会需要创建很多临时文件。这是一个系统配置项，解决办法网上已经有很多了：[Why does Spark job fail with “too many open files”?](http://stackoverflow.com/questions/25707629/why-does-spark-job-fail-with-too-many-open-files)，[Spark 常规故障处理: Too many open files](https://zybuluo.com/yanbo-ai/note/43455)


## 4. SQLContext does not exist in the JVM

这个和我自身的应用有比较大的关系，可能大家不太可能遇到。应用是这样子的：一个基于 flask 的 python web app，在启动的时候会初始化一个 spark context，然后有一些请求会用到这个 spark context。采用 uwsgi 来部署，其中部署了一个 master，10 个 worker，设置弱请求超过 30 秒，则 kill 掉这个请求。

然后问题出现了：有的请求，会涉及到 spark context，然后请求完成的时间会比较长，此时 uwsgi 会 kill 掉正在执行这个请求的 worker，然后会自动重启这个 worker，但重启的时候不会再去初始化一个 spark context。接下来，当有请求还需要 spark context 的时候，则会抱这样的错误。





## 13. Next

最近 databricks 出了一篇非常不错的文章，讲 spark 的一些概念的，个人觉得非常不错，下一篇就翻译这篇文章吧。届时大家可以结合起第二篇文章一起理解：[『 Spark 』2. spark 基本概念解析 ](http://litaotao.github.io/spark-questions-concepts?s=inner)


## 14. 打开微信，扫一扫，点一点，棒棒的，^_^

![wechat_pay_6-6.png](../images/wechat_pay_6-6.png)


## 参考文章



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