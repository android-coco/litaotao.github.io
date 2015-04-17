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

　　同样，下面这个例子会抛异常“local variables 'a' referenced before assignment”。关键要理解最内嵌套作用域规则，由一个赋值语句引进的名字在这个赋值语句所在的作用域里是可见的。这句话的意思，对应到代码里，就是说虽然“a=2”这个约束在“print a”之后定义的，但由于他们在同一个作用域内，所以[2]处a的定义对[1]出的a是可见的。按照LEGB规则，在local名字空间里就能找到名字a，所以使用的是local名字空间里的a。所以，这里的逻辑是这样的，在执行"print a"时，虽然已经知道f()函数作用域里是有a这个变量的，但a还没有被赋值呢，所以才抛出一个异常。    

```
a = 1
def g():
    print a

def f():
    print a #[1]
    a = 2   #[2]

g()
f()
```

　　如果想要 'print a' 输出2的话，可以在之前加一句 'global a'。当一个作用域里出现了global语句时，就意味着我们强制命令python对某个名字的引用只参考global名字空间，而再不去管LEGB规则。   

```
a = 1
def f():
    global a 
    print a # output : 1
    a = 2

f()
print a # output : 2
```

### 8.2 Python运行时环境初探
　　简单了解下 Python的运行模型(主要是线程模型)。Python在初始化时会创建一个主线程，其运行时环境中存在一个主线程。以win32平台为例，对原生的win32可执行文件，都会在一个进程中运行。进程并非是与机器指令序列相对应的活动对象，这个与可执行文件中的机器指令序列对应的活动对象是由线程这个概念来进行抽象的，而进程则是线程的活动环境。   
　　对于通常的单线程可执行文件，在执行时操作系统会创建一个进程，在进程中又会有一个主线程。而对于多线程的可执行文件，在执行时会创建一个进程和多个线程，该多个线程能共享进程地址空间中的全局变量，这就自然而然出现了多线程同步的问题。   
　　在win32下，线程是不能独立存活的，它需要存活在进程的环境中，而多个线程可以共享进程的一些资源。在Python中也是如此。例如，一个python出现有两个线程，都会进行一个 import sys 的动作，那这个sys模块是全局共享的。如果每个线程都有自己独立的module集合，那么python对内存的消耗会大得惊人。  

## 9. Python虚拟机中的一般表达式

## 10. Python虚拟机中的控制流

## 11. Python虚拟机中的函数机制  

## 12. Python虚拟机中的类机制    

　　从Python 2.5开始，python中有两套类机制，一套称为classic class，另一套称为new style class。   
　　在python 2.2之前，python中存在一个裂缝，就是python的内置type与程序员定义的class并不是完全等同的。比如，用户定义的classA可以被继承，作为另一个classB的基类。但python的内置type却不能被继承，也就是说没有办法以类似c++中的继承方式，创建一个继承自dict的类myDict。    
　　在面向对象的理论中，有两个核心的概念：类和对象。在python中所有的东西都是对象，所以类也是一种对象。以下定义了一些术语，尝试用另一套结构对python中的类机制建模。   
　　在python 2.2之前，python中实际存在三类对象：   

- type对象：表示python内置的类型；  
- class对象：表示python程序员定义的类型；
- instance对象：表示由class对象创建的实例；

　　而在python 2.2之后，type和class已经统一，所以我们用“class对象”来统一表示python 2.2之前的“type对象”和“class对象”。   

　　在python的三种对象之间，存在着两种关系：  

- is kind of: 对应于面向对象中的基类与子类之间的关系； 
- is instance of: 对应于面向对象中类与实例之间的关系；  

```
class A(object):
    pass

a = A()
```

　　其中包含了三个对象：object - class对象；A - class 对象；a - instance对象。通过对象的__class__属性或内置的type方法可以探测一个对象和哪个对象存在is instance of关系；而通过对象的__bases__属性可以探测一个对象和哪个对象存在is kind of关系。

## 13. Python运行环境初始化   

## 14. Python模块的动态加载机制   
　　
　　同java的package机制，c++的namespace机制一样，python通过module和package机制来实现对系统复杂度的分解，以及保护名字空间不受污染。  
　　python在初始化时，就将一批module加载到了内存中，但是为了使local名字空间能够达到最干净的效果，python并没有将这些符号暴露在当前的local名字空间中，而上需要用户显示地通过import机制通知python。这些预先被加载进内存的module放在sys.modules中。  
　　python的import机制基本上可以分为3个不同的功能：

- python运行时全局module pool的维护和搜索；
- 解析与搜索module路径的树状结构；
- 对不同文件格式的module的动态加载机制；

