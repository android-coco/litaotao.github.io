---
category: erlang  
published: false  
layout: post  
title: ［touch spark］2. spark 一些错误和解决办法
description: 随时更新哦~~~
---  

##  
## 1. ERROR Remoting: Remoting error: [Startup failed]   
环境： Linux ubuntu2 3.2.0-29-generic #46-Ubuntu SMP Fri Jul 27 17:03:23 UTC 2012 x86_64 x86_64 x86_64 GNU/Linux  
错误： 运行spark-shell出错：ERROR Remoting: Remoting error: [Startup failed]   
解决： [stackoverflow](http://stackoverflow.com/questions/26305930/error-when-running-spark-shell-error-remoting-remoting-error-startup-failed)    
步骤:
>>
1. cd 到spark 配置文件目录下：spark/spark-1.1.1-bin-hadoop2.4/conf  
2. 用环境配置模板新建一个配置文件： cp spark-env.sh.template spark-env.sh
3. vi spark-env.sh, 在`# - SPARK_LOCAL_IP, to set the IP address Spark binds to on this node`这行下面加上一行`SPARK_LOCAL_IP=LOCALHOST`   
4. 重新执行spark-shell即可   


## 2.   

