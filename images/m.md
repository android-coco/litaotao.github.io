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
http://blog.willdx.me/2016/07/31/python%E9%AD%94%E6%B3%95%E6%96%B9%E6%B3%95%E4%B8%93%E9%A2%9801-GIL-%E5%A4%9A%E7%BA%BF%E7%A8%8B-%E5%A4%9A%E8%BF%9B%E7%A8%8B-%E5%8D%8F%E7%A8%8B-%E5%AE%88%E6%8A%A4%E8%BF%9B%E7%A8%8B/
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
http://www.firefoxbug.com/index.php/archives/2818/
```

```
类变量和实例变量
```

```
Python自省：http://www.cnblogs.com/huxi/archive/2011/01/02/1924317.html
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

- what is flask and the difference between django, pyramid?
- async programming: 
  - coroutine
  - multi-thread
  - multi-process
  - asyncio
  - gevent
  - uvloop [awesome repo], pyuv
  - celery
- python theory


> Simple is better than complex, complex is better than complicated;
>
> readability counts;
>
> errors should never pass silently;
>
> FP and OO in python is on the same level of importance;
>
> 



# Shell

```shell
file: cat, head, tail, echo, cp, touch, rm, grep, find, locate, wc, scp, wget,
folder: ls, du, rm, mkdir, tar, 
env: export, source, 
process: ps, netstat, htop, kill, gdb, nohup, pstree
```



