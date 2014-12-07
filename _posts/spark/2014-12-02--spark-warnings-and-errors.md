---
category: spark  
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

## 2. SSH Connections freezing with “Write failed: Broken pipe”
环境： Linux ubuntu2 3.2.0-29-generic #46-Ubuntu SMP Fri Jul 27 17:03:23 UTC 2012 x86_64 x86_64 x86_64 GNU/Linux  
错误： ssh到Amazon EC2上的master进行操作时，长时间不操作后ssh自动断开   
解决： [配置/etc/ssh/ssh_config文件](http://adminsgoodies.com/ssh-connections-freezing-with-%E2%80%9Cwrite-failed-broken-pipe%E2%80%9D/)    
步骤:
>>  
1. ssh配置文件一般有两个，在/etc/ssh/下面，其中sshd_config是全局共享的，config是用户专用的。我们需要修改sshd_config文件；  
2. vi /etc/ssh/sshd_config；  
3. 修改字段KeepAlive的值为yes，ClientAliveInterval的值为60；若没有这两个字段，可以自己新建一个；  
4. service ssh restart 重启ssh服务。  

