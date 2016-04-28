---
category: python
published: false
layout: post
title: Python 技巧总结
description: Python 技巧总结~
---



## 1. [eval in python](http://drops.wooyun.org/tips/7710)

## 2. 时间格式转换
![python-time.jpg](../images/python-time.jpg)

## 3. 带任意数量参数的函数

显示使用 `*args, **kwargs`，不重复造轮子了，[click here](http://www.cnblogs.com/fengmk2/archive/2008/04/21/1163766.html)

## 4. 使用 ispect 进行调试

## 5. 使用 uuid 生成唯一ID

## 6. 使用 json 序列化

## 7. 使用 atexit 注册 Shutdown 函数 

## 8. 指定 pip 源

国内 pip 源：

>>
http://pypi.douban.com/ 豆瓣
http://pypi.v2ex.com/simple V2EX
http://pypi.hustunique.com/ 华中理工大学
http://pypi.sdutlinux.org/ 山东理工大学
http://pypi.mirrors.ustc.edu.cn/ 中国科学技术大学

- 手动指定

{% highlight python %}

pip install package_name -i http://pypi.v2ex.com/simple

{% endhighlight %}

- 修改配置文件

配置文件路径: `~/.pip/pip.conf`

{% highlight python %}

[global]
index-url = http://pypi.douban.com/simple

{% endhighlight %}

## 参考文档
- [Python中eval带来的潜在风险](http://drops.wooyun.org/tips/7710)
- [Python奇技淫巧](http://andrewliu.in/2015/11/14/Python%E5%A5%87%E6%8A%80%E6%B7%AB%E5%B7%A7/)
- [Pandas透视表（pivot_table）详解](http://python.jobbole.com/81212/)
- [你需要知道的、有用的 Python 功能和特点](http://www.oschina.net/translate/python-functions)
- [Python tips: 什么是*args和**kwargs？](http://www.cnblogs.com/fengmk2/archive/2008/04/21/1163766.html)
- [Python-pip源](http://xunhou.me/python-pip/)






