---
layout: post
published: false
title: ［touch spark］8. 当Ipython Notebook遇见Spark  
description: 首先我忠心地感谢Ipython，Spark的开源作者，真心谢谢你们开发这么方便，好用，功能强大的项目，而且还无私地奉献给大众使用。刚刚很轻松地搭建了一个机遇Ipython Notebook的Spark客户端，真的感受到 The power of technology, the power of open source.
---  


##  
## 1. 致谢   
　　首先我忠心地感谢Ipython，Spark的开源作者，真心谢谢你们开发这么方便，好用，功能强大的项目，而且还无私地奉献给大众使用。刚刚很轻松地搭建了一个机遇Ipython Notebook的Spark客户端，真的感受到 The power of technology, the power of open source.  
　　下面是这两个项目的github地址：  

- [Ipython](https://github.com/ipython/ipython)  
- [Spark](https://github.com/apache/spark)  

　　同时，这篇文章在刚开始的部分，参考了很多 [这篇博客](http://blog.cloudera.com/blog/2014/08/how-to-use-ipython-notebook-with-apache-spark/)的内容，感谢这么多人能无私分享如此高质量的内容。   
　　但是，这篇文章不是简单记录怎么做，我尽量做到量少质高，所以有些地方会说得比较详细，其中也会提到在解决遇到的问题上的一些方法和思路。

## 2. 路线规划   
　　基于 [Databricks](http://www.databricks.com/)，[Zeppelin](zeppelin-project.org) 和 [Hue](www.gethue.com) 的启发，我也想尝试搭建一个丰富可用的在线大数据REPL分析平台，正好用此机会好好实践一下spark，毕竟都学习spark几个月了呢。   
　　不说废话，同[使用spark分析微博数据那篇博文一样](../weibo-api-in-action)，我们也要有一个路线规划：  

- 搭建一个可多用户使用的，底层接入了spark集群的Ipython Notebook Server；  
- 完善 Weibo Message Driver，使用户可在Notebook里获取、分析微博数据，as simple as possible；  
- 研究Zeppelin和Hue项目，把其中一个嫁接在Notebook的上层，实现准产品级的大数据实时ETL，Analytic，Sharing平台；这一步可能需要较长时间，可根据自己的时间安排灵活调整；  

　　Dream：在年前完成上面三步，that's really full or chanllenge, but more funny. **Anyway, we need dreams, and I can't wait to make this dream into reality.**

![dreams](../images/dreams.jpg)

　　这篇主要记录我在实现第一步的过程中遇到的主要步骤，遇到的问题和解决方法：搭建一个可多用户使用的，底层接入了spark集群的Ipython Notebook Server。

## 3. 配置Ipython  

### 3.1: ipython 配置名profile介绍 
- profile 命令说明    

　　profile是ipython的一个子命令，其中profile又有两个子命令，分别是create和list，顾名思义，create就是创建一个配置文件，list就是列出当前配置文件。如下：  

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

- profile子命令list说明    

　　本想list命令应该很简单的，和linux下的ls差不多嘛，但我自己看了下，其中还是有些细节值得推敲的。其中这项 `Available profiles in /root/.config/ipython:` 是说目前有两个配置文件在那个目录下面，pyspark是我自己创建的了。在参考的[这篇文章](http://blog.cloudera.com/blog/2014/08/how-to-use-ipython-notebook-with-apache-spark/)中，作者说创建的配置文件会放到 ` ~/.ipython/profile_pyspark/` 下，其实这并不是一定的，具体放在哪个目录下面，可以根据profile list的命令来查看。如此看来，我们在这台机器上创建的配置文件应该是放在目录 `/root/.config/ipython` 下面的。

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

- profile子命令create说明    

　　简单介绍下create子命令的用法。

    Create an IPython profile by name

    Create an ipython profile directory by its name or profile directory path.
    Profile directories contain configuration, log and security related files and
    are named using the convention 'profile_<name>'. By default they are located in
    your ipython directory. Once created, you will can edit the configuration files
    in the profile directory to configure IPython. Most users will create a profile
    directory by name, `ipython profile create myprofile`, which will put the
    directory in `<ipython_dir>/profile_myprofile`.

### 3.2 创建新的Ipython配置文件    
- 创建配置文件     

　　因为我之前已经配置过一个pyspark的配置文件了，这里我们创建一个测试用的配置文件，pytest。运行一下命令后，会在 `/root/.config/ipython` 下生成一个 pytest的目录。

    root@ubuntu2[14:54:14]:~/Desktop#ipython profile create pytest
    [ProfileCreate] Generating default config file: u'/root/.config/ipython/profile_pytest/ipython_config.py'
    [ProfileCreate] Generating default config file: u'/root/.config/ipython/profile_pytest/ipython_notebook_config.py'

    root@ubuntu2[15:00:57]:~/Desktop#ls ~/.config/ipython/profile_pytest/
    ipython_config.py  ipython_notebook_config.py  log  pid  security  startup 

