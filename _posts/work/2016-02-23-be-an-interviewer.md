---
category: work
published: false
layout: post
title: 如何当个面试官
description: 怎么做一个好的面试官.
---


## 1. 一些宗旨

`面试的原则`

- 面试是为了给公司寻找最适合的人才，而不是最高级人才。
- 需要新员工完成什么样的任务？
- 怎样的人能完成这样的任务？
- 哪些方法可以发现这样的人？

`提问的原则`

- 每一个面试问题都有明确的目的。你不仅自己了解，还能向其他面试官解释清楚。
- 多提一些开放性（Open-ended）的问题，而不是那种用Yes/No就可以回答的问题。这样做使你有机会与面试者展开讨论，并且提出后续的问题，尽可能多地了解对方。
- 不要问宗教、家庭、健康、个人隐私等方面的问题。
- 不要问太复杂的问题。因为面试者没有太多思考时间，所以无法周全地回答，你也就无从判断他的能力了。


## 2. STAR 原则

- Situation : 了解应聘人员以前的工作背景，尽可能多了解他先前供职公司的经营管理状况、所在行业的特点、该行业的市场情况，即所谓的背景调查;
- Task : 然后着重了解该员工具体的工作任务都是哪些;
- Action : 每一项工作任务都是怎么做的，都采取了哪些行动;
- Result : 所采取行动的结果如何;

STAR 原则也可以用于一些细化的问题，比如解决一个难题的始末。


## 面试流程

- 自我介绍

- 告知面试流程

```
    + 基础知识
    + 行业知识
    + 协作能力
```


- 基础能力
    + 首先请他简要介绍下他的经历，并针对他做过的项目选取几个兴趣点深入问一下，考察他做过的事是能全局把握的，还是只是负责一个点；
    + 根据简历选择1~3个与你们公司实际情况最相近的项目，请他简单介绍一下，之后询问项目过程中发生的技术难关、跨团队沟通等问题的解决上；
    + 做过的项目中的挑战性的问题，怎么解决的，解决这个问题的过程；
    + github 账号；
    + 



- 学习能力
    + 如何学习最新一门新的语言？学习过程中遇到的问题怎么解决的？
    + 换公司，换项目组后如何适应的？
    + 去年你读了几本技术书籍？最喜欢的书籍？



- 行业能力
    + 是否使用过相关产品，对产品对看法（意见，建议）;
    + 提出几个实际工作中遇到的技术问题，请他讲讲他的理解和解决办法;
    + 找出过去曾经困扰过你或你们团队的问题（可以是技术、运营、沟通），列明产生问题的背景，在面试中用于情景模拟，找出1个技术问题和1个沟通问题;
        + 与产品经理的想法冲突；尽量保证功能可用，但产品细节可以继续完善；试水；A/B test;
    + 



- 协作能力
    + 要了解他换工作的原因，动机，他的期望是什么，你要判断公司能否满足他的期望;


- 其他
    + 兴趣，爱好，特长；如何发展自己的兴趣爱好；
    + 自己怎么评价自己;
    + 理想中的生活，工作状态;


## Python 问题

- 简历中的语言使用时间；

- Why use function decorators? Give an example.

```
    A decorator is essentially a callable Python object that is used to modify or extend a function or class definition. One of the beauties of decorators is that a single decorator definition can be applied to multiple functions (or classes). Much can thereby be accomplished with decorators that would otherwise require lots of boilerplate (or even worse redundant!) code. Flask, for example, uses decorators as the mechanism for adding new endpoints to a web application. Examples of some of the more common uses of decorators include adding synchronization, type enforcement, logging, or pre/post conditions to a class or function.
```

- What are lambda expressions, list comprehensions and generator expressions? What are the advantages and appropriate uses of each?

Lambda expressions are a shorthand technique for creating single line, anonymous functions. Their simple, inline nature often – though not always – leads to more readable and concise code than the alternative of formal function declarations. On the other hand, their terse inline nature, by definition, very much limits what they are capable of doing and their applicability. Being anonymous and inline, the only way to use the same lambda function in multiple locations in your code is to specify it redundantly.

List comprehensions provide a concise syntax for creating lists. List comprehensions are commonly used to make lists where each element is the result of some operation(s) applied to each member of another sequence or iterable. They can also be used to create a subsequence of those elements whose members satisfy a certain condition. In Python, list comprehensions provide an alternative to using the built-in map() and filter() functions.

As the applied usage of lambda expressions and list comprehensions can overlap, opinions vary widely as to when and where to use one vs. the other. One point to bear in mind, though, is that a list comprehension executes somewhat faster than a comparable solution using map and lambda (some quick tests yielded a performance difference of roughly 10%). This is because calling a lambda function creates a new stack frame while the expression in the list comprehension is evaluated without doing so.

