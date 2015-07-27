---
category: python
published: false
layout: post
title: 伴我一路走来的那些bug们，你们好    
description: bug，永远是程序员最忠实的朋友，你打他骂他虐他，他还是一如既然滴追随你~~~
---    


## 1. failed to write data to stream

- 环境：ipython, OSX
- 操作：在ipython里import 一个pure module
- 问题： Python - ERROR - failed to write data to stream: <open file '<stdout>', mode 'w' at 0x104c8f150>
- 办法：export PYTHONIOENCODING=UTF-8 will solve it.
- 相关：[stackoverflow](http://stackoverflow.com/questions/28115375/python-error-failed-to-write-data-to-stream-open-file-stdout-mode-w)


## 2. Git: fatal: Pathspec is in submodule

- 环境：OSX, Git
- 操作：git add *
- 问题：有一个github repo [暂且叫father]，其中这个repo里有子module [暂且叫 child]，且这个child也是作为一个独立的github repo存在，我更改了child下的一些文件，然后在father下执行git add，准备在father下直接commit和push，执行git add 的时候出错，提示 `Pathspec is in submodule`。
- 办法：现在child下add，commit和push，然后再到father下add，commit和push；   
- 相关：最好的方式是：在child下git branch 一个新的分支，然后在这个分支上修改，然后add，commit，push；修改好child后，再到father下新建一个分支，执行add，commit，push。最后，要merge的时候，也是先merge掉child，然后再merge掉father。因为child作为一个独立的repo，所有的更改都要在child这个独立repo下面做更改，由于项目需要，child作为father的一个子module，不能直接在father里更改child然后再add，commit，push。因为father里的child，只是链接到了child这个独立repo。或者说，father里的child只是独立的child的一个只读镜像。   


## 3. DB: (2013, 'Lost connection to MySQL server during query'), python decorator, gevent, greenlet, function life cycle

- 环境：OSX, Python 2.7, Gevent, MySQL
- 操作：对每一个用户异步地向数据库写一条数据［实际上的逻辑要稍微复杂一点］，为了方便理解，我们现在构造这样一个场景。用户在网页上参赛高考，全是选择题，当用户选中答案并且准备开始下一题时，后台需要把用户的答案写到数据库里面。但是因为考生太多了，假设有1000万呢，一张2个小时的考卷有150到选择题，并且假设一个考生平均每道题会更改答案0.2次，那么我们先算算这个请求压力是多少：

```
(total request times)/(total time in seconds) = 
10^8 * 150 * (1 + 0.2) / 2 / 60 / 60 = 
180 * 10^8 / 7200 = 
0.025 * 10^8 = 
2.5 * 10^6 = 25 万次请求／每秒
```

可见其实请求也不是特别大，但是这只是平均请求，天才知道峰值多少呢？其次，zf总不会也要模仿12306那样，请个大公司来做吧。于是，zf里的一个工程师决定，应该把写数据库这个操作异步执行，这样考生在网页上点了下一题之后，虽然立即跳转到下一题，但并不表示考生上一题的答案已经写入数据库了。

ok了，场景大概就是这样了。 详情见代码片段 ：

```
class Test(object):
    @get_dbc
    def assign_user_to_exp(self, dbc, user_id, cell_id):
            self.g_pool.spawn(
                self.async_assign_user_to_exp,
                dbc,
                user_id,
                cell_id,
            )
            return

    def async_assign_user_to_exp(self, dbc, user_id, cell_id):
        return dbc.execute(''' there is a sql sentence that refering user_id and cell_id, just leave details here ''')
```


- 问题：现在的问题是，每次执行 Test().assign_user_to_exp() 时，都会发生错误：(2013, 'Lost connection to MySQL server during query')。   
- 办法：装饰器get_dbc换个位置， 如下：  

```
class Test(object):
    def assign_user_to_exp(self, user_id, cell_id):
            self.g_pool.spawn(
                self.async_assign_user_to_exp,
                user_id,
                cell_id,
            )
            return

    @get_dbc
    def async_assign_user_to_exp(self, dbc, user_id, cell_id):
        return dbc.execute(''' there is a sql sentence that refering user_id and cell_id, just leave details here ''')
```

- 相关：bug的原因是在执行 Test().assign_user_to_exp() 的时候，都先会通过装饰器 get_dbc 去取一个 db 的connection/cursor，然后作为参数传给 async_assign_user_to_exp 函数。可是这里有个问题，gevent 创建了一个greenlet后，也就是 Test().assign_user_to_exp() 的真实作用，这个时候 dbc 已经被释放了，然后过一会儿在greenlet里真正执行数据库操作时，即函数 async_assign_user_to_exp 开始执行时，才发现尼玛穿进来的 dbc 数据库连接已经被释放掉了，所以就会报一个 Lost connection to MySQL server during query 。真是很微妙的，很细节的问题。这个问题我和一个同事研究了好些时间都没有找到问题，后来 cto 过来一看，秒秒钟就解决来。突然间想起李开复的一句话 : 要想做技术型管理者，首先要在技术能力上让手下佩服。不说鸟，继续学习去～









