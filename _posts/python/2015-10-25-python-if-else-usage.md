---
category: python
published: true
layout: post
title: python else 用法总结    
description: 头一次看到python里的else有这么多用法，虽然有些奇葩，还是记录一下。
--- 


## 1. 常规的 if else 用法

{% highlight python %}

x = True

if x:
    print 'x is true'
else:
    print 'x is not true'

{% endhighlight %}



## 2. if else 快捷用法 

这里的 `if else` 可以作为三元操作符使用。

{% highlight python %}

mark = 40
is_pass = True if mark >= 50 else False
print "Pass? " + str(is_pass)

{% endhighlight %}


## 3. 与 `for` 关键字一起用

在满足以下情况的时候，`else` 下的代码块会被执行：

- for 循环里的语句执行完成
- for 循环里的语句没有被 `break` 语句打断

{% highlight python %}

# 打印 `For loop completed the execution`
for i in range(10):
    print i
else:
    print 'For loop completed the execution'

# 不打印 `For loop completed the execution`
for i in range(10):
    print i
    if i == 5:
        break
else:
    print 'For loop completed the execution'

{% endhighlight %}


## 4. 与 `while` 关键字一起用

和上面类似，在满足以下情况的时候，`else` 下的代码块会被执行：

- while 循环里的语句执行完成
- while 循环里的语句没有被 `break` 语句打断

{% highlight python %}

# 打印 `While loop execution completed`
a = 0
loop = 0
while a <= 10:
    print a
    loop += 1
    a += 1
else:
    print "While loop execution completed"

# 不打印 `While loop execution completed`
a = 50
loop = 0
while a > 10:
    print a
    if loop == 5:
        break
    a += 1
    loop += 1
else:
    print "While loop execution completed"

{% endhighlight %}


## 5. 与 `try except` 一起用

和 `try except` 一起使用时，如果不抛出异常，`else`里的语句就能被执行。

{% highlight python %}

file_name = "result.txt"
try:
    f = open(file_name, 'r')
except IOError:
    print 'cannot open', file_name
else:
    # Executes only if file opened properly
    print file_name, 'has', len(f.readlines()), 'lines'
    f.close()

{% endhighlight %}



## 参考文档  

- [5 different methods to use an else block in python](http://www.idiotinside.com/2015/10/18/5-methods-to-use-else-block-in-python)






