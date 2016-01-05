---
category: python
published: false
layout: post
title: ［读书笔记］effective Python
description: Python 技巧总结~
---


##
## 1. Pythonic Thinking

### 1.1 know which version of python you're using

- two major python version;
- multiple popular runtimes for python: cpython, jython, ironpython, pypy, etc;
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

```
for index, item in enumerate(list):
    print 'index : {}, item : {}'.format(index, item)
```

- enumerate provides a concise syntax for looping an iterator and getting the index for each item;
- prefer enumerate instead looping over a range and indexing for each item;
- you can specify a number to the enumerate function, specifying the index you want to iterate with;


### 1.11 use zip to process iterators in parallel

- the `zip` can be used to iterate over multiple iterators;
- in python 3, `zip` is a lazy generator, in python 2, `zip` return all the results as a list, but you can use `izip` from `itertools` to make it a generator;
- `zip` truncates it's output silently if you supply it with different length, if you cannot lose any data, use the `zip_longest` from `itertools`;

### 1.12 avoid else blocks after for and while loops

### 1.13 take advantage of each block in try/except/else/finally

```
# to do
```

- the `try/finally` statements let you run cleanup code regardless whether there is exceptions in your `try` block or not;


## 2. functions


### 2.1 prefering exceptions to return none

- functions that return `None` to indicate special meaning are error prone beacause `None` and other values (0, empty string, etc) are evaluated to `False` in the conditional expression;
- Raise exceptions to indicate special situations instead of returning `None`, expect the calling code to handle the exceptions properly;

### 2.2 know how closures interactive with variable scope

```
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
```

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

```
# when the function is defined, default argument values are evaluated just once per module at the loading time.

def log(msg, time=datetime.now()):
    print 'msg: {}, time: {}'.format(msg, time)

def log_version(msg, time=None):
    msg_time = time if time else datetime.now()
    print 'msg: {}, time: {}'.format(msg, msg_time)

```

- use None for default value is especially important when the argument is mutable;
- default argument values are only evaluated once;

### 2.8 enforce clarity with keyword only argument

- keyword argument make the intention of the function more clear;
- prefer to use keyword arguments if possible, especially when there are many boolean flag arguments;
- python 3 supports explicit syntax for keyword only arguments in functions;
- python 2 can emulate keyword only argument by using `**kwargs` and manually throw `TypeError` exception;

## 3. Classes and Inheritance



































#
