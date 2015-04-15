---
category: books
published: false
layout: post
title: book-7. Python 源码剖析关键字
description: 仅仅是记录我个人的读书记录，看官不必在意～
---


## 
## 0. 准备工作

### 0.1 Python 总体架构

- File Groups：python模块、库以及用户自定义模块；
- Python Core：解释器，或者叫虚拟机。箭头表示数据流方向。scanner对应词法分析，parser对应语法分析，生成AST，compiler根据AST生成指令集合Python字节码，code evaluator执行字节码，因此，code evaluator又叫虚拟机；
- Runtime Environment：python运行时环境，包括对象/类型系统，内存分配器和运行时状态信息。对象/类型系统包含了python中存在的各种内置对象以及用户自定义的类型和对象；内存分配器全权负责对内存的申请工作，即与c的malloc一层的接口；运行时状态信息维护了解释器执行字节码时不同的状态，比如正常、异常状态之间的切换动作，可视为一个巨大复杂的有穷状态机；

![python-arch.jpg](../images/python-arch.jpg)


## 1. Python 对象初探

　　对象是python中最核心的一个概念，在python中，一切都是对象，类型也说一种对象。在python中，对象就是为c中的结构体在堆上申请的一块内存，一般来说，对象是不能被静态初始化，并且也不能在占空间上生存。类型对象是例外，python中所有内建的类型对象都是被静态初始化的。   
　　Python通过对一个对象的引用技术的管理来维护对象在内存中的存在与否。在python中一切都是对象，都有一个ob_refcnt变量，维护着该对象的引用技术，从而也最终决定该对象的创建于消亡。这里类似一个observer模式,在ob_refcnt减为0后，将触发对象销毁的实践。

### 1.1 Python中对象分类

- Fundamental对象：类型对象
- Numberic对象：数值对象
- Sequence对象：容纳其他对象的序列集合对象
- Mapping对象：类似C++中map的关联对象
- Internal对象：python虚拟机在运行时内部使用的对象


## 2. Python中的整数对象

## 3. Python中的字符串对象

## 4. Python中的list对象

## 5. Python中的dict对象

　　关联容器的设计总会极大地关注键的搜索效率。C++的STL中有关联容器的相关实现map，map是基于RB-Tree设计实现，红黑树是一种平衡二叉树，能够提供良好的搜索效率，理论上搜索的时间复杂度为O(Log2N)。   
　　Python中的关联容器叫dict，其对搜索的要求极高，采取了hash table来设计实现。用于映射的函数叫散列函数，映射后的值叫散列值，在散列表的实现中，所选择的散列函数的优劣将直接决定所实现的散列表的搜索效率。统计显示，散列表的装载率大于2/3时，散列冲突发生的概率就会大大增加。    
　　STL中的hash table采用开链法来解决冲突问题，python中采用开放地址法来解决冲突。即当产生冲突时，通过一个二次hash函数计算下一个哈希值，如此不断hash，总会有一个可用的位置。但这样会形成一个冲突探测链，当需要删除某条探测链上的某个元素时，问题就产生了。如果冲突探测链的元素依次是a->b->c，现在如果删除中间位置上的元素b，若直接删除b，则会导致探测链的断裂，这样理轮上就无法查询到c了。所以，在开放定址的hash table中，删除某条探测链上的元素时不能进行真正的删除，而且进行一种假删除，或做标记，必须要让该元素还在探测链上。   

## 6. Small Python

## 7. Python的编译结果 - Code对象与pyc文件
 
　　Python程序的执行原理和java，c#一样，都可以用两个词概括：虚拟机，字节码。实际上，python解释器在执行任何一个python程序的时候，首先进行的动作都是先对文件中的python源代码进行编译，编译的主要结果是产生一组python的字节码，然后将编译的结果交给python的虚拟机，由虚拟机按顺序一条一条地执行字节码。   

## 8. Python虚拟机框架

　　每一个.py文件视为一个module，这些module中有一个是主module，如果以python main.py启动python程序，那么main.py就是主module。Python中引入module的概念，一是将一些逻辑相关的代码放到一个module中，二是为整个系统划分命名空间。在python中，当你加载一个module的时候，python都会编译、执行这个module里的每一行语句。  

### 8.1 约束与名字空间   
　　在python中，赋值语句是一类相当特殊的语句，因为他们会影响到名字空间。在赋值语句被执行后，从概念上讲，我们实际上得到了一个(name, obj)这样的关联关系，我们称这种关系叫做约束。赋值语句就是约束建立的地方。当一个约束建立后，它不会立即消失，相反地，它会长久地影响程序的行为。约束的容身之处就是名字空间，在python中，名字空间就是一个PyDictObject对象实现的。一个对象的名字空间中的所有名字都成为对象的属性，和属性对应的有属性引用的概念，属性引用就是使用另一个名字空间中的名字，一个module定义了一个独立的名字空间。     
　　在一个module内部，可能存在多个名字空间，每一个名字空间都与一个作用域对应。对于作用域这个概念，至关重要的是要记住它仅仅是由源程序的文本决定的。一个约束在程序正文的某个位置是否起作用，是由该约束在文本中的位置是否觉得的，而不是在运行时动态决定的。因此，我们说Python具有静态作用域。  
　　LGB规则：最内嵌套作用域规则。  
　　在python中，一个moudle对应的源文件定义了一个作用域，这个称谓global作用域；一个函数定义了一个local作用域；python本身还定义了一个最顶层的作用域builitin。名字引用优先级：local -> global -> builtin。   
　　下面函数，func() 实际执行的是函数g()。python在执行func = f()的时候，会执行函数f中的def g()语句，这是python会将约束"a=2"与函数g()对应的函数对象捆绑在一起，将捆绑后的结果返回，这个捆绑起来的整体叫做 闭包。有关闭包的引用，可以看下面两篇文章。而且正因为闭包在python里的实现，原来的LGB规则变成了LEGB规则。   

[闭包的概念、形式与应用](https://www.ibm.com/developerworks/cn/linux/l-cn-closure/)    
[Python深入04 闭包](http://www.cnblogs.com/vamei/archive/2012/12/15/2772451.html)

```
a = 1
def f():
    a = 2
    def g():
        print a  # [1] 打印2
    return g

func = f()
func()  # [2]
```



