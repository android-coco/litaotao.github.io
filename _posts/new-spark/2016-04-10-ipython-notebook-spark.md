---
layout: post
published: true
title: 『 Spark 』9. 搭建 IPython + Notebook + Spark 开发环境
description: know more, do better 
---  


## 写在前面

本系列是综合了自己在学习spark过程中的理解记录 ＋ 对参考文章中的一些理解 ＋ 个人实践spark过程中的一些心得而来。写这样一个系列仅仅是为了梳理个人学习spark的笔记记录，所以一切以能够理解为主，没有必要的细节就不会记录了，而且文中有时候会出现英文原版文档，只要不影响理解，都不翻译了。若想深入了解，最好阅读参考文章和官方文档。

其次，本系列是基于目前最新的 spark 1.6.0 系列开始的，spark 目前的更新速度很快，记录一下版本号还是必要的。   
最后，如果各位觉得内容有误，欢迎留言备注，所有留言 24 小时内必定回复，非常感谢。     

Tips: 如果插图看起来不明显，可以：1. 放大网页；2. 新标签中打开图片，查看原图哦；3. 点击右边目录上方的 *present mode* 哦。

## 1. 致谢   

首先我忠心地感谢 IPython，Spark 的开源作者，真心谢谢你们开发这么方便，好用，功能强大的项目，而且还无私地奉献给大众使用。刚刚很轻松地搭建了一个基于 IPython Notebook 的 Spark 开发环境，真的感受到 The power of technology, the power of open source.  
下面是这两个项目的 github 地址：  

