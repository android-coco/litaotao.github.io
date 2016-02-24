---
category: books
published: true
layout: post
title: 『 读书笔记 』 设计模式总结之行为型模式
description: 仅仅是记录我个人的读书记录，看官不必在意～
---  

## 1. 迭代器模式
　　提供一种方法访问一个容器对象中各个元素，而又不暴露该对象的内部细节。迭代器模式的结构：

- 抽象容器：一般是一个接口，提供一个iterator()方法，例如java中的Collection接口，List接口，Set接口等。  
- 具体容器：就是抽象容器的具体实现类，比如List接口的有序列表实现ArrayList，List接口的链表实现LinkList，Set接口的哈希列表的实现HashSet等。
- 抽象迭代器：定义遍历元素所需要的方法，一般来说会有这么三个方法：取得第一个元素的方法first()，取得下一个元素的方法next()，判断是否遍历结束的方法isDone()（或者叫hasNext()），移出当前对象的方法remove(),
- 迭代器实现：实现迭代器接口中定义的方法，完成集合的迭代。

### 1.1 Python源码实例

{% highlight python %}

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/
Implementation of the iterator pattern with a generator"""


def count_to(count):
    """Counts by word numbers, up to a maximum of five"""
    numbers = ["one", "two", "three", "four", "five"]
    # enumerate() returns a tuple containing a count (from start which
    # defaults to 0) and the values obtained from iterating over sequence
    for pos, number in zip(range(count), numbers):
        yield number

# Test the generator
count_to_two = lambda: count_to(2)
count_to_five = lambda: count_to(5)

print('Counting to two...')
for number in count_to_two():
    print(number, end=' ')

print()

print('Counting to five...')
for number in count_to_five():
    print(number, end=' ')

print()

### OUTPUT ###
# Counting to two...
# one two
# Counting to five...
# one two three four five
{% endhighlight %}

## 2. 观察者模式
　　观察者模式（有时又被称为发布/订阅模式）是软件设计模式的一种。在此种模式中，一个目标对象管理所有相依于它的观察者对象，并且在它本身的状态改变时主动发出通知。这通常透过呼叫各观察者所提供的方法来实现。此种模式通常被用来实作事件处理系统。

### 2.1 Python源码示例

{% highlight python %}

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Reference: http://www.slideshare.net/ishraqabd/publish-subscribe-model-overview-13368808
Author: https://github.com/HanWenfang
"""


class Provider:

    def __init__(self):
        self.msg_queue = []
        self.subscribers = {}

    def notify(self, msg):
        self.msg_queue.append(msg)

    def subscribe(self, msg, subscriber):
        if msg not in self.subscribers:
            self.subscribers[msg] = []
            self.subscribers[msg].append(subscriber)  # unfair
        else:
            self.subscribers[msg].append(subscriber)

    def unsubscribe(self, msg, subscriber):
        self.subscribers[msg].remove(subscriber)

    def update(self):
        for msg in self.msg_queue:
            if msg in self.subscribers:
                for sub in self.subscribers[msg]:
                    sub.run(msg)
        self.msg_queue = []


class Publisher:

    def __init__(self, msg_center):
        self.provider = msg_center

    def publish(self, msg):
        self.provider.notify(msg)


class Subscriber:

    def __init__(self, name, msg_center):
        self.name = name
        self.provider = msg_center

    def subscribe(self, msg):
        self.provider.subscribe(msg, self)

    def run(self, msg):
        print("{} got {}".format(self.name, msg))


def main():
    message_center = Provider()

    fftv = Publisher(message_center)

    jim = Subscriber("jim", message_center)
    jim.subscribe("cartoon")
    jack = Subscriber("jack", message_center)
    jack.subscribe("music")
    gee = Subscriber("gee", message_center)
    gee.subscribe("movie")

    fftv.publish("cartoon")
    fftv.publish("music")
    fftv.publish("ads")
    fftv.publish("movie")
    fftv.publish("cartoon")
    fftv.publish("cartoon")
    fftv.publish("movie")
    fftv.publish("blank")

    message_center.update()


