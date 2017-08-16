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

- Fibonacci code

```python
def fib(n):
    """ O(2 ^ n) """
    if n < 0:
        return -1 
    elif n == 0:
        return 1
    else:
        return fib(n-2) + fib(n - 1)

def fib_v2(n):
    """ O(n) """
    a = [0, 1] + [0] * (n - 2)
    for i in range(2, n):
        a[i] = a[i-1] + a[i-2]
    return a
```



- permutations

```python
## method 1

def to_string(_list):
    return ''.join(_list)

def permute(a, l, r):
    """ O(n * n!) 
    a: string
    l: starting index of the string
    r: ending index of the string
    """
    if l == r:
        print to_string(a)
    else:
        for i in xrange(l, r+1):
            print i, l
            print a[l], a[i]
            
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l]
            
## method 2
def permute_v2(a):
    import itertools
    for values in itertools.permutations(a):
        print values
        
```



- ***Is Unique*** Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

- ***Check Permutation*** : Given two strings, write a method to decide if one is a permutation of the other.

- ***URLify*** : Write a method to replace all spaces in a string with `%20`,  You may assume that the string
  has suffcient space at the end to hold the additional characters, and that you are given the "true"
  length of the string. (Note: if implementing in Java, please use a character array so that you can
  perform this operation in place.)

- ***Palindrome Permutation***: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

- ***One Away***: There are three types of edits that can be performed on strings: insert a character,remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.


  ​			
  ​		
  ​	

- 
  ​
  ​	



​	



# Open-Minded



- Why do you want to work for our company?

- Self-introduction: current role simple -> college -> post college -> current role details -> outside of work -> wrap up

- How to solve a problem?

  - A problem-solving flowchart: listen -> example -> brute force -> optimize -> walk through -> implement -> test;

- ***The Hea  Pill***: You have 20 bottles of pills. 19 bottles have 1.0 gram pills, but one has pills of weight 1.1 grams. Given a scale that provides an exact measurement, how would you  nd the heavy bottle? You can only use the scale once.

- ***Basketball***: You have a basketball hoop and someone says that you can play one of two games.

  Game 1: You get one shot to make the hoop.

  Game 2: You get three shots and you have to make two of three shots.

  If p is the probability of making a particular shot, for which values of p should you pick one gameor the other?

- ***Dominos***: There is an 8x8 chessboard in which two diagonally opposite corners have been cut off. You are given 31 dominos, and a single domino can cover exactly two squares. Can you use the 31 dominos to cover the entire board? Prove your answer (by providing an example or showing why it's impossible).

- ***Ants on a Triangle***: There are three ants on different vertices of a triangle. What is the probability ofcollision (between any two or all of them) if they start walking on the sides of the triangle? Assumethat each ant randomly picks a direction, with either direction being equally likely to be chosen, andthat they walk at the same speed. Similarly,  nd the probability of collision with n ants on an n-vertex polygon.

- ***Jugs of Water***: You have a  five-quart jug, a three-quart jug, and an unlimited supply of water (but no measuring cups). How would you come up with exactly four quarts of water? Note that the jugs are oddly shaped, such that  lling up exactly "half" of the jug would be impossible.

  - 4 = 5 -1 = 3 + 1 = 2 x 2 = 1 x 4, so the core of this problem is to find 1 quart of water, maybe.
  - answer: 5 - 3 = 2; 2->3; 3 - 2 = 1; 5 - 1 = 4;
  - actually, using a 5 quart, and 3 quart jug, we can get 1,2,3,4,5,6,7,8 quart water as we want; core is 1 quart;	

- ***blue-eyed people***: a bunch of people live in an island; one day they receive an order: all blue-eyed people must leave the island. there will be a flight out at 8:00 pm every evening. each people can see others' eye color, but they do not know theirs. additionally, they do not know how many blue-eyed people among them, just only know at least one people does. how many days will it take the blue-eyed people to leave?

- ​


  ​		
  ​	

- ​


  ​			
  ​		
  ​	





# Resource



- https://www.careercup.com/
- https://www.careercup.com/resume
- http://rosettacode.org/wiki/Rosetta_Code
- ​