- [Ipython](https://github.com/ipython/ipython)  
- [Spark](https://github.com/apache/spark)  

同时，这篇文章在刚开始的部分，参考了很多 [这篇博客](http://blog.cloudera.com/blog/2014/08/how-to-use-ipython-notebook-with-apache-spark/)的内容，感谢这么多人能无私分享如此高质量的内容。   
但是，这篇文章不是简单记录怎么做，我尽量做到量少质高，所以有些地方会说得比较详细，其中也会提到在解决遇到的问题上的一些方法和思路。

## 2. 原理

Ipython 支持自定义的配置文件，而且配置文件可以极其灵活的定义，我们可以借此在启动 IPython 的时候去做一些自定义的事，比如说加载一些模块，做一些初始化的工作。这里我们就是利用 Ipython 的这个灵活的特性，在启动 Ipython 的时候，自动加载 spark 的 pyspark 包，甚至是初始化一个 SparkContext。

具体我们来看如何创建一个配置文件，并且指定一个配置文件启动 ipython。

## 3. 配置Ipython  

### 3.1 ipython 配置名profile介绍

- profile 命令说明    

profile 是 ipython 的一个子命令，其中 profile 又有两个子命令，分别是 create和list，顾名思义，create就是创建一个配置文件，list就是列出当前配置文件。如下：  

{% highlight shell %}

root@ubuntu2[13:54:01]:~/Desktop#ipython profile
No subcommand specified. Must specify one of: ['create', 'list']

Manage IPython profiles

Profile directories contain configuration, log and security related files and
are named using the convention 'profile_<name>'. By default they are located in
your ipython directory.  You can create profiles with `ipython profile create
<name>`, or see the profiles you already have with `ipython profile list`

To get started configuring IPython, simply do:

$> ipython profile create

and IPython will create the default profile in <ipython_dir>/profile_default,
where you can edit ipython_config.py to start configuring IPython.

Subcommands
-----------

Subcommands are launched as `ipython cmd [args]`. For information on using
subcommand 'cmd', do: `ipython cmd -h`.

create
    Create an IPython profile by name
list
    List available IPython profiles

{% endhighlight %}

- profile子命令 list 说明    

本想 list 命令应该很简单的，和 linux 下的 ls 差不多嘛，但我自己看了下，其中还是有些细节值得推敲的。其中这项 *Available profiles in /root/.config/ipython:* 是说目前有两个配置文件在那个目录下面，pyspark是我自己创建的了。在参考的[这篇文章](http://blog.cloudera.com/blog/2014/08/how-to-use-ipython-notebook-with-apache-spark/)中，作者说创建的配置文件会放到 *~/.ipython/profile_pyspark/* 下，其实这并不是一定的，具体放在哪个目录下面，可以根据 profile list 的命令来查看。如此看来，我们在这台机器上创建的配置文件应该是放在目录 */root/.config/ipython* 下面的。

{% highlight shell %}

root@ubuntu2[14:09:12]:~/Desktop#ipython profile list

Available profiles in IPython:
    pysh
    math
    sympy
    cluster

    The first request for a bundled profile will copy it
    into your IPython directory (/root/.config/ipython),
    where you can customize it.

Available profiles in /root/.config/ipython:
    default
    pyspark

To use any of the above profiles, start IPython with:
    ipython --profile=<name>  

{% endhighlight %}

- profile子命令 create 说明    

简单介绍下create子命令的用法。

{% highlight shell %}

root@ubuntu2[09:25:57]:~/Desktop#ipython profile help create
Create an IPython profile by name

Create an ipython profile directory by its name or profile directory path.
Profile directories contain configuration, log and security related files and
are named using the convention 'profile_<name>'. By default they are located in
your ipython directory. Once created, you will can edit the configuration files
in the profile directory to configure IPython. Most users will create a profile
directory by name, `ipython profile create myprofile`, which will put the
directory in `<ipython_dir>/profile_myprofile`.

{% endhighlight %}

### 3.2 创建新的Ipython配置文件    
- 创建配置文件     

因为我之前已经配置过一个pyspark的配置文件了，这里我们创建一个测试用的配置文件，pytest。运行一下命令后，会在 */root/.config/ipython* 下生成一个 pytest 的目录。

{% highlight shell %}

root@ubuntu2[14:54:14]:~/Desktop#ipython profile create pytest
[ProfileCreate] Generating default config file: u'/root/.config/ipython/profile_pytest/ipython_config.py'
[ProfileCreate] Generating default config file: u'/root/.config/ipython/profile_pytest/ipython_notebook_config.py'

root@ubuntu2[15:00:57]:~/Desktop#ls ~/.config/ipython/profile_pytest/
ipython_config.py  ipython_notebook_config.py  log  pid  security  startup

{% endhighlight %}

### 3.3 编辑配置文件
- 编辑 *ipython_notebook_config.py*   

需要更改的只有下面三项：

- *c.NotebookApp.ip*: 启动服务的地址，设置成 '*' 可以从同一网段的其他机器访问到；
- *c.NotebookApp.open_browser*: 设置成 'False'，表示启动 ipython notebook 的时候不会自动打开浏览器；
- *c.NotebookApp.password*: 设置 ipython notebook 的登陆密码，怎么设置看下面；

{% highlight python %}

c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False    
c.NotebookApp.password = "sha1:c6b748a8e1e2:4688f91ccfb9a8e0afd041ec77cdda99d0e1fb8f"

{% endhighlight %}

- 设置访问密码   
如果你的 notebook server 是需要访问控制的，简单的话可以设置一个访问密码。

    + 生成密码
    + 编辑配置文件，设置密码

{% highlight python %}

In [4]: from IPython.lib import passwd

In [5]: passwd()
Enter password:
Verify password:
Out[5]: 'sha1:e819609871c8:1039dbc5a1392fc230d371d1ce19511490978685'

In [6]:

### set password 
c.NotebookApp.password = "sha1:c6b748a8e1e2:4688f91ccfb9a8e0afd041ec77cdda99d0e1fb8f"

{% endhighlight %}

- 设置启动文件  
这一步算是比较重要的了，也是我在配置这个notebook server中遇到的比较难解的问题。这里我们首先需要创建一个启动文件，并在启动文件里设置一些spark的启动参数。如下：

```
root@ubuntu2[09:52:14]:~/Desktop#touch ~/.config/ipython/profile_pytest/startup/00-pytest-setup.py
root@ubuntu2[10:08:44]:~/Desktop#vi ~/.config/ipython/profile_pytest/startup/00-pytest-setup.py   

import os
import sys

spark_home = os.environ.get('SPARK_HOME', None)
if not spark_home:
    raise ValueError('SPARK_HOME environment variable is not set')
sys.path.insert(0, os.path.join(spark_home, 'python'))
sys.path.insert(0, os.path.join(spark_home, 'python/lib/py4j-0.8.2.1-src.zip'))
# execfile(os.path.join(spark_home, 'python/pyspark/shell.py'))
```

上面的启动配置文件也还简单，即拿到 *spark_home* 路径，并在系统环境变量 path 里加上两个路径，然后再执行一个 *shell.py* 文件。不过，在保存之前还是先确认下配置文件写对了，比如说你的 SPARK_HOME 配置对了，并且下面有 python 这个文件夹，并且 *python/lib 下有 py4j-0.8.1* 这个文件。我在检查的时候就发现我的包版本是 py4j-0.8.2.1 的，所以还是要改得和自己的包一致才行。   
这里得到一个经验，在这种手把手，step by step的教程中，一定要注意版本控制，毕竟各人的机器，操作系统，软件版本等都不可能完全一致，也许在别人机器上能成功，在自己的机器上不成功也是很正常的事情，毕竟细节决定成败啊！所以在我这里，这句我是这样写的： *sys.path.insert(0, os.path.join(spark_home, 'python/lib/py4j-0.8.2.1-src.zip'))*    
注意，上面的最后一行 *execfile(os.path.join(spark_home, 'python/pyspark/shell.py'))* 被注释掉了，表示在新建或打开一个 notebook 时并不去执行 *shell.py* 这个文件，这个文件是创建 SparkContext 的，即如果执行改行语句，那在启动 notebook 时就会初始化一个 sc，但这个 sc 的配置都是写死了的，在 spark web UI 监控里的 appName 也是一样的，很不方便。而且考虑到并不是打开一个 notebook 就要用到 spark 的资源，所以最好是要用户自己定义 sc 了。  

python/pyspark/shell.py 的核心代码：   

```
sc = SparkContext(appName="PySparkShell", pyFiles=add_files)
atexit.register(lambda: sc.stop())
```


## 4. Ok，here we go
到这里差不多大功告成了，可以启动notebook server了。不过在启动之前，需要配置两个环境变量参数，同样，这两个环境变量参数在也是根据个人配置而定的。  

```
# for the CDH-installed Spark
export SPARK_HOME='/usr/local/spark-1.2.0-bin-cdh4/'

# this is where you specify all the options you would normally add after bin/pyspark
export PYSPARK_SUBMIT_ARGS='--master spark://10.21.208.21:7077 --deploy-mode client'
```

ok，万事具备，只欠东风了。让我们来尝尝鲜吧：

```
root@ubuntu2[10:40:50]:~/Desktop#ipython notebook --profile=pyspark
2015-02-01 10:40:54.850 [NotebookApp] Using existing profile dir: u'/root/.config/ipython/profile_pyspark'
2015-02-01 10:40:54.858 [NotebookApp] Using MathJax from CDN: http://cdn.mathjax.org/mathjax/latest/MathJax.js
2015-02-01 10:40:54.868 [NotebookApp] CRITICAL | WARNING: The notebook server is listening on all IP addresses and not using encryption. This is not recommended.
2015-02-01 10:40:54.869 [NotebookApp] Serving notebooks from local directory: /root/Desktop
2015-02-01 10:40:54.869 [NotebookApp] The IPython Notebook is running at: http://[all ip addresses on your system]:8880/
2015-02-01 10:40:54.869 [NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
```

在浏览器输入driver:8880即可访问notebook server了，首先会提示输入密码，密码正确后就可以使用了。
![notebook-spark-1](http://litaotao.github.io/images/notebook-spark-1.jpg)
![notebook-spark-2](http://litaotao.github.io/images/notebook-spark-2.jpg)


## 5. 总结
下面是简单的步骤总结：

- 建立环境变量配置文件：*ipython_notebook_spark.bashrc *   

```
export SPARK_HOME="/usr/local/spark-1.2.0-bin-cdh4/"
export PYSPARK_SUBMIT_ARGS="--master spark://10.21.208.21:7077 --deploy-mode client"
```
- 配置Ipython notebook server
    + *ipython profile create pyspark*
    + 编辑 *ipython_notebook_config.py*
    + [可选]配置ipython notebook登录密码
    + 设置启动文件
- 设置启动脚本    


## 4. next

下一篇总结一下一些 spark 应用优化的小技巧吧。

## 5. 打开微信，扫一扫，点一点，棒棒的，^_^

![wechat_pay_6-6.png](../images/wechat_pay_6-6.png)



## 本系列文章链接

- [『 Spark 』1. spark 简介 ](http://litaotao.github.io/introduction-to-spark?s=inner)
- [『 Spark 』2. spark 基本概念解析 ](http://litaotao.github.io/spark-questions-concepts?s=inner)
- [『 Spark 』3. spark 编程模式 ](http://litaotao.github.io/spark-programming-model?s=inner)
- [『 Spark 』4. spark 之 RDD ](http://litaotao.github.io/spark-what-is-rdd?s=inner)
- [『 Spark 』5. 这些年，你不能错过的 spark 学习资源 ](http://litaotao.github.io/spark-resouces-blogs-paper?s=inner)
- [『 Spark 』6. 深入研究 spark 运行原理之 job, stage, task](http://litaotao.github.io/deep-into-spark-exection-model?s=inner)
- [『 Spark 』7. 使用 Spark DataFrame 进行大数据分析](http://litaotao.github.io/spark-dataframe-introduction?s=inner)
- [『 Spark 』8. 实战案例 ｜ Spark 在金融领域的应用 ｜ 日内走势预测](http://litaotao.github.io/spark-in-finance-and-investing?s=inner)
- [『 Spark 』9. 搭建 IPython + Notebook + Spark 开发环境](http://litaotao.github.io/ipython-notebook-spark?s=inner)
- [『 Spark 』10. spark 应用程序性能优化｜12 个优化方法](http://litaotao.github.io/boost-spark-application-performance?s=inner)
- [『 Spark 』11. spark 机器学习](http://litaotao.github.io/spark-mlib-machine-learning?s=inner)
- [『 Spark 』12. Spark 2.0 特性介绍](http://litaotao.github.io/spark-2.0-faster-easier-smarter?s=inner)
- [『 Spark 』13. Spark 2.0 Release Notes 中文版 ](http://litaotao.github.io/spark-2.0-release-notes-zh?s=inner)
- [『 Spark 』14. 一次 Spark SQL 性能优化之旅](http://litaotao.github.io/spark-sql-parquet-optimize?s=inner)