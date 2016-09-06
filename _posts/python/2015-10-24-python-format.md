---
category: python
published: true
layout: post
title: Python format 笔记    
description: 
--- 


## 1. 位置参数

字符串的format函数可以接受不限个参数，位置可以不按顺序，可以不用或者用多次，不过2.6不能为空{}，2.7才可以。
值得注意的是，`位置可以不按顺序，可以不用或者用多次`，再结合下面的例子，可以发现，这里的位置参数其实和关键字参数是一样的，只是这里的关键字是位置的下标而已了。   

{% highlight python %}

In [1]: '{0},{1}'.format('kzc',18)  
Out[1]: 'kzc,18'  
In [2]: '{},{}'.format('kzc',18)  
Out[2]: 'kzc,18'  
In [3]: '{1},{0},{1}'.format('kzc',18)  
Out[3]: '18,kzc,18'

# more powerful

In [7]: p=['kzc',18]
In [8]: '{0[0]},{0[1]}'.format(p)
Out[8]: 'kzc,18'

{% endhighlight %}

## 2. 通过关键字参数   

{% highlight python %}

In [5]: '{name},{age}'.format(age=18,name='kzc')  
Out[5]: 'kzc,18'

{% endhighlight %}

## 3. 对象属性

这是很多对象的 `str`, `__str__`, `__repr__` 方法的实现。关于这三个方法的区别，可以简单的理解为下面几点：  

- `str` 是 pyhton 的内置函数，`str(obj)` 实际是调用 `obj.__str__()`；
- `obj.__str__()` 是简化版的 `obj.__repr__()`；
- need more details, check this on [SO](http://stackoverflow.com/questions/1436703/difference-between-str-and-repr-in-python)     


{% highlight python %}

class Person:  
    def __init__(self,name,age):  
        self.name,self.age = name,age  
        def __str__(self):  
            return 'This guy is {self.name},is {self.age} old'.format(self=self)  

{% endhighlight %}

## 4. 格式限定符 - 填充与对齐

不好解释，解释了还是得看例子才明白，直接看例子吧，哈哈。 

{% highlight python %}

# 无需对齐，填充
In [1]: '{}'.format('hello')
Out[1]: 'hello'

In [2]: '{:}'.format('hello')
Out[2]: 'hello'

# 居中对齐，构建 9 个长度的字符串
In [5]: '{:^9}'.format('hello')
Out[5]: '  hello  '

# 右对齐，构建 9 个长度的字符串
In [6]: '{:>9}'.format('hello')
Out[6]: '    hello'

# 左对齐，构建 9 个长度的字符串
In [7]: '{:<9}'.format('hello')
Out[7]: 'hello    '

# 右对齐，构建 9 个长度的字符串，用 0 填充空白位置
In [10]: '{:0>9}'.format('hello')
Out[10]: '0000hello'

# # 左对齐，构建 9 个长度的字符串，用 0 填充空白位置
In [11]: '{:0<9}'.format('hello')
Out[11]: 'hello0000'

# 居中对齐，构建 9 个长度的字符串，用 0 填充空白位置
In [12]: '{:0^9}'.format('hello')
Out[12]: '00hello00'

{% endhighlight %}


## 5. 精度与类型

- f : float类型
- b : 二进制
- d : 十进制 
- o : 八进制
- x : 十六进制
- , : 逗号可以表示数字的千分位

{% highlight python %}

In [44]: '{:.2f}'.format(321.33345)
Out[44]: '321.33'

In [54]: '{:b}'.format(17)
Out[54]: '10001'
In [55]: '{:d}'.format(17)
Out[55]: '17'
In [56]: '{:o}'.format(17)
Out[56]: '21'
In [57]: '{:x}'.format(17)
Out[57]: '11'

In [47]: '{:,}'.format(1234567890)
Out[47]: '1,234,567,890'

{% endhighlight %}

## 6. 完善的格式文档 


![python_str_format.jpg](../images/python_str_format.jpg)


## 7. % VS format

我一直都喜欢用 `format` ，不知道为什么，可能喜欢一种写法也是不需要原因的吧，哈哈。其它的，可以在这里找到一大堆说法。  

- [python-string-formatting-vs-format](http://stackoverflow.com/questions/5082452/python-string-formatting-vs-format)



## 参考文档   

- [飘逸的python - 增强的格式化字符串format函数](http://blog.csdn.net/handsomekang/article/details/9183303)
- [官方文档](https://pyformat.info/)
- [Python格式字符串（译）](http://blog.xiayf.cn/2013/01/26/python-string-format/)
