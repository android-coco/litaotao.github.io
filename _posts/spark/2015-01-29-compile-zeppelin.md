---
category: spark
published: false
layout: post
title: ［touch spark］8. 编译Zeppelin
description: ～～～	
---  


##  
## 1. 写在前面  
　　这篇记录是我按照[官网](http://zeppelin-project.org/docs/install/install.html)的步骤来写的，主要是记录在编译Zeppelin过程中的一些经验。  
　　对于这类没有发布特别稳定版本的项目，我倾向于这样一种实践方法，在本地建两个文件夹：project, project-build，把project文件夹作为一个本地的repo，可以随时update到最新的源码，然后在project-build里构建，就算失败了也可以保证不会污染项目源文件。
　　再具体一点就是我在实践Zeppelin的时候使用的方法，如下所示，可以随时保证zeppelin文件夹里的源码最新，然后在zeppelin-build里用最新的源码构建。

```
root@kali:~/Desktop# mkdir zeppelin zeppelin-build
root@kali:~/Desktop# cd zeppelin
root@kali:~/Desktop/zeppelin# git init
Initialized empty Git repository in /root/Desktop/zeppelin/.git/
root@kali:~/Desktop/zeppelin# git remote add origin git@github.com:NFLabs/zeppelin.git
root@kali:~/Desktop/zeppelin# git pull origin master
root@kali:~/Desktop/zeppelin# cd ../zeppelin-build/
root@kali:~/Desktop/zeppelin-build# cp -R ../zeppelin/* .
root@kali:~/Desktop/zeppelin-build# mvn clean package -DskipTests
```

## 2. 详细步骤及错误解决

### 2.1 按照默认配置编译 : mvn clean package -DskipTests

```
root@ubuntu2[15:30:17]:~/Desktop/zeppelin-build#mvn clean package -DskipTests
.
.
.
[INFO] npm WARN deprecated grunt-ngmin@0.0.3: use grunt-ng-annotate instead
[INFO] npm ERR! 
[INFO] npm ERR! Additional logging details can be found in:
[INFO] npm ERR!     /root/Desktop/zeppelin-build/zeppelin-web/npm-debug.log
[INFO] npm ERR! not ok code 0
[INFO] ------------------------------------------------------------------------
[INFO] Reactor Summary:
[INFO] 
[INFO] Zeppelin ........................................... SUCCESS [ 37.320 s]
[INFO] Zeppelin: Zengine .................................. SUCCESS [  9.899 s]
[INFO] Zeppelin: Spark .................................... SUCCESS [ 12.115 s]
[INFO] Zeppelin: Markdown interpreter ..................... SUCCESS [  2.257 s]
[INFO] Zeppelin: Shell interpreter ........................ SUCCESS [  2.239 s]
[INFO] Zeppelin: web Application .......................... FAILURE [04:10 min]
[INFO] Zeppelin: Server ................................... SKIPPED
[INFO] Zeppelin: Packaging distribution ................... SKIPPED
[INFO] ------------------------------------------------------------------------
[INFO] BUILD FAILURE
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 05:15 min
[INFO] Finished at: 2015-02-11T15:30:16+08:00
[INFO] Final Memory: 61M/409M
[INFO] ------------------------------------------------------------------------
[ERROR] Failed to execute goal com.github.eirslett:frontend-maven-plugin:0.0.20:npm (npm install) on project zeppelin-web: Failed to run task: 'npm install --color=false' failed. (error code 1) -> [Help 1]
[ERROR] 
[ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
[ERROR] Re-run Maven using the -X switch to enable full debug logging.
[ERROR] 
[ERROR] For more information about the errors and possible solutions, please read the following articles:
[ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/MojoFailureException
[ERROR] 
[ERROR] After correcting the problems, you can resume the build with the command
[ERROR]   mvn <goals> -rf :zeppelin-web
```

### 2.1 出错: npm install --color=false
　　这个错误在[mailing list](https://groups.google.com/forum/#!searchin/zeppelin-developers/npm$20install)里提到了，我们按照里面的解决方案来尝试一下。注意，以前的mailing list的维护在google groups里面的，但今年2月份之后groups就只读，不可以发帖了，新的mailing list移植到apache旗下，地址在[这里](http://mail-archives.apache.org/mod_mbox/incubator-zeppelin-users/)。
　　解决方案：先在zeppelin-web文件夹里运行 `npm install`，然后再回到zeppelin-build目录构建。

### 2.2 构建成功，可以运行markdown语句，但不能运行scala语句   
　　这个问题很奇怪，如下图所示，可以运行markdown，但不可以运行scala，spark和sql，看日志好像是和scala有关系。
![markdown-scala](../images/markdown-scala.jpg)   
　　下面是运行日志 logs/zeppelin-root-ubuntu2.log 里的摘要：  

```
# exec markdown

 INFO [2015-02-13 15:28:08,180] ({WebSocketWorker-8} NotebookServer.java[onMessage]:76) - RECEIVE << RUN_PARAGRAPH
 INFO [2015-02-13 15:28:08,180] ({WebSocketWorker-8} Note.java[persist]:263) - Persist note 2ADHVQAWJ into /root/Desktop/zeppelin-build/notebook/2ADHVQAWJ/note.json
 INFO [2015-02-13 15:28:08,184] ({WebSocketWorker-8} NotebookServer.java[broadcast]:205) - SEND >> NOTE
 INFO [2015-02-13 15:28:08,186] ({WebSocketWorker-8} NotebookServer.java[broadcast]:205) - SEND >> NOTE
 INFO [2015-02-13 15:28:08,188] ({pool-2-thread-7} SchedulerFactory.java[jobStarted]:94) - Job paragraph_1423811165331_-1611479589 started by scheduler com.nflabs.zeppelin.markdown.Markdown263264514
 INFO [2015-02-13 15:28:08,188] ({pool-2-thread-7} NotebookServer.java[broadcast]:205) - SEND >> NOTE
 INFO [2015-02-13 15:28:08,190] ({pool-2-thread-7} Paragraph.java[jobRun]:165) - run paragraph 20150213-150605_329484409 using md com.nflabs.zeppelin.interpreter.LazyOpenInterpreter@35d2c3c6
 INFO [2015-02-13 15:28:08,191] ({pool-2-thread-7} Paragraph.java[jobRun]:183) - RUN :   # ***Hello, every one, I love you all***
 INFO [2015-02-13 15:28:08,191] ({pool-2-thread-7} NotebookServer.java[afterStatusChange]:456) - Job 20150213-150605_329484409 is finished
 INFO [2015-02-13 15:28:08,191] ({pool-2-thread-7} Note.java[persist]:263) - Persist note 2ADHVQAWJ into /root/Desktop/zeppelin-build/notebook/2ADHVQAWJ/note.json
 INFO [2015-02-13 15:28:08,195] ({pool-2-thread-7} NotebookServer.java[broadcast]:205) - SEND >> NOTE
 INFO [2015-02-13 15:28:08,197] ({pool-2-thread-7} SchedulerFactory.java[jobFinished]:99) - Job paragraph_1423811165331_-1611479589 finished by scheduler com.nflabs.zeppelin.markdown.Markdown263264514


# exec spark

 INFO [2015-02-13 15:28:19,388] ({WebSocketWorker-8} NotebookServer.java[onMessage]:76) - RECEIVE << RUN_PARAGRAPH
 INFO [2015-02-13 15:28:19,388] ({WebSocketWorker-8} Note.java[persist]:263) - Persist note 2ADHVQAWJ into /root/Desktop/zeppelin-build/notebook/2ADHVQAWJ/note.json
 INFO [2015-02-13 15:28:19,393] ({WebSocketWorker-8} NotebookServer.java[broadcast]:205) - SEND >> NOTE
 INFO [2015-02-13 15:28:19,394] ({WebSocketWorker-8} NotebookServer.java[broadcast]:205) - SEND >> NOTE
 INFO [2015-02-13 15:28:19,396] ({pool-2-thread-4} SchedulerFactory.java[jobStarted]:94) - Job paragraph_1423811203262_-601452430 started by scheduler com.nflabs.zeppelin.spark.SparkInterpreter1951918777
 INFO [2015-02-13 15:28:19,396] ({pool-2-thread-4} NotebookServer.java[broadcast]:205) - SEND >> NOTE
 INFO [2015-02-13 15:28:19,398] ({pool-2-thread-4} Paragraph.java[jobRun]:165) - run paragraph 20150213-150643_299836602 using spark com.nflabs.zeppelin.interpreter.LazyOpenInterpreter@285f4e6b
 INFO [2015-02-13 15:28:19,414] ({pool-2-thread-4} Logging.scala[logInfo]:59) - Changing view acls to: root
 INFO [2015-02-13 15:28:19,414] ({pool-2-thread-4} Logging.scala[logInfo]:59) - Changing modify acls to: root
 INFO [2015-02-13 15:28:19,414] ({pool-2-thread-4} Logging.scala[logInfo]:59) - SecurityManager: authentication disabled; ui acls disabled; users with view permissions: Set(root); users with modify permissions: Set(root)
 INFO [2015-02-13 15:28:19,414] ({pool-2-thread-4} Logging.scala[logInfo]:59) - Starting HTTP Server
 INFO [2015-02-13 15:28:19,415] ({pool-2-thread-4} Server.java[doStart]:272) - jetty-8.1.14.v20131031
 INFO [2015-02-13 15:28:19,422] ({pool-2-thread-4} AbstractConnector.java[doStart]:338) - Started SocketConnector@0.0.0.0:46268
 INFO [2015-02-13 15:28:19,422] ({pool-2-thread-4} Logging.scala[logInfo]:59) - Successfully started service 'HTTP class server' on port 46268.
 WARN [2015-02-13 15:28:19,569] ({pool-2-thread-4} Logging.scala[logWarning]:71) - Warning: compiler accessed before init set up.  Assuming no postInit code.
ERROR [2015-02-13 15:28:19,572] ({pool-2-thread-4} Job.java[run]:164) - Job failed
java.lang.AssertionError: assertion failed: null
        at scala.Predef$.assert(Predef.scala:179)
        at org.apache.spark.repl.SparkIMain.initializeSynchronous(SparkIMain.scala:203)
        at com.nflabs.zeppelin.spark.SparkInterpreter.open(SparkInterpreter.java:271)
        at com.nflabs.zeppelin.interpreter.ClassloaderInterpreter.open(ClassloaderInterpreter.java:83)
        at com.nflabs.zeppelin.interpreter.LazyOpenInterpreter.open(LazyOpenInterpreter.java:52)
        at com.nflabs.zeppelin.interpreter.LazyOpenInterpreter.bindValue(LazyOpenInterpreter.java:88)
        at com.nflabs.zeppelin.notebook.Paragraph.jobRun(Paragraph.java:175)
        at com.nflabs.zeppelin.scheduler.Job.run(Job.java:147)
        at com.nflabs.zeppelin.scheduler.FIFOScheduler$1.run(FIFOScheduler.java:85)
        at java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:471)
        at java.util.concurrent.FutureTask.run(FutureTask.java:262)
        at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.access$201(ScheduledThreadPoolExecutor.java:178)
        at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.run(ScheduledThreadPoolExecutor.java:292)
        at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1145)
        at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:615)
        at java.lang.Thread.run(Thread.java:745)
 INFO [2015-02-13 15:28:19,574] ({pool-2-thread-4} NotebookServer.java[afterStatusChange]:456) - Job 20150213-150643_299836602 is finished
 INFO [2015-02-13 15:28:19,574] ({pool-2-thread-4} Note.java[persist]:263) - Persist note 2ADHVQAWJ into /root/Desktop/zeppelin-build/notebook/2ADHVQAWJ/note.json
 INFO [2015-02-13 15:28:19,578] ({pool-2-thread-4} NotebookServer.java[broadcast]:205) - SEND >> NOTE
 INFO [2015-02-13 15:28:20,230] ({pool-2-thread-4} SchedulerFactory.java[jobFinished]:99) - Job paragraph_1423811203262_-601452430 finished by scheduler com.nflabs.zeppelin.spark.SparkInterpreter1951918777
 INFO [2015-02-13 15:28:20,241] ({Thread-62} Logging.scala[logInfo]:59) - Changing view acls to: root
 INFO [2015-02-13 15:28:20,242] ({Thread-62} Logging.scala[logInfo]:59) - Changing modify acls to: root
 INFO [2015-02-13 15:28:20,242] ({Thread-62} Logging.scala[logInfo]:59) - SecurityManager: authentication disabled; ui acls disabled; users with view permissions: Set(root); users with modify permissions: Set(root)
 INFO [2015-02-13 15:28:20,242] ({Thread-62} Logging.scala[logInfo]:59) - Starting HTTP Server
 INFO [2015-02-13 15:28:20,243] ({Thread-62} Server.java[doStart]:272) - jetty-8.1.14.v20131031
 INFO [2015-02-13 15:28:20,245] ({Thread-62} AbstractConnector.java[doStart]:338) - Started SocketConnector@0.0.0.0:56107
 INFO [2015-02-13 15:28:20,245] ({Thread-62} Logging.scala[logInfo]:59) - Successfully started service 'HTTP class server' on port 56107.
 WARN [2015-02-13 15:28:20,393] ({Thread-62} Logging.scala[logWarning]:71) - Warning: compiler accessed before init set up.  Assuming no postInit code.
```

