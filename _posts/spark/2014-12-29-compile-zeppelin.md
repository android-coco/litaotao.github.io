---
category: spark
published: false
layout: post
title: ［touch spark］4. 编译Zeppelin
description: ～～～	
---  


##  
## 1. 写在前面  
　　这篇记录是我按照[官网](http://zeppelin-project.org/docs/install/install.html)的步骤来写的，主要是记录在编译Zeppelin过程中的一些经验。


## 2. 详细步骤及错误解决

### 2.1 集群方式编译
　　`mvn install -DskipTests -Dspark.version=1.1.0 -Dhadoop.version=2.2.0`
　　出错：

	[INFO] [compiler:compile {execution: default-compile}]
	[INFO] Changes detected - recompiling the module!
	[INFO] Compiling 23 source files to /root/Desktop/zeppelin/zeppelin-release-0.4.0/zeppelin-zengine/target/classes
	[INFO] -------------------------------------------------------------
	[ERROR] COMPILATION ERROR : 
	[INFO] -------------------------------------------------------------
	[ERROR] No compiler is provided in this environment. Perhaps you are running on a JRE rather than a JDK?
	[INFO] 1 error
	[INFO] -------------------------------------------------------------
	[INFO] ------------------------------------------------------------------------
	[ERROR] BUILD FAILURE
	[INFO] ------------------------------------------------------------------------
	[INFO] Compilation failure
	No compiler is provided in this environment. Perhaps you are running on a JRE rather than a JDK?

	[INFO] ------------------------------------------------------------------------
	[INFO] For more information, run Maven with the -e switch
	[INFO] ------------------------------------------------------------------------
	[INFO] Total time: 11 minutes 38 seconds
	[INFO] Finished at: Tue Dec 30 10:11:41 CST 2014
	[INFO] Final Memory: 63M/356M
	[INFO] ------------------------------------------------------------------------  

   
　　我想应该是没有找到java的执行路径吧，查看$JAVA_HOME发现为空，配置一下JAVA_HOME后再次执行试下。还是不行，于是Google了一下，发现强大的[SO](http://stackoverflow.com/questions/26313902/maven-error-perhaps-you-are-running-on-a-jre-rather-than-a-jdk)已经有答案了，按照这篇SO的描述，我按如下步骤继续尝试： 

	mvn --version
	Apache Maven 2.2.1 (rdebian-8)
	Java version: 1.6.0_32
	Java home: /usr/lib/jvm/java-6-openjdk-amd64/jre
	Default locale: en_US, platform encoding: UTF-8
	OS name: "linux" version: "3.2.0-29-generic" arch: "amd64" Family: "unix"

　　原来如此，看到第三行输出Java home: /usr/lib/jvm/java-6-openjdk-amd64/jre，和错误信息提示No compiler is provided in this environment. Perhaps you are running on a JRE rather than a JDK?一直，那应该是JAVA_HOME配置错了吧，应该配置到JDK才对。Opps，想起来了，当初我把第一次献给spark的时候，是下载pre-built版本的spark，而运行pre-built的spark不需要JDK，只需要JRE，so当初就只安装了JRE而已。Sigh，果然是出来混，早晚都是要还的啊。 
![had-to-give-back](../../images/had-to-give-back.jpg)  
　　那就先把JDK装上吧，这里我是参考了这篇[文章](http://blog.csdn.net/tecn14/article/details/24797545)。先是下载jdk-7u71-linux-x64.gz文件包，然后解压并复制到/usr/local下面，最后是配置环境变量，我是自己编辑了一个java_1.7_path.bashrc的文件，文件内容如下：  

	export PATH=/usr/local/jdk1.7.0_71/bin:$PATH
	export CLASSPATH="/usr/local/jdk1.7.0_71/lib:."
	export JAVA_HOME="/usr/local/jdk1.7.0_71/"

　　执行 `. java_1.7_path.bashrc` 文件就可以了。现在再次编译Zeppelin就成功了，输出如下：  

	[INFO] ------------------------------------------------------------------------
	[INFO] For more information, run Maven with the -e switch
	[INFO] ------------------------------------------------------------------------
	[INFO] Total time: 52 minutes 50 seconds
	[INFO] Finished at: Tue Dec 30 12:12:38 CST 2014
	[INFO] Final Memory: 63M/367M
	[INFO] ------------------------------------------------------------------------

　　编译Zeppelin还是挺花时间的，下次可以不用这么折腾了，官网上有编译好的版本下载的。然而奇怪的是，现在运行mvn -version还是如下： 

	Apache Maven 2.2.1 (rdebian-8)
	Java version: 1.7.0_71
	Java home: /usr/local/jdk1.7.0_71/jre
	Default locale: en_US, platform encoding: UTF-8
	OS name: "linux" version: "3.2.0-29-generic" arch: "amd64" Family: "unix"
　　
　　Java home还是jre结尾的，看来刚才的分析似乎不太对，答案可能在这两个帖子里面[1](http://stackoverflow.com/questions/26313902/maven-error-perhaps-you-are-running-on-a-jre-rather-than-a-jdk)， [2](http://comments.gmane.org/gmane.comp.jakarta.turbine.maven.user/130257)，这个细节我就先不去追究了，先把Zeppedlin配置好了再说。

### 2.2 配置
　　到conf目录下，创建两个配置文件，可以保持默认配置。然后执行配置文件，我这里执行xml配置文件的时候提示出错了。

	cp zeppelin-env.sh.template zeppelin-env.sh
	cp zeppelin-site.xml.template zeppelin-site.xml
	root@ubuntu2[14:58:36]:~/Desktop/zeppelin/zeppelin-release-0.4.0/conf#. zeppelin-env.sh
	root@ubuntu2[14:59:28]:~/Desktop/zeppelin/zeppelin-release-0.4.0/conf#. zeppelin-site.xml
	-bash: zeppelin-site.xml: line 1: syntax error near unexpected token `newline'
	-bash: zeppelin-site.xml: line 1: `<?xml version="1.0"?>'

### 2.3 初次运行
　　上面已经出了几个错误，现在果然运行不成功啊。

	root@ubuntu2[15:03:29]:~/Desktop/zeppelin/zeppelin-release-0.4.0#./bin/zeppelin-daemon.sh start
	find: `/root/../zeppelin-web': No such file or directory
	find: `/root/../zeppelin-docs': No such file or directory
	Log dir doesn't exist, create /root/../logs
	Pid dir doesn't exist, create /root/../notebook
	Start Zeppelin
	failed to launch Zeppelin:
	  Error: Could not find or load main class com.nflabs.zeppelin.server.ZeppelinServer
	full log in /root/../logs/zeppelin-root-ubuntu2.out

