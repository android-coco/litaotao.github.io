---
category: books
published: false
layout: post
title: spark专刊笔记之：spark运行原理解析
description: 仅仅是记录我个人的读书记录，看官不必在意～
---

## 
## 1. spark运行原理解析
　　目前在大数据计算这个业务范畴内，国内应用较为广泛的是hadoop mapreduce，在yarn出现之前，它属于整个hadoop生态系统的核心。hadoop mapreduce将数据处理过程简化为map和reduce两个阶段，适合大数据离线计算这一业务场景，但由于其调度开销大，中间数据写磁盘（shuffle阶段）导致运行速度慢等缺点，对于实时计算，数据挖掘等场景却不适合。

### 1.1 部署模式
　　不同部署模式都基于一个相似的工作流程，不同运行模式的主要区别就是他们有自己特定的资源分配和任务调度模块，用来执行实际的计算任务。

- spark standalone：需要部署spark到相关节点，包括master和worker；
- yarn-cluster：driver和executor都运行在yarn集群中；
- yarn-client：driver在本地，executor运行在yarn集群中；

### 1.2 spark基本工作流程
　　spark的application在运行的时候，首先在driver程序中创建sparkcontext作为调度的总入口，在其初始化中会分布创建DAGScheduler运行stage调度和TaskScheduler进行task调度两个模块。DAGScheduler模块是基于stage的调度模块，它为每个spark job计算具有依赖关系的多个stage任务阶段，然后将每个stage划分为具体的每一组任务（通常会考虑数据的本地性等）以taskset的形式提交给底层的taskscheduler模块来具体执行。taskscheduler负责具体启动任务，监控和汇报任务运行情况。而任务运行所需要的资源需要向cluster manager申请。
　　spark-submit的参数详细参考pdf的P13。
　　任务运行结束后，如果启动了spark的historyserver服务，则会在historyserver中记录相关的任务运行信息。这一点类似于mapreduce的jobhistoryserver。historyserver的相关属性可以通过$SPARKHOME/conf下的spark-defaults.conf文件来设定。启动historyserver可以通过$SPARKHOME/sbin下用start-history-server.sh脚本来启动。

### 1.3 standalone模式
　　spark standalone是master-slave架构的集群模式，和大部分的master-slave结构集群类似，都存在master单点问题。目前spark提供两种方式解决这个问题。一种是基于文件系统的故障恢复模式，这种方法适合当master进程down掉之后直接重启；另一种是基于zookeeper的HA方式，类似于HDFS的namenode的HA方案，active master挂掉后，standby master会立即切换过去继续对外提供服务，同时这种基于zookeeper的HA方案也被很多分布式框架采用。

### 1.4 部署及程序运行
　　详细见P18.

### 1.5 内部实现原理
　　即使是在standalone模式下，driver的运行位置也有所不同。如果使用spark-shell等方式交互运行spark任务或直接使用run-example来运行spark官方提示的示例的话，driver是运行在master节点上的；如果使用spark-submit工具进行任务的提交或者在Eclipse，IDEA等开发平台进行开发时使用“new SparkContext("spark://master:7077", "AppName")”方式运行spark任务的话，driver是运行在本地客户端的。
　　spark-submit方式来提交任务说明standalone运行原理，详见P24.

