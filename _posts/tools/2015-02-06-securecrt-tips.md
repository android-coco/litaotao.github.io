---
category: tools
published: false
layout: post
title: SecureCRT 使用和技巧
description: 我在使用SecureCRT过程中遇到的问题及解决办法。 
---  


##
## 1. 方向键出现乱码问题

解决办法： 
Options-》session options -》Terminal-》Emulation-》Modes中，去掉CurSor key mode的选择即可。

## 2. PS1配置

　　这不属于SecureCRT的技巧，但也放在这里吧，配置环境变量PS1，用起来更和谐。 

```
export PS1="\[\033[01;31m\]\u\[\033[00m\]@\[\033[01;32m\]\h\[\033[00m\][\[\033[01;33m\]\t\[\033[00m\]]:\[\033[01;34m\]\w\[\033[00m\]#"
```

效果：

```
root@ubuntu2[17:26:50]:~/Desktop#ll
total 25M
drwxr-xr-x  3 root root 4.0K Feb 25  2014 anaconda_1.9.1_20140225
-rw-r--r--  1 root root  24M Jun 16  2014 anaconda_1.9.1_20140225.tar.gz
drwxr-xr-x  3 root root 4.0K Jan 21 19:24 blog
drwxr-xr-x  4 root root 4.0K Jan 19 18:02 community
-rw-r--r--  1 root root  621 Dec 18 15:55 company_hive.bashrc
-rw-r--r--  1 root root  376 Feb  6 17:26 company_spark_1.2.0.bashrc
-rw-r--r--  1 root root  234 Jan 28 15:15 company_spark.bashrc
```

## 3. vim配置
　　一次在secureCRT里启动vim编辑源代码的时候发现tab键是8个空格，想设置成4个空格，我还莫名其妙地在secureCRT的Options里找了半天，后来才反应过来这应该是系统vim的配置，果不其然，在这篇博客里找到了vim的详细配置。[link](http://blog.sina.com.cn/s/blog_544f18310100iim0.html)

## 4. SecureCRT 信号灯设置
　　session option选中Terminal的Anti-idle框中Send protocol NO-OP复选框后面的秒默认60就可以了。

## 扫一扫     

![2015-02-06-securecrt-tips.md](../../images/share/2015-02-06-securecrt-tips.md.jpg)