if __name__ == "__main__":
    main()

### OUTPUT ###
# jim got cartoon
# jack got music
# gee got movie
# jim got cartoon
# jim got cartoon
# gee got movie

{% endhighlight %}


## 3. 策略模式
　　策略模式作为一种软件设计模式，指对象有某个行为，但是在不同的场景中，该行为有不同的实现算法。比如每个人都要“交个人所得税”，但是“在美国交个人所得税”和“在中国交个人所得税”就有不同的算税方法。主要是应对：在软件构建过程中，某些对象使用的算法可能多种多样，经常发生变化。如果在对象内部实现这些算法，将会使对象变得异常复杂，甚至会造成性能上的负担。GoF《设计模式》中说道：定义一系列算法，把它们一个个封装起来，并且使它们可以相互替换。该模式使得算法可独立于它们的客户变化。    

### 3.1 Python 源码示例

{% highlight python %}

class Duck(object):
    # 上面使用继承，这里通用的使用参数方式，传入的就是操作工厂的类
    def __init__(self, strategy=None):
        self.action = None
        self.count = 0
        if strategy:
            # 指定策略，那么执行action就是用这个类的实例
            self.action = strategy()

    def fly(self, kind):
        if self.action:
            self.count += 1
            # 这里的第二个参数self，算是炫技吧，就是为了让操作的方法获得这里计算好的count
            return self.action.fly(kind, self)

        else:
            raise UnboundLocalError('Exception raised, no strategyClass supplied to Duck!')

# 注意这里没有继承Duck，因为是以参数的方式传入类名
class Duck1(object):

    def fly(self, kind, instance):
        return 'Duck1 fly kind: ' + kind + '#' + str(instance.count)


class Duck2(object):

    def fly(self, kind, instance):
        return 'Duck2 fly kind: ' + kind + '#' + str(instance.count)


if __name__ == '__main__':
    duckfly = Duck()
    duck1fly = Duck(strategy=Duck1)
    duck2fly = Duck(strategy=Duck2)

    try:
        print duckfly.fly('yes')
    except Exception as e:
        print "The following exception was expected:"
        print e

    print duck1fly.fly('yes')
    print duck1fly.fly('no')
    print duck1fly.fly('yes')
    print duck2fly.fly('yes')
    print duck2fly.fly('no')

{% endhighlight %}



## 4. 模板方法模式
　　模板方法模式定义了一个算法的步骤，并允许次类别为一个或多个步骤提供其实践方式。让次类别在不改变算法架构的情况下，重新定义算法中的某些步骤。在软件工程中，它是一种软件设计模式，和C++模板没有关连。也可以理解为定义一个操作中的算法的骨架，而将一些步骤延迟到子类中。因此模板方法使得子类可以在不改变一个算法的结构的情况下重新定义该算法的某些特定变量。优点是把不变行为搬移到超类，去除子类中的重复代码。

### 4.1 Python源码示例
　　源码来自[csdn.net](http://blog.csdn.net/five3/article/details/7564578)

{% highlight python %}

#!/usr/bin/env python  
#encoding: utf-8  

class template:
    def __init__(self):
        pass
    
    def logic(self):
        print 'do something before ....'
        print self.do_something_now()
        print 'do something after ....'
        
    def do_something_now(self):
        return None      
        
class apply_temp1(template):
    def __init__(self):
        pass
    
    def do_something_now(self):
        return 'apply 1'  
    
class apply_temp2(template):
    def __init__(self):
        pass
    
    def do_something_now(self):
        return 'apply 2'  

          
if '__main__' == __name__:  
    obj1 = apply_temp1()
    obj2 = apply_temp2()
    obj1.logic()
    obj2.logic()
    print obj1.__class__
    print obj2.__class__

{% endhighlight %}


## 扫一扫     

![2015-03-12-design-pattern-behavior-pattern.md](../../images/share/2015-03-12-design-pattern-behavior-pattern.md.jpg)