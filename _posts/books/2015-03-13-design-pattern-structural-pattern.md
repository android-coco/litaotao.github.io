---
category: books
published: false
layout: post
title: book-3. 设计模式总结之结构型模式
description: 仅仅是记录我个人的读书记录，看官不必在意～
---  

## 
## 1. 适配器模式
　　在设计模式中，适配器模式（英语：adapter pattern）有时候也称包装样式或者包装。将一个类的接口转接成用户所期待的。一个适配使得因接口不兼容而不能在一起工作的类工作在一起，做法是将类别自己的接口包裹在一个已存在的类中。

### 1.1 Python源码示例

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""http://ginstrom.com/scribbles/2008/11/06/generic-adapter-class-in-python/"""

import os

class Dog(object):
    def __init__(self):
        self.name = "Dog"
    def bark(self):
        return "woof!"

class Cat(object):
    def __init__(self):
        self.name = "Cat"
    def meow(self):
        return "meow!"

class Human(object):
    def __init__(self):
        self.name = "Human"
    def speak(self):
        return "'hello'"


class Car(object):
    def __init__(self):
        self.name = "Car"
    def make_noise(self, octane_level):
        return "vroom{0}".format("!" * octane_level)


class Adapter(object):

    """
    Adapts an object by replacing methods.
    Usage:
    dog = Dog
    dog = Adapter(dog, dict(make_noise=dog.bark))
    >>> objects = []
    >>> dog = Dog()
    >>> objects.append(Adapter(dog, make_noise=dog.bark))
    >>> cat = Cat()
    >>> objects.append(Adapter(cat, make_noise=cat.meow))
    >>> human = Human()
    >>> objects.append(Adapter(human, make_noise=human.speak))
    >>> car = Car()
    >>> car_noise = lambda: car.make_noise(3)
    >>> objects.append(Adapter(car, make_noise=car_noise))
    >>> for obj in objects:
    ...     print('A {} goes {}'.format(obj.name, obj.make_noise()))
    A Dog goes woof!
    A Cat goes meow!
    A Human goes 'hello'
    A Car goes vroom!!!
    """

    def __init__(self, obj, **adapted_methods):
        """We set the adapted methods in the object's dict"""
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object"""
        return getattr(self.obj, attr)


def main():
    objects = []
    dog = Dog()
    objects.append(Adapter(dog, make_noise=dog.bark))
    cat = Cat()
    objects.append(Adapter(cat, make_noise=cat.meow))
    human = Human()
    objects.append(Adapter(human, make_noise=human.speak))
    car = Car()
    objects.append(Adapter(car, make_noise=lambda: car.make_noise(3)))

    for obj in objects:
        print("A {0} goes {1}".format(obj.name, obj.make_noise()))


if __name__ == "__main__":
    main()

### OUTPUT ###
# A Dog goes woof!
# A Cat goes meow!
# A Human goes 'hello'
# A Car goes vroom!!!
```


## 2. 桥接模式
　　桥接模式是软件设计模式中最复杂的模式之一，它把事物对象和其具体行为、具体特征分离开来，使它们可以各自独立的变化。事物对象仅是一个抽象的概念。如“圆形”、“三角形”归于抽象的“形状”之下，而“画圆”、“画三角”归于实现行为的“画图”类之下，然后由“形状”调用“画图”。

### 2.1 Python源码示例

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""http://en.wikibooks.org/wiki/Computer_Science_Design_Patterns/Bridge_Pattern#Python"""


# ConcreteImplementor 1/2
class DrawingAPI1(object):

    def draw_circle(self, x, y, radius):
        print('API1.circle at {}:{} radius {}'.format(x, y, radius))


# ConcreteImplementor 2/2
class DrawingAPI2(object):

    def draw_circle(self, x, y, radius):
        print('API2.circle at {}:{} radius {}'.format(x, y, radius))


# Refined Abstraction
class CircleShape(object):

    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    # low-level i.e. Implementation specific
    def draw(self):
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    # high-level i.e. Abstraction specific
    def scale(self, pct):
        self._radius *= pct


def main():
    shapes = (
        CircleShape(1, 2, 3, DrawingAPI1()),
        CircleShape(5, 7, 11, DrawingAPI2())
    )

    for shape in shapes:
        shape.scale(2.5)
        shape.draw()


if __name__ == '__main__':
    main()

### OUTPUT ###
# API1.circle at 1:2 radius 7.5
# API2.circle at 5:7 radius 27.5
```

## 3. 