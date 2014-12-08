---
category: spark
published: true
layout: post
title: ［touch spark］3. Amazon AWS 使用攻略
description: 准备在AWS上跑spark的看过来了~~~
---  

##  
## 1. 申请Amazon AWS账号   
　　申请Amazon AWS需要绑定信用卡，无奈兄弟我从来没用过信用卡，所以只能跑到[global cash](https://www.globalcash.hk/)申请一张虚拟信用卡了。有关申请虚拟信用卡的教程[这里](http://www.freehao123.com/globalcash/)已经有了，我就不重复了。

## 2. 在EC2上创建一个spark集群  
### 2.1 前期准备  
　　本文中用到的所有脚本都是基于python 2.x写的，且在Linux和0S X上测试通过。  

### 2.2 创建EC2 keys  
　　首先确保你的地区是US EAST，在右上角可以选择区域，即帐号名右侧。还没找到的请看下图：  
![choose ec2 region](../../images/choose ec2 region.jpg)  

　　然后在帐号名->Security Credentials->Dashboard 下的 Details->Security Status->Manage Security Credentials->Access Keys->Create New Access Key创建keys，这里最好把keys记录下来，以后好用。  
　　设置变量，下面的KEY_ID, ACCESS_KEY是在你创建keys的时候产生的：

```  
export AWS_ACCESS_KEY_ID=<ACCESS_KEY_ID>
export AWS_SECRET_ACCESS_KEY=<SECRET_ACCESS_KEY>
```  


### 2.3 创建key pair  
　　在EC2 Dashboard左侧边栏->Network & Security->Key Pairs->Create Key Pair。这里会需要你输入一个key pair name，最好搞一个简单好记的，因为以后也会用到。创建成功后会自动下载一个用于后期验证登录的文件，下载该文件把其复制到用户家目录下，确保其权限至少是600，保险起见执行 chmod 600 key_pair_file。  

### 2.4 下载启动脚本  
```  
git clone git://github.com/amplab/ampcamp.git  
```  

### 2.5 建立并启动集群  
　　若上面的启动脚本下载成功后，本地会有一个ampcamp的文件夹，cd 到ampcamp文件夹里，执行下面命令启动集群。其中key_file是刚刚下载并复制到家目录下的验证文件，name_of_key_pair是你创建key_pair的时候自己命名的。  

``` 
./spark-ec2 -i <key_file> -k <name_of_key_pair> --copy launch ampcamp
``` 

　　上面这个过程大约会持续15-20分钟，耐心等待一下。如果期间出现下面这个问题，那是因为没有把key_pair文件复制到家目录下去。

```
rsync: connection unexpectedly closed (0 bytes received so far) [sender]
rsync error: unexplained error (code 255) at io.c(605) [sender=3.0.9]
Traceback (most recent call last):
  File "./spark_ec2.py", line 759, in <module>
    main()
  File "./spark_ec2.py", line 648, in main
    setup_cluster(conn, master_nodes, slave_nodes, zoo_nodes, opts, True)
  File "./spark_ec2.py", line 363, in setup_cluster
    deploy_files(conn, "deploy.generic", opts, master_nodes, slave_nodes, zoo_nodes)
  File "./spark_ec2.py", line 604, in deploy_files
    subprocess.check_call(command, shell=True)
  File "/root/anaconda/lib/python2.7/subprocess.py", line 540, in check_call
    raise CalledProcessError(retcode, cmd)
subprocess.CalledProcessError: Command 'rsync -rv -e 'ssh -o StrictHostKeyChecking=no -i ../company.pem' '/tmp/tmp6YpLzV/' 'root@ec2-54-172-219-206.compute-1.amazonaws.com:/'' returned non-zero exit status 255
root@ubuntu2:~/Desktop/spark/ampcamp# cp ../company.pem .
```  

　　如果一切顺利（但愿），最后会有消息提示创建成功：SUCCESS: Cluster successfully launched! You can login to the master at ***


### 2.6 其他相关命令    
　　第一个命令获取ampcamp集群的master节点，这个需要在集群启动成功后执行一次，因为后续也要用到这个节点地址，所以最好把master 节点地址记录下来。第二个命令是删除集群。    

```  
./spark-ec2 -i <key_file> -k <key_pair> get-master ampcamp   
./spark-ec2 -i <key_file> -k <key_pair> destroy ampcamp  
```  

## 3. 查看集群设置和数据准备

### 3.1 获取master节点地址  
　　在这个练习中，我们会用从[http://aws.amazon.com/datasets/4182](http://aws.amazon.com/datasets/4182)拿到的wikipedia的流量数据来做分析。  
　　方便起见，AMP Camp已经提前把(May 5 to May 7, 2009; roughly 20G and 329 million entries)的数据准备好，并且预加载到集群里一个HDFS机器上了。这样我们就不用准备数据了，可以专注在体验spark特性的这件事上。

### 3.1 获取master节点地址  

```  
./spark-ec2 -i <key_file> -k <key_pair> get-master ampcamp  
```  

　　此时成功的话应该会提示你当前有一个master，3个slave，0个ZooKeeper。  

### 3.2 使用ssh登录master节点  

```  
ssh -i <key_file> -l root <master_node_hostname>
or
ssh -i <key_file> root <master_node_hostname>
```  
　　需要注意的是，这里虽然你是登录到一个机器上，但实际是一个集群中。集群里有一个master节点，3个slave节点。其中你登录的地方是master节点，master节点主要负责任务分配和管理HDFS的元数据。其他的3个slave节点是计算节点，也就是真正运行任务的节点。  
　　在master里，执行ls可以看到以下几个文件夹，下面列出比较重要的几个文件夹：  

- ephemeral-hdfs: Hadoop installation  
- hive: Hive installation  
- java-app-template: Some stand-alone Spark programs in java  
- mesos: Mesos installation  
- mesos-ec2: A suite of scripts to manage Mesos on EC2  
- scala-2.9.1.final: Scala installation  
- scala-app-template: Some stand-alone Spark programs in scala  
- spark: Spark installation  
- shark: Shark installation  

　　可以在mesos-ec2/slaves文件里看到自己的3个slave节点地址：  

```
[root@ip-172-31-22-240 ~]# cat mesos-ec2/slaves
ec2-54-174-175-127.compute-1.amazonaws.com
ec2-54-174-183-88.compute-1.amazonaws.com
ec2-54-174-124-52.compute-1.amazonaws.com
```
　　
　　你的HDFS集群应该已经提前载入20GB的wikipedia数据文件了，可以到ephemeral-hdfs/bin/下执行hadoop fs -ls /wiki/pagecounts查看，这里应该是有74个文件，其中2个是空的。其中每一个文件是以小时为单位来保存的。  

```  
[root@ip-172-31-22-240 ~]# ephemeral-hdfs/bin/hadoop fs -ls /wiki/pagecounts
Found 74 items
-rw-r--r--   3 root supergroup          0 2014-12-03 02:18 /wiki/pagecounts/part-00095
-rw-r--r--   3 root supergroup  244236879 2014-12-03 02:18 /wiki/pagecounts/part-00096
-rw-r--r--   3 root supergroup  233905016 2014-12-03 02:18 /wiki/pagecounts/part-00097
-rw-r--r--   3 root supergroup  225825888 2014-12-03 02:19 /wiki/pagecounts/part-00098
-rw-r--r--   3 root supergroup  225164279 2014-12-03 02:18 /wiki/pagecounts/part-00099
-rw-r--r--   3 root supergroup  228145848 2014-12-03 02:19 /wiki/pagecounts/part-00100
.            
.
.
-rw-r--r--   3 root supergroup  327382691 2014-12-03 02:26 /wiki/pagecounts/part-00163
-rw-r--r--   3 root supergroup  325471268 2014-12-03 02:27 /wiki/pagecounts/part-00164
-rw-r--r--   3 root supergroup  288288841 2014-12-03 02:27 /wiki/pagecounts/part-00165
-rw-r--r--   3 root supergroup  266179174 2014-12-03 02:29 /wiki/pagecounts/part-00166
-rw-r--r--   3 root supergroup  243451716 2014-12-03 02:18 /wiki/pagecounts/part-00167
-rw-r--r--   3 root supergroup          0 2014-12-03 02:19 /wiki/pagecounts/part-00168
```  

　　其中，每个文件都以一行为单位记录，每行都符合模式：<date_time> <project_code> <page_title> <num_hits> <page_size>。其中<date_time>字段以YYYYMMDD-HHMMSS格式，<project_code>字段表示对对应的页面所使用的语言，如"en"则表示英文；<page_title>字段表示该页面在wiki上的标题，<num_hits>表示从<date_time>时间起一小时内的浏览量，<page_size>表示以字节为单位，这个页面的大小。

```  
20090507-040000 aa Main_Page 7 51309
20090507-040000 aa Special:Boardvote 1 11631
20090507-040000 aa Special:Imagelist 1 931
```

## 4. 利用spark来分析wikipedia流量数据  
　　启动spark shell。路径在/root/spark/spark-shell。

### 4.1  热身  
　　创建一个RDD，在spark-shell中，可以用sc代替SparkContext来创建RDD。这里需要注意一点，在Scala中有两种变量类型var和val，其中var是variable的缩写，val是value的缩写。顾名思义，var是可变的，val是不可变的。简单的可以把val理解成C/C++里的常量，或者Erlang里的变量【Erlang里的变量具有单次赋值的特征】。  

``` 
scala> var a ="aaa"
a: java.lang.String = aaa

scala> a = "a"
a: java.lang.String = a

scala> val b = "aaa"
b: java.lang.String = aaa

scala> b = "a"
<console>:12: error: reassignment to val
       b = "a"
         ^
```  

　　这里我们需要用val来指定一个新建的RDD，原因有2：第一，我们不需要对RDD做in place的改变，所以可以采用val来指定；其次，我们不应该对RDD做in place的改变，所以必须采用val来指定。下面，我们新建一个val型pagecounts变量，读取wikipedia 20GB的流量数据，并以两种方式打印前3条数据。  

``` 
scala> val pagecounts = sc.textFile("/wiki/pagecounts")
14/12/04 05:58:35 INFO mapred.FileInputFormat: Total input paths to process : 74
pagecounts: spark.RDD[String] = spark.MappedRDD@2fddef87

scala> pagecounts.take(3)
14/12/04 05:58:49 INFO spark.SparkContext: Starting job...
14/12/04 05:58:49 INFO spark.CacheTracker: Registering RDD ID 1 with cache
14/12/04 05:58:49 INFO spark.CacheTrackerActor: Registering RDD 1 with 177 partitions
14/12/04 05:58:49 INFO spark.CacheTracker: Registering RDD ID 0 with cache
14/12/04 05:58:49 INFO spark.CacheTrackerActor: Registering RDD 0 with 177 partitions
14/12/04 05:58:49 INFO spark.CacheTrackerActor: Asked for current cache locations
14/12/04 05:58:49 INFO spark.MesosScheduler: Final stage: Stage 0
14/12/04 05:58:49 INFO spark.MesosScheduler: Parents of final stage: List()
14/12/04 05:58:49 INFO spark.MesosScheduler: Missing parents: List()
14/12/04 05:58:49 INFO spark.MesosScheduler: Computing the requested partition locally
14/12/04 05:58:49 INFO spark.SparkContext: Job finished in 0.098193078 s
14/12/04 05:58:49 INFO spark.SparkContext: Starting job...
14/12/04 05:58:49 INFO spark.CacheTrackerActor: Asked for current cache locations
14/12/04 05:58:49 INFO spark.MesosScheduler: Final stage: Stage 1
14/12/04 05:58:49 INFO spark.MesosScheduler: Parents of final stage: List()
14/12/04 05:58:49 INFO spark.MesosScheduler: Missing parents: List()
14/12/04 05:58:49 INFO spark.MesosScheduler: Computing the requested partition locally
14/12/04 05:58:49 INFO spark.SparkContext: Job finished in 0.026119526 s
res1: Array[String] = Array(20090505-000000 aa.b ?71G4Bo1cAdWyg 1 14463, 20090505-000000 aa.b Special:Statistics 1 840, 20090505-000000 aa.b Special:Whatlinkshere/MediaWiki:Returnto 1 1019)

scala> pagecounts.take(3).foreach(println)
14/12/04 05:59:16 INFO spark.SparkContext: Starting job...
14/12/04 05:59:16 INFO spark.CacheTrackerActor: Asked for current cache locations
14/12/04 05:59:16 INFO spark.MesosScheduler: Final stage: Stage 2
14/12/04 05:59:16 INFO spark.MesosScheduler: Parents of final stage: List()
14/12/04 05:59:16 INFO spark.MesosScheduler: Missing parents: List()
14/12/04 05:59:16 INFO spark.MesosScheduler: Computing the requested partition locally
14/12/04 05:59:16 INFO spark.SparkContext: Job finished in 0.004355182 s
14/12/04 05:59:16 INFO spark.SparkContext: Starting job...
14/12/04 05:59:16 INFO spark.CacheTrackerActor: Asked for current cache locations
14/12/04 05:59:16 INFO spark.MesosScheduler: Final stage: Stage 3
14/12/04 05:59:16 INFO spark.MesosScheduler: Parents of final stage: List()
14/12/04 05:59:16 INFO spark.MesosScheduler: Missing parents: List()
14/12/04 05:59:16 INFO spark.MesosScheduler: Computing the requested partition locally
14/12/04 05:59:16 INFO spark.SparkContext: Job finished in 0.016392708 s
20090505-000000 aa.b ?71G4Bo1cAdWyg 1 14463
20090505-000000 aa.b Special:Statistics 1 840
20090505-000000 aa.b Special:Whatlinkshere/MediaWiki:Returnto 1 1019
```  

### 4.2 初试RDD Transfomation 和 RDD Action  
　　下面，我们来演示一个RDD Transformation的例子。首先，我们先看看这20GB的文件里有多少条数据，然后查询一下看所有流量数据中，有多少条是浏览的英文wiki。  
　　首先，执行pagecounts.count来查看有多少条数据。这个动作会产生177个spark任务，这里是从HDFS读书数据，所以这个任务的瓶颈实在I/O这块，整个任务执行下来大概2~3分钟。这里我执行了几次，大概花了2分钟左右的时间，执行结果如下：  

```
scala> pagecounts.count
.
.
.
14/12/05 01:19:58 INFO spark.SimpleJob: Finished TID 173 (progress: 177/177)
14/12/05 01:19:58 INFO spark.MesosScheduler: Completed ResultTask(0, 174)
14/12/05 01:19:58 INFO spark.SparkContext: Job finished in 95.251659404 s
res0: Long = 329641466
```

　　在任务运行的时候，可以打开web窗口访问：http://<master_node_hostname>:8080 来实时观察执行进度。下面是我的一个截图示例：  
![mesos-cluster](../../images/mesos-cluster.jpg)  

　　现在，我们来利用现在这个RDD来trasform出另外一个RDD，用于记录英文wiki的数据。也通过把英文wiki的流量数据写到内存里，来比较一下数据在内存中和不在内存中两种情况下一些操作的耗时。这个测试需要下面4步：  
　　1. 通过trasformation生成一个RDD[enPages]，记录英文wiki流量数据，因为这个步骤也需要遍历一边所有数据，所以这个步骤耗时也应该和上一个 pagecounts.count 耗时相当。

``` 
scala> val enPages = pagecounts.filter(_.split(" ")(1) == "en")
enPages: spark.RDD[String] = spark.FilteredRDD@1b8f2e35

scala> enPages.count
.
.
.
14/12/05 01:51:01 INFO spark.SparkContext: Job finished in 114.035390332 s
res1: Long = 122352588
```  

　　2. 把enPages缓存到内存中  

```  
scala> enPages.cache
res0: spark.RDD[String] = spark.FilteredRDD@78bf34f4
```  

　　3. 执行enPages.count，看看执行速度有神马区别，what happened? 按照原计划，现在不应该是神速吗？仔细看看下面的执行log，是不是有一种恍然大悟的赶脚啊？  

```  
scala> enPages.count
.
.
.
14/12/05 01:59:33 INFO spark.SimpleJob: Size of task 0:176 is 10680 bytes and took 4 ms to serialize by spark.JavaSerializerInstance
14/12/05 01:59:33 INFO spark.CacheTrackerActor: Cache entry added: (2, 176) on ip-172-31-25-137.ec2.internal (size added: 16.0B, available: 6.0GB)
14/12/05 01:59:33 INFO spark.SimpleJob: Finished TID 176 (progress: 172/177)
14/12/05 01:59:33 INFO spark.MesosScheduler: Completed ResultTask(0, 176)
14/12/05 01:59:34 INFO spark.CacheTrackerActor: Cache entry added: (2, 170) on ip-172-31-25-139.ec2.internal (size added: 10.3MB, available: 5.0GB)
14/12/05 01:59:34 INFO spark.SimpleJob: Finished TID 169 (progress: 173/177)
14/12/05 01:59:34 INFO spark.MesosScheduler: Completed ResultTask(0, 170)
14/12/05 01:59:35 INFO spark.CacheTrackerActor: Cache entry added: (2, 172) on ip-172-31-25-137.ec2.internal (size added: 183.3MB, available: 5.8GB)
14/12/05 01:59:35 INFO spark.SimpleJob: Finished TID 171 (progress: 174/177)
14/12/05 01:59:35 INFO spark.MesosScheduler: Completed ResultTask(0, 172)
14/12/05 01:59:35 INFO spark.CacheTrackerActor: Cache entry added: (2, 175) on ip-172-31-25-138.ec2.internal (size added: 16.0B, available: 6.1GB)
14/12/05 01:59:35 INFO spark.SimpleJob: Finished TID 174 (progress: 175/177)
14/12/05 01:59:35 INFO spark.MesosScheduler: Completed ResultTask(0, 175)
14/12/05 01:59:36 INFO spark.CacheTrackerActor: Cache entry added: (2, 173) on ip-172-31-25-138.ec2.internal (size added: 16.0B, available: 6.1GB)
14/12/05 01:59:36 INFO spark.SimpleJob: Finished TID 172 (progress: 176/177)
14/12/05 01:59:36 INFO spark.MesosScheduler: Completed ResultTask(0, 173)
14/12/05 01:59:36 INFO spark.CacheTrackerActor: Cache entry added: (2, 174) on ip-172-31-25-139.ec2.internal (size added: 178.3MB, available: 4.8GB)
14/12/05 01:59:36 INFO spark.SimpleJob: Finished TID 173 (progress: 177/177)
14/12/05 01:59:36 INFO spark.MesosScheduler: Completed ResultTask(0, 174)
14/12/05 01:59:36 INFO spark.SparkContext: Job finished in 130.727017576 s
res0: Long = 122352588
```

　　4. 好，现在我们再次执行enPages.count，看看是不是有神马神奇的事情发生了。  

```
scala> enPages.count
.
.
.
14/12/05 02:12:01 INFO spark.SparkContext: Job finished in 2.492567199 s
res2: Long = 122352588
```  
　　
　　哇，130秒和2.5秒的对决，心算一下，52倍啊，如果visualize一下这个数据，估计会更让人吃惊吧。擅于YY的我不禁用echarts画了个图，感受一下内存计算的神速。画图代码如下，直接把代码粘贴到[echarts bar](http://echarts.baidu.com/doc/example/bar1.html#macarons)，在再点击刷新就可以看到图了。 

``` 
option = {
    title : {
        text: 'enPages.count',
        subtext: 'by taotao.li'
    },
    tooltip : {
        trigger: 'axis'
    },
    legend: {
        data:['no cache','cache']
    },
    toolbox: {
        show : true,
        feature : {
            mark : {show: true},
            dataView : {show: true, readOnly: false},
            magicType : {show: true, type: ['line', 'bar']},
            restore : {show: true},
            saveAsImage : {show: true}
        }
    },
    calculable : true,
    xAxis : [
        {
            type : 'category',
            data : ['one time']
        }
    ],
    yAxis : [
        {
            type : 'value'
        }
    ],
    series : [
        {
            name:'no cache',
            type:'bar',
            data:[130.727017576]
        },
        {
            name:'cache',
            type:'bar',
            data:[2.492567199]
        }
    ]
};

```

![enPages-pic](../../images/enPages-pic.jpg)  
