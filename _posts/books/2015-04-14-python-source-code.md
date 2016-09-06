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

### 14.1 符号的销毁与重载

　　为了使用一个module，都需要通过import将其动态加载到内存中，在使用了这个module之后，可能我们需要将其删除。这样可以释放module占用的内存，也可以避免名字空间过于庞大，以保证在名字空间中搜索某个符号的动作的效率不会成为python程序运行时的瓶颈。通常我们会用del来销毁。但是这样的动作真的能保证module被销毁吗？或者更准确的说，符号的销毁和符号关联的对象的销毁是一个概念吗？python可是采用了很多的缓存策略哦。下面代码帮我们探索了del的真正行为。   

![del-python](../images/del-python.jpg)

　　可以看到，在del之后，tank确实从当前的名字空间里消失了，但消失的仅仅是tank这个符号，其背后的module A.tank已然在python的module缓存中。    

　　reload重载机制，reload一个module时，其在python的module缓存中的地址不变，即python虚拟机并没有创建新的module对象，而且在原来的module中添加新的符号。而且值得注意的是，reload只会像原来的module中添加新的符号，而不管module中的符号是否已经在源文件里被删除了。  

![reload-python](../images/reload-python.jpg)

### 14.3 package, module, py, pyc

　　对于py文件，python虚拟机会先进行编译，而对于pyc文件，python直接可以import，少了编译一步。   
　　对于package，python会调用底层函数load_package，load_package智慧将package自己加载到python中，并不会对package中的module进行任何动作，除非在__init__.py中显示地import语句。在load_package中，find_module和load_module所搜索和加载的都仅仅是__init__.py文件，如果__init__.py为空，那么load_package就不会加载package下任何module，而是沿着调用函数栈一层一层向上返回到import_module_level中，通过下一个load_ext来加载package中的module。   


## 15. Python的多线程机制

　　python中的线程从一开始就是操作系统的原生线程，而python虚拟机也同样使用一个全局解释器锁GIL来互斥线程对python虚拟机的使用。   

### 15.1 GIL与线程调度   

　　为了支持多线程机制，一个基本的要求就是需要实现不同的线程对共享资源访问的互斥，python也不例外。这正是引入GIL的根源所在。Python中的GIL是一个非常霸道的互斥实现。在一个线程拥有了解释器的访问权后，其他的所有线程都必须等他释放解释器的访问权，即使这些线程的下一条指令并不会互相影响。初看上去这样的保护机制粒度太大，我们似乎只要将多个线程共享的资源保护起来即可，对于不会被多个线程共享的资源完全可以不用保护。可实际上，在python的发展历史中，确实出现过这样的解决方案，但是这样的解决方案在单处理器上的多线程实现的效率却没有GIL的方案好。所以现在的python中的多线程机制是在GIL基础上实现的。   
　　当然，GIL方案意味着在同一时间，只能有一个线程能访问Python所提供的API。这里的同一时间对于单处理器是毫无意义的，因为单处理器本质上本可能并行处理。但是对于多处理器，情形就完全不同了，同一时间确实可以有多个线程独立运行，然后GIL限制了这样的情形，使得多处理器最终退化为单处理器，性能大打折扣。曾经有branch去除了GIL限制，但细粒度的锁机制导致了大量的加锁、解锁操作，而加锁、解锁对于操作系统来说是一个比较重量级的操作。  
　　python的线程调度机制，同操作系统的进程调度一样，最关键的是要解决两个问题：   

- 在何时挂起当前线程，选择处于等待状态的下一个线程；
- 在众多处于等待状态的候选线程中，选择激活哪一个线程；

