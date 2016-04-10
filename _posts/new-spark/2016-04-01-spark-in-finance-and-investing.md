---
layout: post
published: false
title: 『 Spark 』8. 实战案例 ｜ Spark 在金融领域的应用 ｜ 相似度计算
description: know more, do better 
---  

## 写在前面

本系列是综合了自己在学习spark过程中的理解记录 ＋ 对参考文章中的一些理解 ＋ 个人实践spark过程中的一些心得而来。写这样一个系列仅仅是为了梳理个人学习spark的笔记记录，并非为了做什么教程，所以一切以个人理解梳理为主，没有必要的细节就不会记录了。若想深入了解，最好阅读参考文章和官方文档。

其次，本系列是基于目前最新的 spark 1.6.0 系列开始的，spark 目前的更新速度很快，记录一下版本好还是必要的。   
最后，如果各位觉得内容有误，欢迎留言备注，所有留言 24 小时内必定回复，非常感谢。     
Tips: 如果插图看起来不明显，可以：1. 放大网页；2. 新标签中打开图片，查看原图哦。


## 1. 同花顺收费版之走势预测

2014年后半年开始，国内 A 股市场可谓是热火朝天啊，路上的人谈的都是股票。小弟虽然就职金融互联网公司，但之前从来没有买过股票，但每天听着别人又赚了几套房几辆车，那叫一个心痒痒啊，那感觉，就跟一个出浴美女和你共处一室，但你却要死忍住不去掀开浴巾一样。终于，小弟还是"犯了全天下男人都会犯的错误"，还是在 2015.03.19 那天入市了，还记得自己的第一次是献给了一支叫 `天建集团` 的股票，好像当天还赚了一两百块吧，当时心情那叫一个激动，下班了第一时间就打电话给娘亲了。

哦，似乎有点扯得远了。言归正传，当时自己为了投资更方便，就花了将近 300 大洋买了同花顺的 level 2 版，里面有个功能，叫做形态预测。具体就是，根据所有股票的历史行情，看看当前股票的未来一段时间的走势分布。下面是一个截图：

![spark-in-finance-1.jpg](../images/spark-in-finance-1.jpg)

截图说明：颜色越深，概率越大，包括一组预测的 k 线走势。就像上面说的，上面的那支股票的预测结果是：未来3周收益大于 4.0% 的概率有 60%。amazing...

先不说这个预测准确度有多高，但首先这个思路不错，至少可以作为一个信号吧［当然一个稳健的投资策略肯定不能仅仅依赖于一个信号］


## 2. 形态选股

同花顺这个功能，其实也挺实用的，因为本身在股票市场技术指标这个分类下面，就有形态选股这样一种指标。比如说，经常听财经频道主持人说的 [三阳开泰](http://baike.baidu.com/item/%E4%B8%89%E9%98%B3%E5%BC%80%E6%B3%B0/18751451)，[圆弧底](http://baike.baidu.com/view/1302521.htm) 什么的。

## 3. 指数日内相似度

今天，我们就来尝试一下，通过指数日内走势来进行宏观择时：分别在 10:00, 10:30, 11:00, 11:30 四个时间节点进行预测，看看当天日内走势预测情况。

原理如下：



## 4. spark 实现指数日内相似度



## 6. Next

这个例子还算 ok 吧，可是我每天都应用的投资策略的一部分啊，已经下血本了，各位还不打赏打赏吗？一转眼 spark 已经快要有十篇 blog 了，期间也写了一些 spark 的应用程序，读了一些高质量的书和博文，在 youtube 上也看了一些高质量的技术分享。也总结了一些写 spark 应用程序的时候的细节问题，下一篇就列一下这些细节问题，希望能优化，加速各位的 spark 应用程序。

## 7. 打开微信，扫一扫，点一点，棒棒的，^_^

![wechat_pay_6-6.png](../images/wechat_pay_6-6.png)


## 参考文章

- [Spark SQL, DataFrames and Datasets Guide](http://spark.apache.org/docs/latest/sql-programming-guide.html#dataframes)
- [Introducing DataFrames in Spark for Large Scale Data Science](https://databricks.com/blog/2015/02/17/introducing-dataframes-in-spark-for-large-scale-data-science.html)
- [From Webinar Apache Spark 1.5: What is the difference between a DataFrame and a RDD?](https://forums.databricks.com/questions/7257/from-webinar-spark-dataframes-what-is-the-differen-1.html)
- [用Apache Spark进行大数据处理——第二部分：Spark SQL](http://www.infoq.com/cn/articles/apache-spark-sql)
- [An introduction to JSON support in Spark SQL](https://databricks.com/blog/2015/02/02/an-introduction-to-json-support-in-spark-sql.html)
- [Spark新年福音：一个用于大规模数据科学的API——DataFrame](http://www.csdn.net/article/2015-02-18/2823997)
- [An introduction to JSON support in Spark SQL](https://databricks.com/blog/2015/02/02/an-introduction-to-json-support-in-spark-sql.html)


## 本系列文章链接

- [『 Spark 』1. spark 简介 ](../introduction-to-spark)
- [『 Spark 』2. spark 基本概念解析 ](../spark-questions-concepts)
- [『 Spark 』3. spark 编程模式 ](../spark-programming-model)
- [『 Spark 』4. spark 之 RDD ](../spark-what-is-rdd)
- [『 Spark 』5. 这些年，你不能错过的 spark 学习资源 ](../spark-resouces-blogs-paper)
- [『 Spark 』6. 深入研究 spark 运行原理之 job, stage, task](../deep-into-spark-exection-model)
- [『 Spark 』7. 使用 Spark DataFrame 进行大数据分析](../spark-dataframe-introduction)
