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





# SQL

- ***Multiple Apartments***: write a sql to get a list of tenants who are renting more than one apartment.

```sql
select tenantName 
	from tenants
	inner join (
		select tenantID from aptTenants group by tenantID having count(*) > 1
	) c
	on tenants.TenantID = c.tenantID;
```

- ***Open requests***: write a sql to get a list of all buildings and the number of open requests( requests in which status equals 'open')

```sql
select buildingName, ISNULL(count, 0) as 'count'
	from buildings
	left join (
    	select apartments.buildingID, count(*) as 'count'
      		from requests inner join apartments
      		on requests.aptID = apartments.aptID
      		where requests.status = 'open'
      		group by apartments.buildings
    ) reqCounts
on reqCounts.buildingID = buildings.buildingID;
```

- ***close all requests***: building #11 is undergoing a major renovation, inplement a query to close all requests from apartments in this building.

```sql
update requests
set status = 'closed'
where aptID in (select aptID from apartments where buldingID = 11);
```

- ***joins***: what are the different types of joins? please explain how they differ and why certain types are better in certain situations.

```
join is used to combine the results of two tables. to perform a join, each of the tables must have at least one field that will be used to find matching records from the other table. the join type defines which records will go into the result set.

there are several join types: inner, outer, left outer, right outer, full outer;
```

- ***denormalization***: what is denormalization and explain pros and cons.

```

```









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
- ***Add without plus***: Write a function that adds two numbers, you should not user + or any arithmetic operators.
- Inplement count_words(input_str) function which returns number of words from the input string (hint the edge cases they provide means you have to implement it manually).
- implement count_substr(input_str, sub_str) function which returns the number of times the sub_str occurs in the input_str.
- 给定一个有序数组，除了一个元素出现一次以外其他元素均出现两次，请找到这个只 出现一次的元素，要求O(logn)的时间复杂度和O(1)的空间复杂度。


```python
"""
异或操作，最快 O(logN)，是否有序没有关系
"""

def xor(a, b):
    c = a ^ b
    print '{}: {:0>8}'.format(a, bin(a)[2:])
    print '{}: {:0>8}'.format(b, bin(b)[2:])
    print '{}: {:0>8}'.format(c, bin(c)[2:])
    
    print '{} ^ {} = {}'.format(a, b, c)
    return

def find_one(_list):
    """pre vs next; o(n), o(1)
    cases:
    0 1 1 2 2 
    0 0 1 2 2
    0 0 1 1 2
    """
    ### checking
    
    ### core
    pre, current = _list[0], _list[1]
    
    if pre != current:
        return pre
    
    for i in range(2, len(_list)):
        pre = current
        current = _list[i]
        
        if pre != current:
            if i+1 != len(_list) and _list[i+1] != current:
                return current
            elif i+1 == len(_list):
                return current
            else:
                continue
        else:
            continue
```



- ***Spiral Matrix***: Given a matrix of *m* x *n* elements (*m* rows, *n* columns), return all elements of the matrix in spiral order.

```python

def print_spiral_matrix(matrix, x, y):
    """还不对哦
    """
    #  //左右上下四个边界
    left = 0
    right = x - 1
    top = 0
    bottom = y - 1

    while (True):
#         print 'left, right, top, bottom: ', left, right, top, bottom
        
        # //上边，自左至右
        for i in range(left, right + 1):
            print matrix[top][i]

        top += 1
        if (top > bottom):
            break

        # //右边，自上至下
        for i in range(top, bottom + 1):
            print matrix[i][right]

        right -= 1
        if (left > right):
            break

        # //下边，自右至左
        for i in range(right , left, -1):
            print matrix[bottom][i]
            
        bottom -= 1
        if (top > bottom):
            break

        # //左边，自下至上
        for i in range(bottom , top, -1):
            print matrix[i][left]
            
        left += 1
        if (left > right):
            break
            
def build_spiral_matrix(n):
    """生成一个螺旋矩阵，同样也是有问题的哦
    """
#     a = [ [0] * n ] * n
    a = [ [0 for i in range(n)] for j in range(n) ]
    
    def spiral_matrix(matrix, x, y, start, n):        
        if n <= 0:
            return 
    
        if n == 1:
            matrix[x][y] = start
            return
        
        for i in range(x, x+n):
            matrix[y][i] = start
            start += 1
        
        for i in range(y, y+n):
            matrix[i][x+n-1] = start
            start += 1
            
        for i in range(x+n-1, x-1):
            matrix[y+n-1][i] = start
            start += 1
            
        for i in range(y+n-1, y-1):
            matrix[j][x] = start
            start += 1
        
        spiral_matrix(a, x+1, y+1, start, n-2)
        
    spiral_matrix(a, 0, 0, 0, n)
    
    return a
```



- What is Tail Call and Tail Recursive ? 
  - [尾调用优化](http://www.ruanyifeng.com/blog/2015/04/tail-call.html)


​	



# Data Engineer

- Do you have experience with data modeling? If so, what data modeling tools do you have experience using?



# System Conprehension and Design

- ***Social Network***: how would you design the data structures for a very large social network like facebook or linkedin? describe how you would design an algorithm to show the shortest path between two people( e.g. me -> bob -> susan -> jason -> you)
- ***Web crawler***: if you were designing a web crawler, hwo would you avoid getting into infinite loops?
- ***Personal financial manager***: how would you design a personal financial manager. this system would connect to your back accounts analyze your spending habits, and make recommendations.
- ***Thread vs Process***: what's the difference between a thread and a process?
- ​







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

- ***The apocalypse***: in the new post-apocalytic world, the queen is desperately concerned about the birth rate. therefore she decided that all families should ensure that they have one girl or else they face massive fines. if all families abide by this policy — that is, they have continue to have children until they have one girl, at which point they immediately stop — what will the gender ratio of the new generation be? assume that the odds of someone having a boy or a girl on any given pregnancy is equal. solve this out logically and then write a computer simulation of it.

- ***The egg drop problem*** : there is a building of 100 floors, if an egg drops from the Nth floor or above, it will break, if it's dropped from any floor below, it will not break. You're given two eggs. Find N, while minimizing the number of drops for the worst case.

  - step by step, first find a general way to find N, and then find a way to minimize the number of drops;

- ***100 lockers***: there are 100 closed lockers in a hallway. a man begins by opening all 100 lockers, next, he closes every second locker. then, on this third pass, he toggles every third locker ( closes it if it is open or opens it if it is closed ). this process continues for 100 passes, sunch that on each pass i, the man toggles every with 'ith' locker, after his 100th pass in the hallway, in which he toggles only locker #100, how many lockers are open?

- ***Posion***: You have 1000 bottles of soda, and exactly one is poisoned. you have 10 test strips which can be used to detect poison. a gingle drop of poison will turn the test strip positive permanently. You can put any number of drops on a test strip at once and you can reuse a test strip as many times as you'd like (as long as the results are negative). however you can only run tests once per day and it takes seven days to return a result. how would you figure out the poisoned bottle in as few days as possible? write code to simulate your approach.

- ***Moral***: What is your biggest weakness?

- ***Open***: Why should we hire you to this job?

  - Skills, experience, personality; energy and passion;

- ***Open***: Do you have any questions to ask us?

  - interview/talk feedback; daily job if joined; team-members;



  	

- ​


  ​			
  ​		
  ​	





# Resource



- https://www.careercup.com/
- https://www.careercup.com/resume
- http://rosettacode.org/wiki/Rosetta_Code
- http://visualgo.net
- https://github.com/gatieme/CodingInterviews
- ​

