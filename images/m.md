# Python

```
说说自己常常用到的模块及其作用 
```

```
list/dict comprehension（列表/字典推导） 
```

```
如何设置带默认值的字典，并比较其优缺点 
```

```
简述python中的多线程，多进程，协程及其实现
```

```
简述何谓函数式编程
```

```
说说常用的python内置函数，越多越好，并举几个使用的例子
```

```
谈谈 Python的__name__变量
```

```
说说python 中 sequence、string、dic、tuple的常用方法，比如分片，排序等
```

```
如何多种方式在Python里输出一个Fibonacci数列？
```

```
Python中pass语句的作用是什么？ pass语句什么也不做，一般作为占位符或者创建占位程序，pass语句不会执行任何操作
```

```
如何知道一个python对象的类型？ type()	
```

```
python里面正则表达式的search()和match()的区别？ match()函数只检测RE是不是在string的开始位置匹配，search()会扫描整个string查找匹配, 也就是说match()只有在0位置匹配成功的话才有返回，如果不是开始位置匹配成功的话，match()就返回none
```

```
如何用Python删除一个文件？ 使用os.remove(filename)或者os.unlink(filename);
```

```
如何拷贝一个对象？
```

```
 Python的函数参数传递
```

```
Python中的元类(metaclass)
```

```
@staticmethod和@classmethod
```

```
类变量和实例变量
```

```
Python自省
```

```
Python中单下划线和双下划线

__foo__:一种约定,Python内部的名字,用来区别其他用户自定义的命名,以防冲突.

_foo:一种约定,用来指定变量私有.程序员用来指定私有变量的一种方式.

__foo:这个有真正的意义:解析器用_classname__foo来代替这个名字,以区别和其他类相同的命名.

详情见:http://stackoverflow.com/questions/1301346/the-meaning-of-a-single-and-a-double-underscore-before-an-object-name-in-python

或者: http://www.zhihu.com/question/19754941
```

```
字符串格式化:%和.format
```

```
迭代器和生成器
```

```
*args and **kwargs
```

```
面向切面编程AOP和装饰器
```

```
到底什么是Python？你可以在回答中与其他技术进行对比（也鼓励这样做）。

解释型，动态类型，oop，函数是第一阶级，方便，生态完善，胶水语言；
```

```
“猴子补丁”（monkey patching）指的是什么？这种做法好吗？	
```

```
下面这些是什么意思：@classmethod, @staticmethod, @property？
```

```
简要描述Python的垃圾回收机制（garbage collection）。

Python在内存中存储了每个对象的引用计数（reference count）。如果计数值变成0，那么相应的对象就会消失，分配给该对象的内存就会释放出来用作他用。
偶尔也会出现引用循环（reference cycle）。垃圾回收器会定时寻找这个循环，并将其回收。举个例子，假设有两个对象o1和o2，而且符合o1.x == o2和o2.x == o1这两个条件。如果o1和o2没有其他代码引用，那么它们就不应该继续存在。但它们的引用计数都是1。
Python中使用了某些启发式算法（heuristics）来加速垃圾回收。例如，越晚创建的对象更有可能被回收。对象被创建之后，垃圾回收器会分配它们所属的代（generation）。每个对象都会被分配一个代，而被分配更年轻代的对象是优先被处理的。
```









# Shell



```shell
简述shell中的各种循环，以读取一个文件内容为例:

for i in `cat a.txt`;do echo "$i";done

while read i ;do echo "$i";done < a.txt
```



```shell
查找目录下修改时间超过7天的文件及目录，并删除:
 
find . -mtime +7 -type f -exec rm {} \;
find . -mtime +7 -type d -exec rmdir {} \;

点评： 
1） 能说出+7 & -7 区别的，说明是个熟练的运维操作人员；
2） 能说出-mtime, -atime -ctime 的区别的，说明对Linux 文件系统体系很熟悉；
```



```shell
字符如何进行替换？如： /etc/zabbix/zabbix_agentd.conf 如何取出etc以及zabbix_agentd 

echo "/etc/zabbix/zabbix_agentd.conf" |awk -F/ '{print $2,$4}'|sed -e 's/\.conf//'

点评：
1） sed 和 awk 是必须知道，并且能掌握的基本命令；
2） sed 和 awk 的掌握主要取决于正则表达式的熟练程度，引申出来的问题： 在正则表达式，什么是贪婪匹配，什么是非贪婪匹配？
```



```shell
（A）如有一个文本：  13800000000  13800000000  15800000000  17300000000  15600000000  18900000000  18900000000  请用尽可能多的方法来进行去重   

sort a.txt |uniq
cat a.txt |while read i;do set[$i]=1;echo "${!set[@]}";done|tail -1
 
点评：
1) sort 和uniq 是比较常用的工具，希望能掌握；
2）在shell 中写for 是件耗时的工作，所以尽量去用shell 中已有的程序和命令实现一些简单功能；
```

```
（A）特殊变量$@ $# $? $*的值？ 
 答案
http://www.thelinuxtips.com/2011/02/shell-special-variables/
```









# Spark







# Finance



# Algorithm



# Open-Minded







# Resource



- https://www.careercup.com/
- ​