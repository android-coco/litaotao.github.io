---
category: python
published: true
layout: post
title: Python 并发编程之一：Gevent    
description: Gevent，用过都说好~
---    


## 1. 什么是Gevent

gevent是一个基于libev的python并发框架,以微线程greenlet为核心，使用了epoll事件监听机制以及诸多其他优化而变得高效.而且其中有个monkey类, 将现有基于Python线程直接转化为greenlet(类似于打patch).

greenlet 包是 Stackless 的副产品，其将微线程称为 “tasklet” 。tasklet运行在伪并发中，使用channel进行同步数据交换。

一个”greenlet”，是一个更加原始的微线程的概念，但是没有调度，或者叫做协程。这在你需要控制你的代码时很有用。你可以自己构造微线程的 调度器；也可以使用”greenlet”实现高级的控制流。例如可以重新创建构造器；不同于Python的构造器，我们的构造器可以嵌套的调用函数，而被嵌套的函数也可以 yield 一个值。(另外，你并不需要一个”yield”关键字，参考例子)。


## 2. 什么是 Coroutine

要理解Gevent，明白Gevent的执行机制，需要了解另外一个概念：Coroutine，中文叫做协程。第一次看见这个名词，确实很奇怪，进程、线程都了解了，突然冒出个协程，还真有点反应不过来。

按照 [进程、线程和协程的理解](http://blog.leiqin.info/2012/12/02/%E8%BF%9B%E7%A8%8B%E3%80%81%E7%BA%BF%E7%A8%8B%E5%92%8C%E5%8D%8F%E7%A8%8B%E7%9A%84%E7%90%86%E8%A7%A3.html) 的说法：   


- 进程拥有自己独立的堆和栈，既不共享堆，亦不共享栈，进程由操作系统调度。
- 线程拥有自己独立的栈和共享的堆，共享堆，不共享栈，线程亦由操作系统调度(标准线程是的)。
- 协程和线程一样共享堆，不共享栈，协程由程序员在协程的代码里显示调度。


上面的说法不是很好理解，后来发现这篇文章 [浅谈coroutine与gevent](http://blog.ez2learn.com/2010/07/17/talk-about-coroutine-and-gevent/), 里面对协程的解释是：  


    用简单的一句话来说Coroutine，就是可以暂时中断，之后再继续执行的程序， 
    我们来看一个例子，事实上Python就有最基础的Coroutine，也就是generator

好了，通过上面两篇文章，理解协程已经对比协程、进程、线程的概念就清晰很多了：  

协程就是一种特殊的并发机制，其调度[就是指什么时候调用什么函数]完全由程序员指定，比如说这篇文章里的例子：  [浅谈coroutine与gevent](http://blog.ez2learn.com/2010/07/17/talk-about-coroutine-and-gevent/) ：    

{% highlight python %}

# -*- coding: utf8 -*-
def foo():
    for i in range(10):
        # 丢资料并且把主控权交给呼叫者
        yield i
        print u'foo: 主控又回到我手上了，打我阿笨蛋'

bar = foo()
# 执行coroutine
print bar.next()
print u'main: 现在主控权在我们手上，做点杂事'
print 'main:hello baby!'
# 回到刚才foo这个coroutine中断的地方继续执行
print bar.next()
print bar.next()


###结果：

0
main: 现在主控权在我们手上，做点杂事
main:hello baby!
foo: 主控又回到我手上了，打我阿笨蛋
1
foo: 主控又回到我手上了，打我阿笨蛋
2
 
{% endhighlight %}

## 3. Gevent适用场景  

说到Gevent的适用场景，不得不先理解Gevent的优缺点。按照上面我们的说法，还有那两篇文章的理解，Gevent是通过协程的机制来实现并行，即其并行机制并没有利用到多核CPU的优势，所以很明显了，Gevent的优缺如下：    

- 多进程能够利用多核优势，但是进程间通信比较麻烦，另外，进程数目的增加会使性能下降，进程切换的成本较高。程序流程复杂度相对I/O多路复用要低。  
- I/O多路复用是在一个进程内部处理多个逻辑流程，不用进行进程切换，性能较高，另外流程间共享信息简单。但是无法利用多核优势，另外，程序流程被事件处理切割成一个个小块，程序比较复杂，难于理解。   
- 线程运行在一个进程内部，由操作系统调度，切换成本较低，另外，他们共享进程的虚拟地址空间，线程间共享信息简单。但是线程安全问题导致线程学习曲线陡峭，而且易出错。  
- 协程有编程语言提供，由程序员控制进行切换，所以没有线程安全问题，可以用来处理状态机，并发请求等。但是无法利用多核优势。   

所以，协程的适用场景，应该是一些I/O密集型的并行程序，而对应的计算密集型，应当采用传统的多线程、多进程方案。   

## 4. Gevent编程模式和思维方法   

我想从两个例子来介绍Gevent的编程模式，第一个比较简单，可以直接去看这篇文章里的开篇例子，[gevent程序员指南](http://xlambda.com/gevent-tutorial/#)。不过这个例子只是简单的解释gevent的执行流程和编程模式，离现实应用还有一定的距离。当看完这篇文章后，可以参考Firefox的一个实例就行了，[Python Gevent应用](http://www.firefoxbug.com/index.php/archives/2750/) 。

总结一下，按照我个人的理解，要想用好gevent，需要先思考下面几点：

- 你的应用是否需要考虑Gevent；   
- 如何把你的大任务slice成小任务，这些任务之间是否独立；   
- 如果收集，处理小任务执行的结果；
- 理解如何真正利用gevent来实现并行，很多情况下，如果是网络I/O，需要打patch的；比说 [Python Gevent应用](http://www.firefoxbug.com/index.php/archives/2750/)   
- 这里接上一点，打patch要小心，比如说打了socket的patch，要先知道会不会影响到本应用中其他用了socket的服务，因为打patch是直接替换了当前运行时环境里的socket，所以在当前运行时环境里使用socket的服务都会受影响；

## 5. Gevent In Action 

因为Gevent多用于I/O密集型并发程序，而网络请求又是很常见的一种I/O请求，所以在大规模网络并发请求的时候，可以使用Gevent。相信python程序员都应该用过 requests 这个包吧，都应该知道 requests 的作者，kennethreitz，一个货真价实的 python界的大牛。他在写了 requests 的同时，还写了一个包：[grequest ： gevent + requests ](https://github.com/kennethreitz/grequests)，把requests用gevent包了一下，实现异步的网络请求，下次大家要是有网络方面的并发请求，需要用到gevent的话，就不用重复造轮子了，直接用 [grequests](https://github.com/kennethreitz/grequests) 就好了。


## 参考文章   

- [Python Gevent应用](http://www.firefoxbug.com/index.php/archives/2750/)    
- [进程、线程和协程的理解](http://blog.leiqin.info/2012/12/02/%E8%BF%9B%E7%A8%8B%E3%80%81%E7%BA%BF%E7%A8%8B%E5%92%8C%E5%8D%8F%E7%A8%8B%E7%9A%84%E7%90%86%E8%A7%A3.html)    
- [浅谈coroutine与gevent](http://blog.ez2learn.com/2010/07/17/talk-about-coroutine-and-gevent/)    
- [gevent程序员指南](http://xlambda.com/gevent-tutorial/#)    
- [python greenlet背景介绍与实现机制](http://blog.jobbole.com/77240/)
- [Python几种并发实现方案的性能比较](http://www.elias.cn/Python/PyConcurrency?from=Develop.PyConcurrency)




## 扫一扫     

![2015-05-28-python-gevent.md](../../images/share/2015-05-28-python-gevent.md.jpg)