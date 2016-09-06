---
category: spark
published: false
layout: post
title: ［touch spark］1. 准备和初次体验spark
description: 总结了spark下载，安装，设置环境变量，以及如何运行python写的spark应用的一些基本点～～～	
---  

##  
## 1. 下载，安装，运行spark  

　　下载最新版的[spark](http://spark.apache.org/downloads.html). 我选择的是spark-1.1.1-bin-hadoop2.4.tgz。因为是预编译过的，所以没有所谓的“安装”环境，直接解压即可运行了。  
　　运行路径是：spark-1.1.1-bin-hadoop2.4/bin，如下： 

```
chenshan@mac007 spark$ls
spark-1.1.1-bin-hadoop2.4.tgz
chenshan@mac007 spark$tar zxf spark-1.1.1-bin-hadoop2.4.tgz 
chenshan@mac007 spark$ls
chenshan@mac007 spark$cd spark-1.1.1-bin-hadoop2.4
chenshan@mac007 spark-1.1.1-bin-hadoop2.4$ls
CHANGES.txt NOTICE      RELEASE     conf        examples    python
LICENSE     README.md   bin         ec2         lib         sbin
chenshan@mac007 spark-1.1.1-bin-hadoop2.4$cd bin
chenshan@mac007 bin$ls
beeline               pyspark               run-example.cmd       spark-class2.cmd      spark-submit
compute-classpath.cmd pyspark.cmd           run-example2.cmd      spark-shell           spark-submit.cmd
compute-classpath.sh  pyspark2.cmd          spark-class           spark-shell.cmd       utils.sh
load-spark-env.sh     run-example           spark-class.cmd       spark-sql
chenshan@mac007 bin$./pyspark 

```  

## 2. 设置环境变量  
　　为了方便以后使用，最好把bin文件夹加入环境变量，关于环境变量的设置可以参考[这里](http://www.tuicool.com/articles/7nu2E3R)。编辑～/.bash_profile，在最后加上一句：export PATH=~/Desktop/spark/spark-1.1.1-bin-hadoop2.4/bin:$PATH，保存文件后退出，在执行 source ～/.bash_profile 或 . ～/.bash_profile 即可生效。  
　　ok，现在可以随时随地在任何路径下执行pyspark启动spark了。因为默认是用python的console来启动的，这样也可以用，但在python console里编码多多少少有很多不便，对我个人而言就是一些ls/cd啊这些常用命令，以及查看每个对象但方法和属性和自动补全了。所以这里如果可以在ipython里启动spark的话不就完美了。先google了下，没什么结果。那就来看看pyspark这个脚本里是怎么写的吧，果不其然，在最后几行还真找到东西了：  

```
  if [[ "$IPYTHON" = "1" ]]; then
    exec ipython $IPYTHON_OPTS
  else
    exec "$PYSPARK_PYTHON"
  fi
```  

　　好，神秘钥匙找到了，看来我们需要设置一个IPYTHON的变量，且把该变量设置成1。ok，试一下:  

```  
chenshan@mac007 bin$$IPTYHON
chenshan@mac007 bin$export IPYTHON="1"
chenshan@mac007 bin$$IPTYHON
-bash: 1: command not found
chenshan@mac007 bin$pyspark 
Python 2.7.5 (default, Mar  9 2014, 22:15:05) 
Type "copyright", "credits" or "license" for more information.

IPython 2.1.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.
```  

　　成功，我想要的效果达到了，看下面。后来才发现原来官方上面已经有这个说明了，只是感觉也说得不是很明确，看[这里](http://spark.apache.org/docs/latest/programming-guide.html)  

```
In [1]: ls
README.md

In [2]: t = sc.textFile("R
README.md       ReferenceError  RuntimeError    RuntimeWarning  

In [2]: t = sc.textFile("README.md")
14/11/30 12:48:12 INFO MemoryStore: ensureFreeSpace(172851) called with curMem=0, maxMem=286300569
14/11/30 12:48:12 INFO MemoryStore: Block broadcast_0 stored as values in memory (estimated size 168.8 KB, free 272.9 MB)

In [3]: t.
t.aggregate                  t.foreachPartition           t.max                        t.setName
t.aggregateByKey             t.getCheckpointFile          t.mean                       t.sortBy
t.cache                      t.getNumPartitions           t.min                        t.sortByKey
t.cartesian                  t.getStorageLevel            t.name                       t.stats

```  
	
## 3. 单机版的spark应用  
　　官方的[quick start](http://spark.apache.org/docs/latest/quick-start.html)里已经有了一个单机版的spark应用的示例。很简单的例子，但我觉得还是有一个地方需要理解下才行。那就是运行python写但spark应用但方法，需要使用spark安装目录里bin可执行文件目录下但spark-submit来运行。我第一次运行这个示例的时候，很不知所谓地就python SimpleApp.py，然后自然而然地提示我没有pyspark这个包，我心想，没有这个包还不好办吗，直接pip install pyspark，可pip居然提示也没有这个包。我想难道是pip抽风了，那好，我就google下pyspark，按理说第一项应该就是pyspark在pip的网页了，我靠，可连google也没搜出什么东西来啊。这下我觉得应该是我的问题了。想了下，先启动pyspark来看看有没有这个包，居然是有的，这？执行pyspark.__file__来看看这个包的路径，我才恍然大悟。原来是我短路了，spark官方都说了，人家自己提供了scala，java，python都接口，全部都在源码里了，还提供了一些基于这三种语言都examples。只是这个包没有放到pip里去，而是随spark一起发布的。我想是因为spark现在还不够成熟，基于python的接口也会跟着每一个小版本的spark发布而改变，所以暂时没把pyspark发布到pip上去吧。  
　　所以，这里值得注意的是，一定要用spark-submit来运行python写的spark应用。  

```   
In [13]: import pyspark

In [14]: pyspark.__file__
Out[14]: '/Users/chenshan/Desktop/spark/spark-1.1.1-bin-hadoop2.4/python/pyspark/__init__.pyc'
```



　　

## 扫一扫     

![2014-11-30-learning-spark-step-1.md](../../images/share/2014-11-30-learning-spark-step-1.md.jpg)