```
nohup: https://www.ibm.com/developerworks/cn/linux/l-cn-nohup/index.html
pstree: http://www.runoob.com/linux/linux-comm-pstree.html


提供回测数据缓存机制

难点：
- 数据同步，依赖各种数据源，处理好依赖情况，DAG 方式进行调度；
- 数据校验和检测，监控报警，性能级别的监控；
- 因子量多，且互相之间有所依赖，采用多进程模式生产，进程间状态共享；
- 量化因子算法细节问题，异常值，缺失值，TTM 算法，PIT 处理；
```



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
- [2017.10 | 10 SQL Tricks That You Didn’t Think Were Possible](https://blog.jooq.org/2016/04/25/10-sql-tricks-that-you-didnt-think-were-possible/)


> 1. Everything is a table (derived table);
> 2. data generation with recursive SQL;
> 3. running total calculations: window functions are aggregations/ranking on a subset of rows relative to the current row being transformed by select;
> 4. finding the largest series with no Gaps; `with` statements, `cast` keyword, `row_number` window function,
> 5. finding the length of a series
> 6. the subset sum problem with sql
> 7. capping a running total
> 8. time series pattern recognition
> 9. pivoting and unpivoting
> 10. abusing xml and json

- [2017.10 | Why Uber Engineering Switched from Postgres to MySQL](https://eng.uber.com/mysql-migration/)

> The early architecture of Uber consisted of a monolithic backend application written in Python that used [Postgres](http://www.postgresql.org/) for data persistence.
>
> postgres limitations in uber: inefficient architecture for writes; inefficient data replication; issues with table corruption; poor replica MVCC support; difficulty upgrading to newer releases;
>
> Postgres served us well in the early days of Uber, but we ran into significant problems scaling Postgres with our growth. Today, we have some legacy Postgres instances, but the bulk of our databases are either built on top of MySQL (typically using our [Schemaless](https://eng.uber.com/schemaless-part-one/) layer) or, in some specialized cases, NoSQL databases like Cassandra. We are generally quite happy with MySQL, and we may have more blog articles in the future explaining some of its more advanced uses at Uber.



- [2010.10 | 11个重要的数据库设计规则](http://database.51cto.com/art/201204/328629.htm)

> ***规则1: 弄清楚服务目标，OLTP 还是 OLAP 型；***
>
> ***规则2: 将数据按照业务逻辑分成不同的块；***
>
> ***规则3: 不要重度使用规则2，凡事物极必反，需要权衡；***
>
> ***规则4: 把重复，不统一的数据当成最大的敌人，比如说有2列代表的含义完全一样；或者有一列存储的值类型，格式都不一样；***
>
> 规则5: 当心被分隔符分割的数据，它们违反了 “字段不可再分” 的目标，比如说某列的值格式如下：”类目1/商品1“
>
> 规则6: 所有字段都必须完整的依赖主键而不是部分依赖；
>
> 规则7: 仔细选择派生列：如果你正在开发一个 **OLTP** 型的应用程序，那强制不去使用派生字段会是一个很好的思路，除非有迫切的性能要求，比如经常需要求和、计算的 **OLAP **程序，为了性能，这些派生字段就有必要存在了。
>
> ***规则8: 如果性能是关键，不要固执的避免冗余***
>
> 规则9: 多位数据是各种不同数据的聚合
>
> 规则10: 将那些具有“名值表”特点等表统一起来设计
>
> 规则11: 无限分级结构等数据，引用自己的主键作为外键



- [2010.10 | MySQL数据库设计、优化](https://www.slideshare.net/yejr/my-sql-20130820)

> 读写分离，主库只写和少量实时读取请求；
>
> 采用队列方式合并多次写请求，持续写入，避免瞬间压力；
>
> 冷热数据进行切分，lru 原则；
>
> 单表记录行数控制在1000万以内，行平均长度控制在16kb以内，单表20gb 以内；通过内置数据库 `information_schema` 的表 `tables` 来查看信息；
>
> 单实例下数据库表不要超过2000个，单库下数据库表不要超过500个；

- [2010.10 | PostgreSQL 与 MySQL 相比，优势何在？](https://www.zhihu.com/question/20010554)

- [2010.10 | PostgreSQL vs MySQL](https://www.2ndquadrant.com/en/postgresql/postgresql-vs-mysql/)

- 事务

- ```
  事务的概念来自于两个独立的需求：并发数据库访问，系统错误恢复。一个事务是可以被看作一个单元的一系列SQL语句的集合。

  ## 事务的特性（ACID）

  A, atomacity 原子性 
  事务必须是原子工作单元；对于其数据修改，要么全都执行，要么全都不执行。通常，与某个事务关联的操作具有共同的目标，并且是相互依赖的。如果系统只执行这些操作的一个子集，则可能会破坏事务的总体目标。原子性消除了系统处理操作子集的可能性。

  C, consistency 一致性
  事务将数据库从一种一致状态转变为下一种一致状态。也就是说，事务在完成时，必须使所有的数据都保持一致状态（各种 constraint 不被破坏）。

  I, isolation 隔离性 
  由并发事务所作的修改必须与任何其它并发事务所作的修改隔离。事务查看数据时数据所处的状态，要么是另一并发事务修改它之前的状态，要么是另一事务修改它之后的状态，事务不会查看中间状态的数据。换句话说，一个事务的影响在该事务提交前对其他事务都不可见。

  D, durability 持久性
  事务完成之后，它对于系统的影响是永久性的。该修改即使出现致命的系统故障也将一直保持。

  ## 事务的隔离级别

  如果不对数据库进行并发控制，可能会产生异常情况：

  脏读(Dirty Read)
  当一个事务读取另一个事务尚未提交的修改时，产生脏读。同一事务内不是脏读。 一个事务开始读取了某行数据，但是另外一个事务已经更新了此数据但没有能够及时提交。这是相当危险的，因为很可能所有的操作都被回滚，也就是说读取出的数据其实是错误的。

  非重复读(Nonrepeatable Read) 
  一个事务对同一行数据重复读取两次，但是却得到了不同的结果。同一查询在同一事务中多次进行，由于其他提交事务所做的修改或删除，每次返回不同的结果集，此时发生非重复读。

  幻像读(Phantom Reads) 
  事务在操作过程中进行两次查询，第二次查询的结果包含了第一次查询中未出现的数据（这里并不要求两次查询的SQL语句相同）。这是因为在两次查询过程中有另外一个事务插入数据造成的。当对某行执行插入或删除操作，而该行属于某个事务正在读取的行的范围时，会发生幻像读问题。

  丢失修改(Lost Update)

  第一类：当两个事务更新相同的数据源，如果第一个事务被提交，第二个却被撤销，那么连同第一个事务做的更新也被撤销。
  第二类：有两个并发事务同时读取同一行数据，然后其中一个对它进行修改提交，而另一个也进行了修改提交。这就会造成第一次写操作失效。

  为了兼顾并发效率和异常控制，在标准SQL规范中，定义了4个事务隔离级别，（ Oracle 和 SQL Server 对标准隔离级别有不同的实现 ）

  未提交读(Read Uncommitted)
  直译就是"读未提交"，意思就是即使一个更新语句没有提交，但是别的事务可以读到这个改变。

  Read Uncommitted允许脏读。

  已提交读(Read Committed)
  直译就是"读提交"，意思就是语句提交以后，即执行了 Commit 以后别的事务就能读到这个改变，只能读取到已经提交的数据。Oracle等多数数据库默认都是该级别。

  Read Commited 不允许脏读，但会出现非重复读。

  可重复读(Repeatable Read)：
  直译就是"可以重复读"，这是说在同一个事务里面先后执行同一个查询语句的时候，得到的结果是一样的。

  Repeatable Read 不允许脏读，不允许非重复读，但是会出现幻象读。

  串行读(Serializable)

  直译就是"序列化"，意思是说这个事务执行的时候不允许别的事务并发执行。完全串行化的读，每次读都需要获得表级共享锁，读写相互都会阻塞。

  Serializable 不允许不一致现象的出现。

  ## 事务隔离的实现——锁

  共享锁(S锁)
  用于只读操作(SELECT)，锁定共享的资源。共享锁不会阻止其他用户读，但是阻止其他的用户写和修改。

  更新锁(U锁)
  用于可更新的资源中。防止当多个会话在读取、锁定以及随后可能进行的资源更新时发生常见形式的死锁。

  独占锁(X锁，也叫排他锁)
  一次只能有一个独占锁用在一个资源上，并且阻止其他所有的锁包括共享缩。写是独占锁，可以有效的防止“脏读”。

  Read Uncommited 如果一个事务已经开始写数据，则另外一个数据则不允许同时进行写操作，但允许其他事务读此行数据。该隔离级别可以通过“排他写锁”实现。

  Read Committed 读取数据的事务允许其他事务继续访问该行数据，但是未提交的写事务将会禁止其他事务访问该行。可以通过“瞬间共享读锁”和“排他写锁”实现。

  Repeatable Read 读取数据的事务将会禁止写事务（但允许读事务），写事务则禁止任何其他事务。可以通过“共享读锁”和“排他写锁”实现。

  Serializable 读加共享锁，写加排他锁，读写互斥。
  ```
  ​

  ​

  [2017.10 | 10 SQL Tricks That You Didn’t Think Were Possible](https://blog.jooq.org/2016/04/25/10-sql-tricks-that-you-didnt-think-were-possible/)

  > 1. Everything is a table (derived table);
  > 2. data generation with recursive SQL;
  > 3. running total calculations: window functions are aggregations/ranking on a subset of rows relative to the current row being transformed by select;
  > 4. finding the largest series with no Gaps; `with` statements, `cast` keyword, `row_number` window function,
  > 5. finding the length of a series
  > 6. the subset sum problem with sql
  > 7. capping a running total
  > 8. time series pattern recognition
  > 9. pivoting and unpivoting
  > 10. abusing xml and json

  - [2017.10 | Why Uber Engineering Switched from Postgres to MySQL](https://eng.uber.com/mysql-migration/)

  > The early architecture of Uber consisted of a monolithic backend application written in Python that used [Postgres](http://www.postgresql.org/) for data persistence.
  >
  > postgres limitations in uber: inefficient architecture for writes; inefficient data replication; issues with table corruption; poor replica MVCC support; difficulty upgrading to newer releases;
  >
  > Postgres served us well in the early days of Uber, but we ran into significant problems scaling Postgres with our growth. Today, we have some legacy Postgres instances, but the bulk of our databases are either built on top of MySQL (typically using our [Schemaless](https://eng.uber.com/schemaless-part-one/) layer) or, in some specialized cases, NoSQL databases like Cassandra. We are generally quite happy with MySQL, and we may have more blog articles in the future explaining some of its more advanced uses at Uber.

  ​

  - [2010.10 | 11个重要的数据库设计规则](http://database.51cto.com/art/201204/328629.htm)

  > ***规则1: 弄清楚服务目标，OLTP 还是 OLAP 型；***
  >
  > ***规则2: 将数据按照业务逻辑分成不同的块；***
  >
  > ***规则3: 不要重度使用规则2，凡事物极必反，需要权衡；***
  >
  > ***规则4: 把重复，不统一的数据当成最大的敌人，比如说有2列代表的含义完全一样；或者有一列存储的值类型，格式都不一样；***
  >
  > 规则5: 当心被分隔符分割的数据，它们违反了 “字段不可再分” 的目标，比如说某列的值格式如下：”类目1/商品1“
  >
  > 规则6: 所有字段都必须完整的依赖主键而不是部分依赖；
  >
  > 规则7: 仔细选择派生列：如果你正在开发一个 **OLTP** 型的应用程序，那强制不去使用派生字段会是一个很好的思路，除非有迫切的性能要求，比如经常需要求和、计算的 **OLAP **程序，为了性能，这些派生字段就有必要存在了。
  >
  > ***规则8: 如果性能是关键，不要固执的避免冗余***
  >
  > 规则9: 多位数据是各种不同数据的聚合
  >
  > 规则10: 将那些具有“名值表”特点等表统一起来设计
  >
  > 规则11: 无限分级结构等数据，引用自己的主键作为外键

  ​

  - [2010.10 | MySQL数据库设计、优化](https://www.slideshare.net/yejr/my-sql-20130820)

  > 读写分离，主库只写和少量实时读取请求；
  >
  > 采用队列方式合并多次写请求，持续写入，避免瞬间压力；
  >
  > 冷热数据进行切分，lru 原则；
  >
  > 单表记录行数控制在1000万以内，行平均长度控制在16kb以内，单表20gb 以内；通过内置数据库 `information_schema` 的表 `tables` 来查看信息；
  >
  > 单实例下数据库表不要超过2000个，单库下数据库表不要超过500个；

  - [2010.10 | PostgreSQL 与 MySQL 相比，优势何在？](https://www.zhihu.com/question/20010554)
  - [2010.10 | PostgreSQL vs MySQL](https://www.2ndquadrant.com/en/postgresql/postgresql-vs-mysql/)

  ​

  ​

  ​








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

def permute(a, l, r):
    """ O(n * n!) 
    a: string
    l: starting index of the string
    r: ending index of the string
    """
    if l == r:
        print ''.join(a)
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

- ***Triple Step***: A child is running up a staircase with N steps and can hop either 1 step, 2 steps or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.

  - dynamic programming or recursive or tail recursive: f(n) = f(n-1) + f(n-2) + f(n-3) + 3, but
    - dynamic programming: *Space O(n), Time O(n)*
    - recursive: *Space O(1), Time O(3^n)*
    - tail recursive: *Space O(1), Time O(n)*

- ***Robot in a Grid***: Imagine a robot sitting on the upper left corner of grid with r rows and c columns. the robot can only move in two directions, right and down, but certain cells are off limits such that the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to the bottom right.

- ***Magic Index***: A magic index in an array A [1,2,3,….,n-1] is defined to be an index such that A[i] = i. Given a sorted array of distinct integers, write a method to find a magic index.

  - use the ***Sorted*** characteristic of the array, binary search method, O(logN).

- ***Power set***: write a method to return all subsets of a set.

- ***Recursive Multiply***: write a recursive function to multiply two positive integers without using the * or / operator. you can use addition, subtraction and bit shifting, but you should minimize the number of those operations.

  - binary method.

- ***Towers of Hanoi***: In the classic problem of the Towers of Hanio, you have 3 towers and N disks of different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order of size from top to bottom. you have the following constraints:

  - only one disk can be moved at a time
  - a disk is slid off the top of one tower onto another tower
  - a disk cannot be placed on top of a smaller disk

  write a program to move the disks from the first tower to the last using Stacks.


![图片注释](http://odqb0lggi.bkt.clouddn.com/5480622df9f06c8e773366f4/7eecd74e-8c03-11e7-bf57-0242ac140002)

- ***Permutation without dups***: write a method to compute all permutations of a string of unique characters.
- ***Permutation with duplicates***: write a method to compute all permutations of a string whose characters are not necessary unique. The list of permutations should not have duplicates.
- ***Parens***: Implement an algorithm to print all valid (i.e. properly opened and closed ) combinations of n pairs of parentheses.
  - example: input 3
  - output: ((())), ((), ()), (())(), ()(()), ()()()
- ***Coins***: given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents) and pennies (1 cent), write code to calculate the number of ways of representing n cents.
- ***Eight Queens***: write an algorithm to print all ways of arranging eight queens on an 8x8 chess board.
- ***Sorted Merge***: You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B. write a method to merge B into A in sorted order.
- ***Group Anagrams***: write a method to sort an array of strings so that all the anagrams are next to each other.
- ***Sort big file***: imagine you have a 20 GB file with one string per line. explain how you would sort the file.
  - Using ***external sorting*** method.
- ***Missing int***: given an input file with 4 billion non-negative integers. provide an algorithm to generate an integer that is not contained in the file. assume you have 1 GB of memory available for this task. Follow up: what if you have only 10 mb of memory?  assume that all the values are distinct and we now have no more than one billion non-negative integers.
  - bit map algorithm
  - division algorithm
- ***Number swapper***: write a function to swap a number in place (that is without temporary variables)
  - a = a - b
  - b = a + b
  - a = b - a
- ***Bottle of water***: A bottle of coke is $1, you can exchange 2 empty bottles for a bottle of coke. you have N dollars, how many bottles you can drink a lot.

  - `f(n) = int(n) + f(0.5 * int(n) + n - int(n))`
- ***二维数组中的查找***: 在一个二维数组中，每一行都是按照从左到右递增的顺序排序，每一列都是按照从上到下递增的顺序排序，写一个函数，输入一个这样的数组和整数，判断数组中是否含有该整数。
  - 核心：四个角，从哪个角开始便利，找一个数，可以先排除不包含这个数的行或列；
- ***替换空格***：实现一个函数，把字符串中每个空格替换成 "20%"。
  - 思考方式同上题，逆向思考。
- ***归并排序***：两个排序的数组a1，a2，a1后有足够多的空间容纳a2【可有可无】，写一个函数把a2所有数字插入 a1并且所有的数字都是排序的。
  - 完全同上提，替换空格。
- ***逆序打印***：输入一个链表的头节点，从尾到头打印每个节点的值。
  - 递归，考虑到调用栈的溢出哦。
- ***重建二叉树***：输入某二叉树的前序遍历和中序遍历，请重建该二叉树。
  - 递归，理解前序，中序，后序遍历方法。所有递归，动态规划算法，考察的基本都是分析问题，将问题拆分，分解的能力。
- ***用两个栈实现队列***：用两个栈实现一个列队，且实现该队列的两个函数：appendTail(), popHead()，分别完成在队列尾部插入节点和在队列头部删除节点的功能。
  - 即使用两个 “先进后出” 的数据结构实现一个 “先进先出” 的数据结构。
- ***旋转数组的最小数字***：把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
  - O(n) 是最简单的，但是利用排序的特性，可以考虑二分，会更快，所以得出经验，排序数组相关的查找问题，都可以考虑二分。
- ***二进制中1的个数***：写一个函数，输入一个整数，输出该数二进制表示中1的个数。
  - 注意负数的情况
  - 是用 0x0001 左移还是用输入的数右移，值得思考
  - 书中提出来一种新颖的算法，只用重复 m 次，且m即为输入数字中1的个数呢，值得研究
- ***调整数组顺序***：输入一个整数，实现一个函数来调整数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
  - 同样：若是要所有负数在前面，所有非负数在后面呢？
  - 同样：若是要所有能被3整除的在前面，剩余的在后面呢？
- ***包含 min 函数的栈***：定义栈的数据结构，在该结构中实现一个能够得到栈的最小元素的min函数，使min，push，pop 的时间复杂度都是 O(1)
  - 如果用一个临时变量来存储最小值，那当最小值被 pop 后咋办呢？
- ***层次遍历二叉树***：从上往下打印二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
  - 画出二叉树，一步一步分析，使用队列存储即可；
- ***二叉树后序遍历判断***：输入一个整数数组，判断该整数数组是不是某二叉搜索树的后序遍历结果。
  - 核心是根据遍历方式找到根节点，然后左右子树递归分析
- ***数组中出现次数超过一半的数字***：数组中又一个数字出现的次数超过数组长度的一半，请找出这个数字。
- ***最小的k个数***：输入n个整数，找出其中最小的k个数。
- ***连续子数组的最大和***：输入一个整型数组，其中有正数也有负数，数组中一个或连续的多个整数组成一个子数组，求所有子数组的和的最大值，要求时间复杂度为 O(n)。
  - 还可以用动态规划哦，仔细研究推导公式。
- ***从 1 到 n 整数中 1 出现的次数***：输入一个整数，求从 1 到 n 这n个整数的十进制中 1 的出现次数。例如输入 12，从 1到12这些整数中包含 1 点数字有：1，10，11，12，1一共出现5次。
  - count += str(number).count('1')
- ***把数组排成最小的数***：输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印出能拼接的所有数字中的最小的一个。
- ***数组中的逆序对***：在数组中的两个数字如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对，输入一个数组，求出这个数组中的逆序对的总数。
- ***公共节点***：输入两个链表，找出他们的第一个公共节点。
- ***只出现一次的数字***：一个整型数组里除了两个数字之外，其他的数字都出现了2次，写程序找出这两个只出现一次的数字，时间复杂度是 O(n)，空间复杂度是 O(1)。
- ***数组和序列***：输入一个递增排序的数组和一个数字 s，在数组中查找两个数，使他们的和正好是s。
  - 双指针发，头尾同时遍历
  - s/2 法，找到平均数，再向头尾遍历
- ​















# Data Engineer

- Do you have experience with data modeling? If so, what data modeling tools do you have experience using?



# System Conprehension and Design

- ***Social Network***: how would you design the data structures for a very large social network like facebook or linkedin? describe how you would design an algorithm to show the shortest path between two people( e.g. me -> bob -> susan -> jason -> you)

- ***Web crawler***: if you were designing a web crawler, hwo would you avoid getting into infinite loops?

- ***Personal financial manager***: how would you design a personal financial manager. this system would connect to your back accounts analyze your spending habits, and make recommendations.

- ***Thread vs Process***: what's the difference between a thread and a process?

- ***Code Debug: unsigned int***:

  ```c
  unsigned int i;
  for (i=100; i>=0; --i)
    printf("%d\n", i);
  ```

- linux folder:

  - root: files belong to root
  - home: files belong to general users
  - bin: commands
  - sbin: commands with privilege
  - mnt: usb, cd
  - etc: configuration files
  - var: changable files
  - boot: starting system files
  - usr: default directory of installing application, like Program File under windows

- linux commands

  - files
    - cat
    - grep
    - vi
    - touch
    - rm
    - cp
    - ln
    - head
    - tail
    - more
    - less
    - chmod, chown
  - folders
    - ls
    - pwd
    - cd
    - mkdir
    - rmdir
    - find: find /home -size 10k
  - other
    - `>,>>`
    - zip
    - unzip
    - tar

- ***SOA: Service Orented Architecture***:

  - 模块化开发 + 分布式计算
  - 松耦合：实现，时间，位置，版本
  - 服务设计原则：
    - 优化远程调用
    - 消除冗余数据
    - 粗粒度契约，通用契约
    - 低耦合，隔离变化

- soa 是面向服务架构的，而 rest 则是面向资源的；

- [全面了解Nginx主要应用场景](http://www.raye.wang/2017/02/24/quan-mian-liao-jie-nginxdao-di-neng-zuo-shi-yao/)


> 反向代理：客户端请求发送到 nginx 上，nginx将请求转发到内部网络的服务器上，并将从服务器上得到的结果返回给客户端。
>
> 负载均衡：有两台及两台以上服务器时，可以通过 nginx 来配置，请求转发到哪台服务器上，此时客户端永远只访问 nginx，并不知道后期如何处理的。
>
> http 服务器：nginx 其实也是一个服务器，只是不处理逻辑计算相关的，所以完全可以用来存放静态资源，也算是缓存的一种实现方案；也是网站动静分离的一种核心思路；
>
> 正向代理：客户端向代理发送一个请求并且制定原始服务器目标，代理将请求转发到客户端指定的服务器目标上，并将获取的结果返回给客户端。
>
> 






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
- ***Triangle***: 一个直角三角形，底边是 10，向底边所做的高是6，求这个三角形的面积.
  - 2 d平面上这样的三角形不存在
  - 3d 球形面上，这样的三角形的确存在
- ​




# Front-End

- bootstrap: HTML, CSS, JS前端布局框架；支持响应式布局，支持移动设备；
- angularjs: js框架，javascript -> jQuery -> angularJS;
- ​



  	





# Resource



- https://www.careercup.com/
- https://www.careercup.com/resume
- http://rosettacode.org/wiki/Rosetta_Code
- http://visualgo.net
- [剑指offer github](https://github.com/gatieme/CodingInterviews)
- [http://www.infoq.com/cn/articles/micro-soa-1](http://www.infoq.com/cn/articles/micro-soa-1)
- http://www.infoq.com/cn/articles/micro-soa-2
- [极客学院 算法教程](http://wiki.jikexueyuan.com/list/sort/)








---

# NZ



## plan

- ~ 2018.05: make money & learn NZ and the world
- ~ 2018.01: simulate application, make the excel form
- ~ 2018.01: Make IELTS done


-  2018.06 -> China Working Holiday Visa
  - [x] criteria: https://www.immigration.govt.nz/new-zealand-visas/apply-for-a-visa/criteria/china-working-holiday-visa?nationality=nationality-CHN&country=residence-NZL&applying=no
  - [x] identity: passport
  - [ ] healthy: make it before 2018.04
  - [x] character
  - [x] bona fide
  - [x] age: 18 ~ 30
  - [x] citizenship
  - [ ] onward travel: make it before 2018.05
  - [ ] funds: make it before 2018.05
  - [x] previous approvals
  - [x] education
  - [ ] english language: IELTS 5.5 or more, make it before 2018.01
  - [x] ordinarily resident
  - [x] location
  - [x] medical insurance
-  2018.08 ~ 2019.08 In NZ, feeling and planning 





## resources

- http://jack-liu.com/
- [新西兰打工度假怎么样？需要做什么准备？](https://www.zhihu.com/question/19998099)
- http://www.newzealand.com/cn/
- ​
