---
category: python
published: false
layout: post
title: Python 装饰器实例   
description: 装饰器看过很多遍了，但每次被人问到都感觉还是不熟悉，一种既陌生又熟悉的感觉，我想多看看例子应该会对我有所帮助~
---    

## 
## 1. 打印执行函数的名字

这是我们项目里用到的真实例子，很简单，就是在函数执行前打印函数的名字，函数执行后再次打印函数的名字。这个脚本是用来对数据库做修改的，因为随着产品版本的升级，时不时需要对数据库的一些字段，甚至是scheme进行修改。我们暂且把数据库兼容的脚本叫做 compatible.py ，每次执行compatible.py都打印出日志，日志的内容就是该次执行compatible.py里的哪些函数。


```
'''
# A simple wrapper, print func name when been executed.
'''

from functools import wraps
def print_func_name(func):
    @wraps(func)
    def _wrapper(*args, **kwargs):
        print 'start execute {} ...'.format(func.__name__)
        result = func(*args, **kwargs)
        print 'end execute {} ...\n----------'.format(func.__name__)
        return result
    return _wrapper

@print_func_name
def gen_node(test_user_path):
    '''
    genernate node.
    '''
    pass
```


## 2. 缓存   

这是 Glow CTO 在一次PyCon上的演讲中的例子，做函数计算结果的缓存。该演讲的地址和PDF在这里可以找到：[为何Python适合初创公司](http://boolan.com/lecture/1000001046)    

```
def memorized(func):
    def _wrapper(*args, **kwargs):
        if not hasattr(func, '__cached_result'):
            func.__cached_result = {}
        cache_key = hash((tuple(args), tuple(kwargs.iteritems())))
        if cache_key not in func.__cached_result:
            func.__cached_result[cache_key] = func(*args, **kwargs)
        return func.__cache_result[cache_key]
    return _wrapper

@memorized
def fib(n):
    if n <= 0: return 0
    if 1 == n: return 1
    return fib(n-1) + fib(n-2)
```  

## 3. 获取数据库连接，或者redis 连接等，常用

这个是在另一片文章里提到的一个bug分析，连接在此：[伴我一路走来的那些bug们，你们好](../bugs-in-my-life/)

```
class Test(object):
    def assign_user_to_exp(self, user_id, cell_id):
            self.g_pool.spawn(
                self.async_assign_user_to_exp,
                user_id,
                cell_id,
            )
            return

    @get_dbc
    def async_assign_user_to_exp(self, dbc, user_id, cell_id):
        return dbc.execute(''' there is a sql sentence that refering user_id and cell_id, just leave details here ''')
```

## 参考资料

- [Python修饰器的函数式编程](http://coolshell.cn/articles/11265.html)  
- [python黑魔法---装饰器（decorator）](http://www.jianshu.com/p/7e5466661744)   
- [PythonDecoratorLibrary](https://wiki.python.org/moin/PythonDecoratorLibrary)







