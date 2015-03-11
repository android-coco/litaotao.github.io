---
category: books
published: false
layout: post
title: book-3. 设计模式总结之创建型模式
description: 仅仅是记录我个人的读书记录，看官不必在意～
---  



## 
## 1. 抽象工厂模式
　　抽象工厂模式（英语：Abstract factory pattern）是一种软件开发设计模式。抽象工厂模式提供了一种方式，可以将一组具有同一主题的单独的工厂封装起来。在正常使用中，客户端程序需要创建抽象工厂的具体实现，然后使用抽象工厂作为接口来创建这一主题的具体对象。客户端程序不需要知道（或关心）它从这些内部的工厂方法中获得对象的具体类型，因为客户端程序仅使用这些对象的通用接口。抽象工厂模式将一组对象的实现细节与他们的一般使用分离开来。

　　举个例子来说，比如一个抽象工厂类叫做DocumentCreator（文档创建器），此类提供创建若干种产品的接口，包括createLetter()（创建邮件）和createResume()（创建简历）。其中，createLetter()返回一个Letter（邮件），createResume()返回一个Resume（简历）。系统中还有一些DocumentCreator的具体实现类，包括FancyDocumentCreator和ModernDocumentCreator。这两个类对DocumentCreator的两个方法分别有不同的实现，用来创建不同的“邮件”和“简历”（用FancyDocumentCreator的实例可以创建FancyLetter和FancyResume，用ModernDocumentCreator的实例可以创建ModernLetter和ModernResume）。这些具体的“邮件”和“简历”类均继承自抽象类，即Letter和Resume类。客户端需要创建“邮件”或“简历”时，先要得到一个合适的DocumentCreator实例，然后调用它的方法。一个工厂中创建的每个对象都是同一个主题的（“fancy”或者“modern”）。客户端程序只需要知道得到的对象是“邮件”或者“简历”，而不需要知道具体的主题，因此客户端程序从抽象工厂DocumentCreator中得到了Letter或Resume类的引用，而不是具体类的对象引用。

　　“工厂”是创建产品（对象）的地方，其目的是将产品的创建与产品的使用分离。抽象工厂模式的目的，是将若干抽象产品的接口与不同主题产品的具体实现分离开。这样就能在增加新的具体工厂的时候，不用修改引用抽象工厂的客户端代码。

　　使用抽象工厂模式，能够在具体工厂变化的时候，不用修改使用工厂的客户端代码，甚至是在运行时。然而，使用这种模式或者相似的设计模式，可能给编写代码带来不必要的复杂性和额外的工作。正确使用设计模式能够抵消这样的“额外工作”。

### 1.1 Python 源码示例

　　源码来自[github:python-patterns](https://github.com/faif/python-patterns/)

```
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
```


## 2.工厂方法模式
　　工厂方法模式（英语：Factory method pattern）是一种实现了“工厂”概念的面向对象设计模式。就像其他创建型模式一样，它也是处理在不指定对象具体类型的情况下创建对象的问题。工厂方法模式的实质是“定义一个创建对象的接口，但让实现这个接口的类来决定实例化哪个类。工厂方法让类的实例化推迟到子类中进行。”

　　创建一个对象常常需要复杂的过程，所以不适合包含在一个复合对象中。创建对象可能会导致大量的重复代码，可能会需要复合对象访问不到的信息，也可能提供不了足够级别的抽象，还可能并不是复合对象概念的一部分。工厂方法模式通过定义一个单独的创建对象的方法来解决这些问题。由子类实现这个方法来创建具体类型的对象。

　　对象创建中的有些过程包括决定创建哪个对象、管理对象的生命周期，以及管理特定对象的创建和销毁的概念。

　　如果抛开设计模式的范畴，“工厂方法”这个词也可以指作为“工厂”的方法，这个方法的主要目的就是创建对象，而这个方法不一定在单独的工厂类中。这些方法通常作为静态方法，定义在方法所实例化的类中。

　　每个工厂方法都有特定的名称。在许多面向对象的编程语言中，构造方法必须和它所在的类具有相同的名称，这样的话，如果有多种创建对象的方式（重载）就可能导致歧义。工厂方法没有这种限制，所以可以具有描述性的名称。举例来说，根据两个实数创建一个复数，而这两个实数表示直角坐标或极坐标，如果使用工厂方法，方法的含义就非常清晰了。当工厂方法起到这种消除歧义的作用时，构造方法常常被设置为私有方法，从而强制客户端代码使用工厂方法创建对象。

### 2.1 Python 源码示例

　　源码来自[github:python-patterns](https://github.com/faif/python-patterns/)

```
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
```