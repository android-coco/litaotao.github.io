---
layout: post
published: false
title: ［touch spark］*. IPython SQL magic
description: 在IPython中直接运行sql语句，实在是太方便了。
---  


## 
## 1. 写在前面
　　在Databricks，Zeppelin中，都可以使用%sql magic来实现sql语句的运行，不过他们都有一个大前提，就是再之前已经有生成SchemaRDD并且注册为table了。所以，他们的sql语句都是针对于Spark的RDD的，如果也能支持本地、远程数据库的CURD，岂不完美了。
　　本文就是我初步学习如何在IPython中通过一个ipython-sql的扩展包，使IPython支持本地、远程数据库的CURD。本文的目标如下：

- 安装使用ipython-sql包；
- 研究IPython extension原理；
- 修改ipython-sql包；

## 2. 安装、使用ipython-sql包
　　关于ipython-sql的介绍在[https://github.com/catherinedevlin/ipython-sql](https://github.com/catherinedevlin/ipython-sql)
　　安装ipython-sql：

```
root@ubuntu2[15:26:48]:~/Desktop/ipython-notebook-spark#pip install ipython-sql
```

　　使用ipython-sql

![ipython-sql.jpg](../images/ipython-sql.jpg)

　　一切看起来不错，小白秒秒钟上手，but，一件事，要做成很简单，要做好却很难。这里如果想要真正用好这个扩展包的话，我需要深入了解下面几个问题：

- 为何我本地没有安装任何SQL数据库，语句也能执行成功；正如截图里所示，我连接到一个None@None的数据库，what's the hell is that????
- 这个ipython-sql包的结构【本来想说架构的，但总觉得架构这词太heavy了】和运作原理；
- 这个ipython-sql支持哪些数据库，if possible and needed，也许可以写一个支持其他数据库的extension；
- 所以，也需要了解IPython里extension的原理；

　　介于以上几个问题，下面我想从两个方面来好好学习一下：IPython extension原理；ipython-sql包结构和原理。

## 3. Deep Into IPython Extension




## 扫一扫     

![2015-03-25-ipython-sql.md](../../images/share/2015-03-25-ipython-sql.md.jpg)