Generator expressions are syntactically and functionally similar to list comprehensions but there are some fairly significant differences between the ways the two operate and, accordingly, when each should be used. In a nutshell, iterating over a generator expression or list comprehension will essentially do the same thing, but the list comprehension will create the entire list in memory first while the generator expression will create the items on the fly as needed. Generator expressions can therefore be used for very large (and even infinite) sequences and their lazy (i.e., on demand) generation of values results in improved performance and lower memory usage. It is worth noting, though, that the standard Python list methods can be used on the result of a list comprehension, but not directly on that of a generator expression.

- Consider the two approaches below for initializing an array and the arrays that will result. How will the resulting arrays differ and why should you use one initialization approach vs. the other?

```
    >>> # INITIALIZING AN ARRAY -- METHOD 1
    ...
    >>> x = [[1,2,3,4]] * 3
    >>> x
    [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
    >>>
    >>>
    >>> # INITIALIZING AN ARRAY -- METHOD 2
    ...
    >>> y = [[1,2,3,4] for _ in range(3)]
    >>> y
    [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
    >>>
    >>> # WHICH METHOD SHOULD YOU USE AND WHY?
```

While both methods appear at first blush to produce the same result, there is an extremely significant difference between the two. Method 2 produces, as you would expect, an array of 3 elements, each of which is itself an independent 4-element array. In method 1, however, the members of the array all point to the same object. This can lead to what is most likely unanticipated and undesired behavior as shown below.


```
>>> # MODIFYING THE x ARRAY FROM THE PRIOR CODE SNIPPET:
>>> x[0][3] = 99
>>> x
[[1, 2, 3, 99], [1, 2, 3, 99], [1, 2, 3, 99]]
>>> # UH-OH, DON’T THINK YOU WANTED THAT TO HAPPEN!
...
>>>
>>> # MODIFYING THE y ARRAY FROM THE PRIOR CODE SNIPPET:
>>> y[0][3] = 99
>>> y
[[1, 2, 3, 99], [1, 2, 3, 4], [1, 2, 3, 4]]
>>> # THAT’S MORE LIKE WHAT YOU EXPECTED!
...
```

- What will be printed out by the second append() statement below?

```
>>> def append(list=[]):
...     # append the length of a list to the list
...     list.append(len(list))
...     return list
...
>>> append(['a','b'])
['a', 'b', 2]
>>>
>>> append()  # calling with no arg uses default list value of []
[0]
>>>
>>> append()  # but what happens when we AGAIN call append with no arg?
```

When the default value for a function argument is an expression, the expression is evaluated only once, not every time the function is called. Thus, once the list argument has been initialized to an empty array, subsequent calls to append without any argument specified will continue to use the same array to which list was originally initialized. This will therefore yield the following, presumably unexpected, behavior:

```
>>> append()  # first call with no arg uses default list value of []
[0]
>>> append()  # but then look what happens...
[0, 1]
>>> append()  # successive calls keep extending the same default list!
[0, 1, 2]
>>> append()  # and so on, and so on, and so on...
[0, 1, 2, 3]
```

- How might one modify the implementation of the ‘append’ method in the previous question to avoid the undesirable behavior described there?

The following alternative implementation of the append method would be one of a number of ways to avoid the undesirable behavior described in the answer to the previous question:

```
>>> def append(list=None):
...     if list is None:
            list = []
        # append the length of a list to the list
...     list.append(len(list))
...     return list
...
>>> append()
[0]
>>> append()
[0]
```

- How can you swap the values of two variables with a single line of Python code?


- What’s your approach to unit testing in Python?

The most fundamental answer to this question centers around Python’s unittest testing framework. Basically, if a candidate doesn’t mention unittest when answering this question, that should be a huge red flag.

unittest supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of the tests from the reporting framework. The unittest module provides classes that make it easy to support these qualities for a set of tests.

Assuming that the candidate does mention unittest (if they don’t, you may just want to end the interview right then and there!), you should also ask them to describe the key elements of the unittest framework; namely, test fixtures, test cases, test suites and test runners.

A more recent addition to the unittest framework is mock. mock allows you to replace parts of your system under test with mock objects and make assertions about how they are to be used. mock is now part of the Python standard library, available as unittest.mock in Python 3.3 onwards.

The value and power of mock are well explained in An Introduction to Mocking in Python. As noted therein, system calls are prime candidates for mocking: whether writing a script to eject a CD drive, a web server which removes antiquated cache files from /tmp, or a socket server which binds to a TCP port, these calls all feature undesired side-effects in the context of unit tests. Similarly, keeping your unit-tests efficient and performant means keeping as much “slow code” as possible out of the automated test runs, namely filesystem and network access.

## Spark 问题

- what is spark application;
- what is driver, master, worker, executor;
- how to deploy spark app, configure spark cluter;
- what is RDD;
- what is dataframe, datasets;
- what is transforms and actions in rdd, why design transforms and actions;
- 



## 参考文档

- [STAR 面试准则](http://baike.baidu.com/subview/470818/11235965.htm)
- [如何面试一个工作经验比自己高很多的人](https://www.zhihu.com/question/20042950)
- [怎样花两年时间去面试一个人](http://mindhacks.cn/2011/11/04/how-to-interview-a-person-for-two-years/)

