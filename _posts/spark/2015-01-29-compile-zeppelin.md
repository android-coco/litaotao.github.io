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