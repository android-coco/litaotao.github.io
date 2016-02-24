---
category: books
published: true
layout: post
title: 『 读书笔记 』 设计模式总结之创建型模式
description: 仅仅是记录我个人的读书记录，看官不必在意～
---  

## 1. 抽象工厂模式
　　抽象工厂模式（英语：Abstract factory pattern）是一种软件开发设计模式。抽象工厂模式提供了一种方式，可以将一组具有同一主题的单独的工厂封装起来。在正常使用中，客户端程序需要创建抽象工厂的具体实现，然后使用抽象工厂作为接口来创建这一主题的具体对象。客户端程序不需要知道（或关心）它从这些内部的工厂方法中获得对象的具体类型，因为客户端程序仅使用这些对象的通用接口。抽象工厂模式将一组对象的实现细节与他们的一般使用分离开来。

　　举个例子来说，比如一个抽象工厂类叫做DocumentCreator（文档创建器），此类提供创建若干种产品的接口，包括createLetter()（创建邮件）和createResume()（创建简历）。其中，createLetter()返回一个Letter（邮件），createResume()返回一个Resume（简历）。系统中还有一些DocumentCreator的具体实现类，包括FancyDocumentCreator和ModernDocumentCreator。这两个类对DocumentCreator的两个方法分别有不同的实现，用来创建不同的“邮件”和“简历”（用FancyDocumentCreator的实例可以创建FancyLetter和FancyResume，用ModernDocumentCreator的实例可以创建ModernLetter和ModernResume）。这些具体的“邮件”和“简历”类均继承自抽象类，即Letter和Resume类。客户端需要创建“邮件”或“简历”时，先要得到一个合适的DocumentCreator实例，然后调用它的方法。一个工厂中创建的每个对象都是同一个主题的（“fancy”或者“modern”）。客户端程序只需要知道得到的对象是“邮件”或者“简历”，而不需要知道具体的主题，因此客户端程序从抽象工厂DocumentCreator中得到了Letter或Resume类的引用，而不是具体类的对象引用。

　　“工厂”是创建产品（对象）的地方，其目的是将产品的创建与产品的使用分离。抽象工厂模式的目的，是将若干抽象产品的接口与不同主题产品的具体实现分离开。这样就能在增加新的具体工厂的时候，不用修改引用抽象工厂的客户端代码。

　　使用抽象工厂模式，能够在具体工厂变化的时候，不用修改使用工厂的客户端代码，甚至是在运行时。然而，使用这种模式或者相似的设计模式，可能给编写代码带来不必要的复杂性和额外的工作。正确使用设计模式能够抵消这样的“额外工作”。

### 1.1 Python 源码示例