　　在Python的多线程机制中，这两个问题分别是由不同的层次解决的。对于何时进行线程调度的问题，是由python自身决定的。python中模拟了操作系统的时钟中断机制，来激活线程的调度。Python字节码解释器的工作原理是按照指令一条一条顺序执行，python内部维护着一个数值，python的内部时钟【设为N】，意味着python在执行了N条指令以后应该立即启动线程调度机制。可以通过 `sys.getcheckinterval()` 函数来获取当前的N值。    
　　现在我们知道python什么时候进行线程调度，当一个线程获得了访问解释器所必须的GIL进入解释器后，python内部的检测机制就开始启动，当这个线程执行了100条指令之后python解释器强制挂起当前进程，开始切换到下一个处于等待状态的进程。那么究竟python会在众多等待线程中选择哪一个呢？python把这个任务交给了底层的操作系统来解决，即python借用了底层操作系统所提供的线程调度机制来决定下一个进入解释器的线程。这一点至关重要，以为着python重的线程实际上就是操作系统所支持的原生线程。python中的多线程机制正式建立在操作系统的原生线程之上。对应不同的操作系统，有不同的实现。然后再各不相同的原生线程的基础之上，python提供了一套统一的抽象机制，给python的使用者一个非常简单而且方便的多线程工具箱，这就是python中的两个module：thread以及在其之上的threading。    

### 15.2 初见python thread

　　thread是一个builtin module，用c实现，在thread的基础上，python提供了一个更高层的多线程接口，threading，是一个标准库，用python语言实现。

### 15.3 Threading的线程同步工具

　　在thread中提供了用户级别的同步工具：Lock对象，而在threading中，python提供了不同的线程同步工具：   

- RLock：RLock对象是Lock对象的一个变种，其内部维护者一个Lock对象，但是它是一种可重入的Lock。一般的，对于lock对象而言，如果一个线程连续两次进行acquire操作，那么由于第一次acquire之后没有释放，第二次acquire将把线程挂起，这直接导致lock对象永远不会释放，因此线程死锁。Rlock允许一个线程多次对其进行acquire操作，rlock在内部通过一个counter变量维护线程acquire的次数，而且每一次的acquire都有一个release操作与之对应，在所有的release都完成后，别的线程才能申请该rlock对象；  
- Condition：condition对象是对lock对象的包装。在创建condition对象时，其构造函数需要一个lock对象作为参数，如果没有这个lock对象，condition内部将自行创建一个rlock对象。在condition的基础上，当然也可以调用acquire和release操作，因为内部的lock对象本身就支持这些操作。但是condition对象c，当线程a调用c.wait()时，线程a将释放c中的lock对象，并进入阻塞状态，直到有别的线程调用c.notify()，a才会重新通过acquire申请c中的lock对象，并退出wait操作；  
- semaphore：semaphore对象内部维护一个condition对象，对于管理一组共享资源非常有用。lock对象可以保护一个共享资源，但是假如我们有一个共享资源池，其中有5个共享资源a，这意味着可以有5个线程同时自由地访问这些资源。然而如果使用lock来对共享资源进行保护的花，所有线程都将互斥，这使得有4个资源a被浪费了。semaphore提供两个操作，acquire和release操作，都具有和lock相同的语义。当线程调用semaphore.acquire时，如果共享资源池中还有剩余的A时，线程就会继续执行，如果资源池中已经没有存在任何资源了，线程就会将自己挂起，直到别的线程调用semaphore.reslease操作释放一个资源；  
- event：与semaphore类似，event对象实际上也是对condition对象的一种包装，只是提供了独有的set和wait语义；  


## 16. Python的内存管理机制  

### 16.1 小块空间的内存池

　　在python中，许多时候申请的内存都是小块的内存，这些小块内存在申请后，很快又会被释放，由于这些内存的申请并不是为了创建对象，所以并没有对象一级的内存池机制。这意味着python程序在运行期间会大量执行malloc和free操作，导致系统频繁地在用户态和核心态之间进行切换，这将严重影响python的执行效率。为了提高python的执行效率，python引入了一个内存池机制，用于管理对小块内存的申请和释放。

### 16.2 引用计数与垃圾回收  

　　在python中，大多数对象的生命周期都是通过对象的引用计数来管理的。虽然引用计数在每次分配和释放内存的时候加入管理引用计数的动作，然后于其他主流的垃圾回收机制相比，引用计数方法最大的一个优点就是实时性，任何内存，一旦没有指向它的引用，就会立即被回收。执行效率是引用计数机制的一个软肋，但其还存在一个致命弱点：循环引用。要解决这个弱点，必须引入其他垃圾收集计数来打破循环引用，python中引入了主流垃圾回收技术中的标记---清除和分代回收两种技术来填补其内存管理机制中最后的漏洞。  




































## 扫一扫     

![2015-04-14-python-source-code.md](../../images/share/2015-04-14-python-source-code.md.jpg)