---
layout: post
published: false
title: ［touch spark］8. 当Ipython Notebook遇见Spark 1， 安装配置篇 
description: 首先我忠心地感谢Ipython，Spark的开源作者，真心谢谢你们开发这么方便，好用，功能强大的项目，而且还无私地奉献给大众使用。刚刚很轻松地搭建了一个机遇Ipython Notebook的Spark客户端，真的感受到 The power of technology, the power of open source.
---  

注：和本文相关的资料和文件都放到Github上了：[ipython-notebook-spark](https://github.com/litaotao/ipython-notebook-spark)


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

- 因为考虑到公司的data scientist很喜欢R，所以也在我们的ipython notebook环境里加入r kernel；
- 搭建一个可多用户使用的，并且各个用户互相独立的环境［至少让用户A不能读取到用户B的文件吧］； 
- 结合丰富的开源包，能做到在线，实时的数据分析和共享分析报告； 
- 底层接入了spark集群，支持在notebook做基于spark对大数据分析；  


　　Dream：在国庆前完成至少前3步，that's really full or chanllenge, but more funny. **Anyway, we need dreams, and I can't wait to make this dream into reality.**

![dreams](../images/dreams.jpg)

　　这篇主要记录我在实现第一步的过程中遇到的主要步骤，遇到的问题和解决方法：搭建一个可多用户隔离使用的，能做丰富的大数据在线分析和分享对，并且底层接入了spark集群的Ipython Notebook Server。


## 3. 安装Ipython 

　　使用 `sudo pip install ipython==3.2.0` 来安装ipython 3.2.0 版本，本来打算用和jupyter分离后的ipython 4.0.0的，但是一下子要配置ipython和jupyter，赶紧有点乱，而且ipython 4.0.0 似乎也仅仅是吧notebook分离到jupyter，并没有什么大的改动，所以就先用3.2.0了，短期内应该不会有升级的安排。

　　安装好之后试试运行下 ipython，看看似乎有错，如果出现下面的错误的话，把 `/usr/local/lib/python2.7/dist-packages/IPython/external/path/__init__.py` 里的 `from path import *` 改成 `from _path import *` 即可。   

```
Traceback (most recent call last):
  File "/usr/local/bin/ipython", line 7, in <module>
    from IPython import start_ipython
  File "/usr/local/lib/python2.7/dist-packages/IPython/__init__.py", line 45, in <module>
    from .config.loader import Config
  File "/usr/local/lib/python2.7/dist-packages/IPython/config/__init__.py", line 6, in <module>
    from .application import *
  File "/usr/local/lib/python2.7/dist-packages/IPython/config/application.py", line 19, in <module>
    from IPython.config.configurable import SingletonConfigurable
  File "/usr/local/lib/python2.7/dist-packages/IPython/config/configurable.py", line 14, in <module>
    from IPython.utils.text import indent, wrap_paragraphs
  File "/usr/local/lib/python2.7/dist-packages/IPython/utils/text.py", line 28, in <module>
    from IPython.external.path import path
ImportError: cannot import name path
```


## 3. 配置Ipython  

### 3.1: ipython 配置名profile介绍 
- profile 命令说明    

　　profile是ipython的一个子命令，其中profile又有三个子命令，分别是locate，create和list，顾名思义，create就是创建一个配置文件，list就是列出当前配置文件。如下：  

```
aaron@dev-chad:~/ipython-notebook-spark$ipython profile
Subcommands
-----------

Subcommands are launched as `ipython profile cmd [args]`. For information on
using subcommand 'cmd', do: `ipython profile cmd -h`.

locate
    print the path to an IPython profile dir
create
    Create an IPython profile by name
list
    List available IPython profiles
```

### 3.2 创建新的Ipython配置文件    
- 创建配置文件     

```
    aaron@dev-chad:~/ipython-notebook-spark$ipython profile create bigdata
    [ProfileCreate] Generating default config file: u'/home/aaron/.ipython/profile_bigdata/ipython_console_config.py'
    [ProfileCreate] Generating default config file: u'/home/aaron/.ipython/profile_bigdata/ipython_notebook_config.py'
    [ProfileCreate] Generating default config file: u'/home/aaron/.ipython/profile_bigdata/ipython_nbconvert_config.py'
```

### 3.3 编辑配置文件
- 编辑ipython_notebook_config.py   

```
    c = get_config()
    
    c.NotebookApp.ip = '*'

    # 本想指定每次都在一个专有的目录启动notebook server的，可是这样设置还是不行，这样设置后每次打开启动notebook server 的路径是
    # 当前路径 ＋ u'home/aaron/notebooks'，完全达不到我想要的效果，所以暂时注释啦。
    # c.NotebookApp.notebook_dir = u'home/aaron/notebooks'

    c.NotebookApp.open_browser = False

    c.NotebookApp.port = 8880 # or whatever you want, make sure the port is available  

    # 
    # c.NotebookApp.pylab = 'inline' 已经被弃用了，官方推荐在notebook中显示指定，不过下面的这个配置依然可以使用的，
    # 我的建议是，先这样使用，然后在以后写到启动的配置文件里去，并且在每一个新建的 notebook 中都能有显式说明。
    c.IPKernelApp.matplotlib = 'inline'
```

- 设置访问密码   

　　如果你的notebook server是需要访问控制的，简单的话可以设置一个访问密码。听说Ipython 2.x 版本有用户访问控制，这里我还没有接触过，晚点会看看是否有成熟的可用的用户控制方案。

    + 生成密码文件  
    这里我们用python自带的密码包生成一个密码，然后再把这个密码重定向到nvpasswd.txt文件里。注意这里重定向的路径哦。
    + 编辑配置文件，设置读取密码文件配置项
    这里有一个需要注意的，就是PWDFILE的设置，一开始我设置为 `~/.config/ipython/profile_pytest/nbpasswd.txt`，但是启动ipython notebook server的时候老师报错，说找不到密码文件nbpasswd.txt，很奇怪，明明文件就是在的，可就是提示找不到。无奈我到nbpasswd.txt路径下用 pwd 打印当前路径，显示为 `root/.config/ipython/profile_pytest/nbpasswd.txt`，可是这两个路径应该是一样的啊。无奈之下，死马当作活马医，我就把PWDFILE设置成为 `root/.config/ipython/profile_pytest/nbpasswd.txt`，没想到这样还成功了。关于这点为什么会有效，目前我还不是很清楚，等我请教了公司大神后再补上这一个tip吧。
      
    示例如下：  

```
aaron@dev-chad:~/ipython-notebook-spark$python -c 'from IPython.lib import passwd; print passwd()'
Enter password:
Verify password:
sha1:eee72d659d34:bc7cf7fc26700b28eaa16bb8a8ce846fa35084de

root@ubuntu2[09:49:09]:~/Desktop#vi /root/.config/ipython/profile_pytest/ipython_notebook_config.py 

c.NotebookApp.password = u'sha1:eee72d659d34:bc7cf7fc26700b28eaa16bb8a8ce846fa35084de'  # copy your encoded password here 
```

- 设置启动文件  

　　这个设置非常好用，在每个ipython的配置路径下，都有一个startup的文件夹，里面你可以写一些脚本，这些脚本都是在启动ipython notebook server之前被执行的，并且是全局的。有两个好处：

- 脚本的执行是有序的，具体可以参考下面的写法文档   
- 影响是全局的，也就是说如果你在一个脚本里定义了一个变量a，那在所有新建的notebook中这个变量a都是已经创建了的；但这也许也是一个缺点吧，anyway，看你怎么用了；

```
This is the IPython startup directory

.py and .ipy files in this directory will be run *prior* to any code or files specified
via the exec_lines or exec_files configurables whenever you load this profile.
Files will be run in lexicographical order, so you can control the execution order of files
with a prefix, e.g.::
    00-first.py
    50-middle.py
    99-last.ipy
```

　　原本打算在启动文件里写入一些package import和设置相关的脚步的，但是我想这样的话会造成一些误解，特别是当你分享notebook的时候，别人都不知道你事先导入了哪些package，会让人感到很迷惑。而且，我认为在每一个notebook的第一个cell里把改notebook里所需要的package和package setting注明是一个非常好的习惯，所有启动脚本就先不用了。   


## 3. 安装R, 配置IRkernel

　　关于如何安装R，请参考：[https://mirrors.tuna.tsinghua.edu.cn/CRAN/](https://mirrors.tuna.tsinghua.edu.cn/CRAN/)
　　关于如何安装配置IRkernel，请参考：[https://github.com/IRkernel/IRkernel](https://github.com/IRkernel/IRkernel)
　　好吧，我承认了，我现在这台服务器上之前就有人装过R和IRkernel了，具体怎么配置我也不想花时间去研究，因为实在不喜欢R，不要问我为什么不喜欢。“喜欢一个人不需要理由”，不喜欢一个东西有时候也不需要理由啊～



## 4. 总结

　　好了，环境算是基本搭建好了，github还没怎么更新，因为不能把公司相关的信息透露出来，所以commit的时候都需要谨慎一点。下一步，我们就来看看怎么让多个用户有个独立的 IPython 开发环境吧。


![a-good-start.jpg](../images/a-good-start.jpg)






## 扫一扫     

![2015-01-27-ipython-notebook-server-spark.md](../../images/share/2015-01-27-ipython-notebook-server-spark.md.jpg)