　　源码来自[github:python-patterns](https://github.com/faif/python-patterns/)

{% highlight python %}

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/

"""Implementation of the abstract factory pattern"""

import random

class PetShop:

    """A pet shop"""

    def __init__(self, animal_factory=None):
        """pet_factory is our abstract factory.  We can set it at will."""

        self.pet_factory = animal_factory

    def show_pet(self):
        """Creates and shows a pet using the abstract factory"""

        pet = self.pet_factory.get_pet()
        print("We have a lovely {}".format(pet))
        print("It says {}".format(pet.speak()))
        print("We also have {}".format(self.pet_factory.get_food()))


# Stuff that our factory makes

class Dog:

    def speak(self):
        return "woof"

    def __str__(self):
        return "Dog"


class Cat:

    def speak(self):
        return "meow"

    def __str__(self):
        return "Cat"


# Factory classes

class DogFactory:

    def get_pet(self):
        return Dog()

    def get_food(self):
        return "dog food"


class CatFactory:

    def get_pet(self):
        return Cat()

    def get_food(self):
        return "cat food"

# Create the proper family
def get_factory():
    """Let's be dynamic!"""
    return random.choice([DogFactory, CatFactory])()


# Show pets with various factories
if __name__ == "__main__":
    for i in range(3):
        shop = PetShop(get_factory())
        shop.show_pet()
        print("=" * 20)

### OUTPUT ###
# We have a lovely Dog
# It says woof
# We also have dog food
# ====================
# We have a lovely Dog
# It says woof
# We also have dog food
# ====================
# We have a lovely Cat
# It says meow
# We also have cat food
# ====================

{% endhighlight %}

## 2.工厂方法模式
　　工厂方法模式（英语：Factory method pattern）是一种实现了“工厂”概念的面向对象设计模式。就像其他创建型模式一样，它也是处理在不指定对象具体类型的情况下创建对象的问题。工厂方法模式的实质是“定义一个创建对象的接口，但让实现这个接口的类来决定实例化哪个类。工厂方法让类的实例化推迟到子类中进行。”

　　创建一个对象常常需要复杂的过程，所以不适合包含在一个复合对象中。创建对象可能会导致大量的重复代码，可能会需要复合对象访问不到的信息，也可能提供不了足够级别的抽象，还可能并不是复合对象概念的一部分。工厂方法模式通过定义一个单独的创建对象的方法来解决这些问题。由子类实现这个方法来创建具体类型的对象。

　　对象创建中的有些过程包括决定创建哪个对象、管理对象的生命周期，以及管理特定对象的创建和销毁的概念。

　　如果抛开设计模式的范畴，“工厂方法”这个词也可以指作为“工厂”的方法，这个方法的主要目的就是创建对象，而这个方法不一定在单独的工厂类中。这些方法通常作为静态方法，定义在方法所实例化的类中。

　　每个工厂方法都有特定的名称。在许多面向对象的编程语言中，构造方法必须和它所在的类具有相同的名称，这样的话，如果有多种创建对象的方式（重载）就可能导致歧义。工厂方法没有这种限制，所以可以具有描述性的名称。举例来说，根据两个实数创建一个复数，而这两个实数表示直角坐标或极坐标，如果使用工厂方法，方法的含义就非常清晰了。当工厂方法起到这种消除歧义的作用时，构造方法常常被设置为私有方法，从而强制客户端代码使用工厂方法创建对象。

### 2.1 Python 源码示例

　　源码来自[github:python-patterns](https://github.com/faif/python-patterns/)

{% highlight python %}

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/"""


class GreekGetter:

    """A simple localizer a la gettext"""

    def __init__(self):
        self.trans = dict(dog="σκύλος", cat="γάτα")

    def get(self, msgid):
        """We'll punt if we don't have a translation"""
        try:
            return self.trans[msgid]
        except KeyError:
            return str(msgid)


class EnglishGetter:

    """Simply echoes the msg ids"""

    def get(self, msgid):
        return str(msgid)


def get_localizer(language="English"):
    """The factory method"""
    languages = dict(English=EnglishGetter, Greek=GreekGetter)
    return languages[language]()

# Create our localizers
e, g = get_localizer(language="English"), get_localizer(language="Greek")
# Localize some text
for msgid in "dog parrot cat bear".split():
    print(e.get(msgid), g.get(msgid))

### OUTPUT ###
# dog σκύλος
# parrot parrot
# cat γάτα
# bear bear

{% endhighlight %}


## 3. 单例模式
　　单例模式，也叫单子模式，是一种常用的软件设计模式。在应用这个模式时，单例对象的类必须保证只有一个实例存在。许多时候整个系统只需要拥有一个的全局对象，这样有利于我们协调系统整体的行为。比如在某个服务器程序中，该服务器的配置信息存放在一个文件中，这些配置数据由一个单例对象统一读取，然后服务进程中的其他对象再通过这个单例对象获取这些配置信息。这种方式简化了在复杂环境下的配置管理。

　　实现单例模式的思路是：一个类能返回对象一个引用(永远是同一个)和一个获得该实例的方法（必须是静态方法，通常使用getInstance这个名称）；当我们调用这个方法时，如果类持有的引用不为空就返回这个引用，如果类保持的引用为空就创建该类的实例并将实例的引用赋予该类保持的引用；同时我们还将该类的构造函数定义为私有方法，这样其他处的代码就无法通过调用该类的构造函数来实例化该类的对象，只有通过该类提供的静态方法来得到该类的唯一实例。

　　单例模式在多线程的应用场合下必须小心使用。如果当唯一实例尚未创建时，有两个线程同时调用创建方法，那么它们同时没有检测到唯一实例的存在，从而同时各自创建了一个实例，这样就有两个实例被构造出来，从而违反了单例模式中实例唯一的原则。 解决这个问题的办法是为指示类是否已经实例化的变量提供一个互斥锁(虽然这样会降低效率)。

### 3.1 Python源码示例
　　源码来自[csdn.net](http://blog.csdn.net/ghostfromheaven/article/details/7671853)

{% highlight python %}

#-*- encoding=utf-8 -*-
print '----------------------方法1--------------------------'
#方法1,实现__new__方法
#并在将一个类的实例绑定到类变量_instance上,
#如果cls._instance为None说明该类还没有实例化过,实例化该类,并返回
#如果cls._instance不为None,直接返回cls._instance
class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

class MyClass(Singleton):
    a = 1

one = MyClass()
two = MyClass()

two.a = 3
print one.a
#3
#one和two完全相同,可以用id(), ==, is检测
print id(one)
#29097904
print id(two)
#29097904
print one == two
#True
print one is two
#True

print '----------------------方法2--------------------------'
#方法2,共享属性;所谓单例就是所有引用(实例、对象)拥有相同的状态(属性)和行为(方法)
#同一个类的所有实例天然拥有相同的行为(方法),
#只需要保证同一个类的所有实例具有相同的状态(属性)即可
#所有实例共享属性的最简单最直接的方法就是__dict__属性指向(引用)同一个字典(dict)
#可参看:http://code.activestate.com/recipes/66531/
class Borg(object):
    _state = {}
    def __new__(cls, *args, **kw):
        ob = super(Borg, cls).__new__(cls, *args, **kw)
        ob.__dict__ = cls._state
        return ob

class MyClass2(Borg):
    a = 1

one = MyClass2()
two = MyClass2()

#one和two是两个不同的对象,id, ==, is对比结果可看出
two.a = 3
print one.a
#3
print id(one)
#28873680
print id(two)
#28873712
print one == two
#False
print one is two
#False
#但是one和two具有相同的（同一个__dict__属性）,见:
print id(one.__dict__)
#30104000
print id(two.__dict__)
#30104000

print '----------------------方法3--------------------------'
#方法3:本质上是方法1的升级（或者说高级）版
#使用__metaclass__（元类）的高级python用法
class Singleton2(type):
    def __init__(cls, name, bases, dict):
        super(Singleton2, cls).__init__(name, bases, dict)
        cls._instance = None
    def __call__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = super(Singleton2, cls).__call__(*args, **kw)
        return cls._instance

class MyClass3(object):
    __metaclass__ = Singleton2

one = MyClass3()
two = MyClass3()

two.a = 3
print one.a
#3
print id(one)
#31495472
print id(two)
#31495472
print one == two
#True
print one is two
#True

print '----------------------方法4--------------------------'
#方法4:也是方法1的升级（高级）版本,
#使用装饰器(decorator),
#这是一种更pythonic,更elegant的方法,
#单例类本身根本不知道自己是单例的,因为他本身(自己的代码)并不是单例的
def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton

@singleton
class MyClass4(object):
    a = 1
    def __init__(self, x=0):
        self.x = x

one = MyClass4()
two = MyClass4()

two.a = 3
print one.a
#3
print id(one)
#29660784
print id(two)
#29660784
print one == two
#True
print one is two
#True
one.x = 1
print one.x
#1
print two.x
#1

{% endhighlight %}


## 扫一扫     

![2015-03-11-design-pattern-create-pattern.md](../../images/share/2015-03-11-design-pattern-create-pattern.md.jpg)