---
category: python
published: true
layout: post
title: 『 读书笔记 』effective Python
description: Python 技巧总结~
---


## 1. Pythonic Thinking

### 1.1 know which version of python you're using

- two major python version;
- multiple popular `runtimes` for python: cpython, jython, ironpython, pypy, etc;
- be sure that the command line for running python on your system is the version you want;
- prefer python 3 in your next project;

### 1.2 follow the pep 8 style guide

- always follow the pep 8 style guide;
- sharing a common style with the larger community facilitates collaboration with others;
- using a consistent style, making it easier to maintain your code later;

### 1.3 know the differences between bytes, str and unicode

- [PYTHON-进阶-编码处理小结](http://wklken.me/posts/2013/08/31/python-extra-coding-intro.html)
- [python encode和decode函数说明](http://www.cnblogs.com/evening/archive/2012/04/19/2457440.html)
- in python 3, bytes contains sequences of 8-bit values, str contains sequences of unicode characters. bytes and str instances can't be used together with operators.
- in python 2, str contains sequences of 8-bit, unicode contains sequences of unicode characters. str and unicode can be used together with operators if the str only contains 7-bit ascii characters;
- if you want to read or write binary data to/from a file, always open the file using a binary mode (like 'rb', 'wb');

### 1.4 wirte helper functions instead of complex expressions

- python's syntax make it easy to write a single line expression that are overly difficult to read;
- move complex single line expressions to helper functions;
- the `if/else` expression make it more readable to alternative using bool operators like `and` and `or`;

### 1.5 know how to slice sequence

- avoid being verbose, do not use [0] and [len(sequence)] to fetch the first or end element of a sequence;
- assign to a list slice will replace the origin data in that slice part even if the new data's length does not equal with the old one;

### 1.6 avoid using start, end and stride in a single slice

- specifying start, end and stride in a slice can be extremely confusing;
- avoid negative stride if possible;
- avoid using start, end and stride in a single slice, consider doing two assignments(one to slice, the other to stride) or using islice from the itertools module;

### 1.7 use list comprehension instead of map and filter

- list comprehension is more clearer than map and filter because it does not need another `lambda` expression;
- list comprehension allows to skip items from the input list, but map can not make that without using `filter`;
- dict and set also support comprehension;

### 1.8 avoid more than two expressions in list comprehension

- list comprehension support multiple levels of loops and multiple conditions per loop;
- list comprehension with two expressions are difficult to read in some degree;

### 1.9 consider generator for large list comprehension

- list comprehension can consume large memory for large input;
- generator can avoid memory issues by produce one item each time;
- generator can execute very quickly when chained together;


### 1.10 prefer enumerate over range

{% highlight python%}

for index, item in enumerate(list):
    print 'index : {}, item : {}'.format(index, item)

{% endhighlight %}

- enumerate provides a concise syntax for looping an iterator and getting the index for each item;
- prefer enumerate instead looping over a range and indexing for each item;
- you can specify a number to the enumerate function, specifying the index you want to iterate with;


### 1.11 use zip to process iterators in parallel

- the `zip` can be used to iterate over multiple iterators;
- in python 3, `zip` is a lazy generator, in python 2, `zip` return all the results as a list, but you can use `izip` from `itertools` to make it a generator;
- `zip` truncates it's output silently if you supply it with different length, if you cannot lose any data, use the `zip_longest` from `itertools`;

### 1.12 avoid else blocks after for and while loops

### 1.13 take advantage of each block in try/except/else/finally

- the `try/finally` statements let you run cleanup code regardless whether there is exceptions in your `try` block or not;


## 2. functions


### 2.1 prefering exceptions to return none

- functions that return `None` to indicate special meaning are error prone beacause `None` and other values (0, empty string, etc) are evaluated to `False` in the conditional expression;
- Raise exceptions to indicate special situations instead of returning `None`, expect the calling code to handle the exceptions properly;

### 2.2 know how closures interactive with variable scope

{% highlight python%}

In [1]: def sort_priority(values, group):
   ...:         def helper(x):
   ...:                 if x in group:
   ...:                         return (0, x)
   ...:                 return (1, x)
   ...:         values.sort(key=helper)
   ...:

In [2]: values = [8, 3, 1, 2, 5, 4, 7, 6]

In [3]: group = [2, 3, 5, 7]

In [4]: sort_priority(values, group)

In [5]: values
Out[5]: [2, 3, 5, 7, 1, 4, 6, 8]

{% endhighlight %}

- python supports closures: functions that refer to variables from the scope in which they were defined. this is why helper function is able to access the group argument to `sort_priority`;
- functions are first-class objects in python, meaning you can refer to them directly, assign them to variables, pass them as arguments to other functions, compare them in expressions and if statements, etc. this is how the sort method can accept a closure function as the key argument;
- python has specific rules for comparing tuples. it first compares items in index zero, then index one and so on. this is why the return value from the helper closure causes the sort order to have two distinct groups.
- when you refer a variable in an expression, the python interpreter will traverse the scope to resolve the reference in this order:
    + the current function's scope;
    + any enclosing scope(like other containing functions)
    + the scope of the module that contains the code(also called the global scope)
    + the built-in scope

### 2.3 consider generators instead of returning list

- using generators can be clearer than the alternative of returning lists of accumulated results;
- the iterator returned by a generator produces the set of values passed to yield expressions within the generator funtions' body;
- generators can produce a sequence of outputs for arbitrarily large inputs because their working memory doesn't include all inputs and outputs;

### 2.4 be defensive when iterating over arguments

### 2.5 reduce visual noise with variable positional arguments

- functions can accept a variable number of positional arguments by using `*args` in the def statement;
- you can use the items from a sequence as the posistional arguments for a function with the `*` operator;
- using the `*` operator with a generator may cause your program to ran out of memory and crash;
- adding new positional parameters to functions that accept `*args` can introduce hard-to-find bugs;

### 2.6 provide optional behavior with keyword argument

- function arguments can be positional or keyword arguments;
- keyword arguments will make it clear when it will be confusing only using positional arguments;
- keyword arguments with default values make it easy to add new behaviors, especially there exists some callers;
- optional keyword should always be passed using keyword argument other than positional argument;

### 2.7 use none and docstrings to specify dynamic default arguments

{% highlight python%}

# when the function is defined, default argument values are evaluated just once per module at the loading time.

def log(msg, time=datetime.now()):
    print 'msg: {}, time: {}'.format(msg, time)

def log_version(msg, time=None):
    msg_time = time if time else datetime.now()
    print 'msg: {}, time: {}'.format(msg, msg_time)

{% endhighlight%}

- use None for default value is especially important when the argument is mutable;
- default argument values are only evaluated once;

### 2.8 enforce clarity with keyword only argument

- keyword argument make the intention of the function more clear;
- prefer to use keyword arguments if possible, especially when there are many boolean flag arguments;
- python 3 supports explicit syntax for keyword only arguments in functions;
- python 2 can emulate keyword only argument by using `**kwargs` and manually throw `TypeError` exception;

## 3. Classes and Inheritance

### 3.1 prefer helper classes over bookkeeping with dictionaries and tuples

- avoid making dicts with values that are other dicts or long tuple;
- use namedtuple for lightweight, immutable data containers before you need the flexibility of full class;
- move your bookkeeping code to use multiple helper classes when your internal state dicts get complicated;

### 3.2 accept functions for simple interfaces instead of classes

- instead of defining classes, functions are often all you need for simple interfaces between components in python;
- references to functions and methods in python are first class, meaning they can be used in expressions like any other type;
- the `__call__` special method enables instances of a class to be called like plain python functions;
- when you need a function to maintain state, consider defining a class that provides the `__call__` method instead of defining a stateful closure.


### 3.3 use @classmethod polymorphism to construct objects generically

- python only supports a single constructor per class, the `__init__` method;
- use @classmethod to define alternative constructors for your classes;
- use class method polymorphism to provide generic ways to build and connect concrete subclasses;

### 3.4 initialized parent classes with super

- python's standard method to resolution order (MRO) solves the problems of superclass init order and diamond inheritance;
- always use the super built-in function to init parent classes;


### 3.5 use multiple inheritance only for mix-in utility classes

- avoid using multiple inheritance if mix-in classes can achieve the same outcome;
- use pluggable behaviors at the instance level to provide per-class customization when mix-in classes may require it;
- compose mix-ins to create complex functionality from simple behaviors;

### 3.6 prefer public attributes over private ones

- private attributes aren't rigorously enforced by the python compiler;
- plan from the beginning to allow subclasses to do more with your internal APIs and attributes instead of locking them out by default;
- use documentation of protected fields to guide subclasses instead of trying to force access control with private attributes;
- only consider using private attributes to avoid naming conflicts with subclasses that are out of your control;


### 3.7 inherit from collections.abc for custom container types

- inherit directly from python's container types (list, dict) for simple use cases;
- beaware of the large number of methods required to implement custom container types correctly;
- have your custom container types inherit from the interfaces defined in collections.abc to ensure that your classes match required interfaces and behaviors;

## 4. metaclasses and attributes

### 4.1 use plain attributes instead of get and set methods

- define new class interfaces using simple public attributes and avoid set and get methods;
- use @property to define special behavior when attributes are accessed on your objects, if necessary;
- follow the rule of least surprise and avoid weird side effects in your @property methods;
- ensure that @property methods are fast, do slow or complex work using normal methods;

### 4.2 consider @property instead of refactoring attributes

- use @property to give existing instance attributes new functionality;
- make incremental progress toward better data models by using @property;
- consider refactoring a class and all call sites when you find yourself using @property too heavily;

### 4.3 use descriptors for reusable @property methods

- reuse the behavior and validation of @property methods by defining your own descriptor classes;
- use WeakKeyDict to ensure that your descriptor classes don't cause memory leaks;
- don't get bogged down trying to understand exactly how `__getattribute__` uses the descriptor protocol for getting and setting attrbutes;

### 4.4 use `__getattr__`, `__getattribute__`, and `__setattr__` for lazy attributes

- use `__getattr__` and `__setattr__` to lazily load and save attributes for an object;
- understand that `__getattr__` only gets called once when accessing a missing attribute, whereas `__getattribute__` gets called every time an attribute is accessed;
- avoid infinite recursion in `__getattribute__` and `__setattr__` by using methods from super() to access instance attributes directly;


### 4.5 validate subclass with metaclass

- use metaclasses to ensure that subclasses are well formed at the time they are defined, before objects of their type are constructed;
- metaclasses have slightly different syntax in python 2 and python 3;
- the `__new__` method of metaclasses is run after the class statement's entire body has been processed;

### 4.6 register class existence with metaclasses

- class registeration is a helpful pattern for building modular python programs;
- metaclasses let you run register code automatically each time your base class is subclassed in a program;
- using metaclasses for class register avoids errors by ensuring that you never miss a register call;

### 4.7 annotate class attributes with metaclasses

- metaclasses enable you to modify a class's attributes before the class is fully defined;
- descriptors and metaclasses make a powerful combination for declarative behavior and runtime introspection;
- you can avoid both memory leaks and the weakref module by using metaclasses along with descriptors;

## 5. concurrenc and parallelism

### 5.1 use subprocess to manage child processes

- use the subprocess module to run child processes and manage their input and output manually;
- child processes run in parallel with the python interpreter, enabling you to maximize your cpu usage;
- use the timeout parameter with communicate to avoid deadlocks and hanging child proceses;

### 5.2 use threads for blocking i/o, avoid for parallelism

- python threads can't run bytecode in parallel on multiple cpu cores because of the glow interpreter lock;
- python threads are still useful despite the gil because they provide an easy way to do multiple things at seemingly the same time;
- use python threads to make multiple system calls in parallel, this allows you to do blocking io at the same time as computation;

### 5.3 use lock to prevent data races in threads

- even though python has global interpreter lock, you're still responsible for protecting against data races between the threads in your programs;
- your programs will corrupt their data structures if you allow multiple threads to modify the same objects without locks;
- the lock class in the threading built-in module is python's standard mutual exclusion lock implementation;

### 5.4 use queue to coordinate work between threads

- pipelines are a great way to organize sequences of work that run concurrently using multiple python threads;
- be aware of the many problems in building concurrent pipelines: busy waiting, stopping workers and memory explosion;
- the queue class has all of the facilities you need to build robust pipelines: blocking operations, buffer sizes and joining;

### 5.5 consider coroutines to run many functions concurrently

- coroutines provie an efficient way to run tens of thousands of functions seemingly at the same time;
- within a generator, the value of the yield expression will be whatever value was passed to the generator's send method from the exterior code;
- coroutines give you a powerful tool for separating the core logic of your program from its interaction with the surrounding environment;
- python 2 doesn't support yield from or returning values from generators;

### 5.6 consider concurrent.futures for true parallelism

- moving cpu bottlenecks to c-extension modules can be an effective way to improve performance while maximizing your investment in python code. however, the cost of doing so is high and may introduce bugs;
- the multiprocessing module provides powerful tools that can parallelize certain types of python computation with minimal effort;
- the power of multiprocessing is best accessed through the concurrent.futures built-in module and its simple processpollexecutor class;
- the advanced parts of the multiprocessing module should be avoided because they are so complex;

## 6. built-in modules

### 6.1 define functions decorators with functools.wraps

- decorators are python syntax for allowing one function to modify another function at runtime;
- using decorators can cause strange behaviors in tools that do introspection, such as debuggers;
- use the `wraps` decorator from the `functools` built-in modules when you define your own decorators to avoid any issues;

### 6.2 consider contextlib and with statements for reusable try/finally behavior

- the with statement allow you to reuse logic from try/finally blocks and reduce visual noise;
- the contextlib built-in module provides a contextmanager decorator that makes it easy to use your own functions in with statements;
- the value yielded by context managers is supplied to the as part of the with statement. it's useful for letting your code directly access the cause of the special context;

### 6.3 make pickle reliable with copyreg

{% highlight python%}

the pickle module's serialization format is unsafe by design. the serialzed data contains what is essentially a program that describes how to reconstruct the original python object. this means a malicious pickle payload could be used to compromise any part of the python program that attempts to deserialize it.

{% endhighlight %}

- the pickle module is only useful for serializing and deserializing objects between trusted programs;
- the pickle module may break down when used for more than trivial use cases;
- use the copyreg built-in module with pickle to add missing attribute values, allow versioning of classes, and provide stable import paths;

### 6.4 use datetime instead of time for local clocks

- avoid using the time module for translating between different time zones;
- use the datetime built-in module along with the pytz module to reiliably convert between times in different time zones;
- always represent time in utc and do conversions to local time as the final step before presentation;

### 6.5 use built-in algorithms and data structures

- use python's built-in modules for algorithms and data structures;
- don't reimplement this functionality yourself;

### 6.6 use decimal when precising is paramount

- python has built-in types and classes in modules that can represent practically every type of numerical value;
- the decimal class is ideal for situations that require high precision and exact rounding behavior, such as computations of monetary values;

### 6.7 know where to find community-built modules

## 7. collaboration

### 7.1 write docstring for every function, class and module

- write documentation for every module, class and function using docstrings. keep them up to date as your code changes;
- for modules, introduce the contents of the module and any important classes or functions all users should know about;
- for classes, document behavior, important attributes and subclass behavior in the docstring following the class statement;
- for functions and methods, document every argument, returned value, raised exception and other behaviors in the docstring following the def statement;

### 7.2 use packages to organize modules and provide stable apis

- packages in python are modules that contain other modules, packages allow you to organize your code into separate, non-conflicting namespaces with unique absolute module names;
- simple packages are defined by adding an `__init__.py` file to a directory that contains other source files. these files become the child modules of the directory's package, package directories may also contain other packages;
- you can provide an explicit api for a module by listing its publicly visible names in its `__all__` special attribute;
- you can hide a package's internal implementation by only importing public names in the package's `__init__.py` file or by naming internal-only members with a leading underscore;
- when collaborating within a single team or on a single codebase, using `__call__` for explicit apis is probably unnecessary;

### 7.3 define a root exception to insulate callers from apis

- define root exceptions for your modules allows api consumers to insulate themselves from your api;
- catching root exception can help your modules allows api consumers to insulate themselves from your api;
- catching the python exception base class can help you find bugs in api implementation;
- intermediate root exceptions let you add more specific types of exceptions in the future without breaking your api consumers;

### 7.4 know how to break circular dependecies

{% highlight python%}

# dialog.py
import app

class Dialog():
    def __init__(self):
        pass

save_dialog = Dialog(app.prefs.get("hello"))

def show():
    pass

# app.py
import dialog

class Prefs():
    def get(self, name):
        pass

prefs = Prefs()
dialog.show()

{% endhighlight %}

then if you use app.py in your project, you'll absolutely get an error like bellow:

{% highlight python %}

In [1]: import app
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-1-f8537898a049> in <module>()
----> 1 import app

/Users/chenshan/Desktop/app.py in <module>()
----> 1 import dialog
      2
      3 # import ipdb; ipdb.set_trace()
      4
      5 class Prefs():

/Users/chenshan/Desktop/dialog.py in <module>()
      8         pass
      9
---> 10 save_dialog = Dialog(app.prefs.get("hello"))
     11
     12 def show():

AttributeError: 'module' object has no attribute 'prefs'
{% endhighlight %}

the problem with a circular dependency is that the attributes of a module aren't defined until the code for those attributes has executed(after step 5), but the module can be loaded with the import statement immediately after it's inserted into sys.modules(after step 4)

in the example above, 

1. the app.py import dialog before doing anything
2. then, dialog.py import app firstly, currently the `imported app is just an empty module`
3. then, in dailog.py, the `save_dialog = Dialog(app.prefs.get("hello"))`, at that time, we're sure that there are really a module named `app` exists in current runtime, but it's an empty module, so will raise an attribute error like this.


- python import machinery:
    + searches for your module in locations from sys.path
    + loads the code from the module and ensures that it compiles
    + creates a corresponding empty module object
    + inserts the module into sys.modules
    + runs the code in the module object to define its contents

- [sever ways to break circular imports](http://localhost:4000/python-cycle-import/)
    + reorder imports
    + import first, config second, run last
    + dynamic import
    + re-strucuture or re-factory your code


### 7.5 use virtual env for isonated and reproducible dependences

## 8. Production

### 8.1 consider module-scoped code to configure deployment env

### 8.2 use repr string for debugging output

### 8.3 test everything with unittest

### 8.4 consider interactive debugging with pdb

### 8.5 profile before optimizing

### 8.6 use tracemalloc to understand memory usage and leaks 



