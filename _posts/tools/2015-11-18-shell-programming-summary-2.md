---
category: tools
published: true
layout: post
title: shell 编程总结二，test 命令，流程控制
description: 再不总结一下就真的忘了。
---



## 1. test 命令

Shell中的 test 命令用于检查某个条件是否成立，它可以进行数值、字符和文件三个方面的测试。

### 1.1 数值测试

- `-eq : equal`: 等于
- `-ne : non-equal`: 不等于
- `-gt : great than`: 大于
- `-ge : great or equal`: 大于或等于
- `-lt : lower than`: 小于
- `-le : lower or equal`: 小于或等于

{% highlight shell %}
num1=100
num2=100
if test $[num1] -eq $[num2]
then
    echo 'The two numbers are equal!'
else
    echo 'The two numbers are not equal!'
fi
{% endhighlight %}

### 1.2 字符串测试

- `=`: 等于
- `!=`: 不等于
- `-z : zero`: 字符串长度为零，则为真
- `-n : non-zero`: 字符串长度不为零，则为真
- `${var-DEFAULT}`:	如果var没有被声明, 那么就以$DEFAULT作为其值 *
- `${var:-DEFAULT}`: 如果var没有被声明, 或者其值为空, 那么就以$DEFAULT作为其值 * 	 
- `${var=DEFAULT}`:	如果var没有被声明, 那么就以$DEFAULT作为其值 *
- `${var:=DEFAULT}`: 如果var没有被声明, 或者其值为空, 那么就以$DEFAULT作为其值 *
- `${var+OTHER}`:	如果var声明了, 那么其值就是$OTHER, 否则就为null字符串
- `${var:+OTHER}`:	如果var被设置了, 那么其值就是$OTHER, 否则就为null字符串	 
- `${var?ERR_MSG}`:	如果var没被声明, 那么就打印$ERR_MSG *
- `${var:?ERR_MSG}`:	如果var没被设置, 那么就打印$ERR_MSG *

{% highlight shell %}
num1=100
num2=100
if test num1=num2
then
    echo 'The two strings are equal!'
else
    echo 'The two strings are not equal!'
fi
{% endhighlight %}

### 1.3 文件测试

- `-e  : exist`: 如果文件存在则为真
- `-r  : readable`: 如果文件存在且可读则为真
- `-w  : writable`: 如果文件存在且可写则为真
- `-x  : execute`: 如果文件存在且可执行则为真
- `-s  : `: 如果文件存在且至少有一个字符则为真
- `-d  : directory`: 如果文件存在且为目录则为真
- `-f  : file`: 如果文件存在且为普通文件则为真
- `-c  : `: 如果文件存在且为字符型特殊文件则为真
- `-b  : block`: 如果文件存在且为块特殊文件则为真

{% highlight shell %}
cd /bin
if test -e ./bash
then
    echo 'The file already exists!'
else
    echo 'The file does not exists!'
fi
{% endhighlight %}

另外，Shell还提供了与( -a )、或( -o )、非( ! )三个逻辑操作符用于将测试条件连接起来，其优先级为："!"最高，"-a"次之，"-o"最低。例如：

{% highlight shell %}
cd /bin
if test -e ./notFile -o ./bash
then
    echo 'One file exists at least!'
else
    echo 'Both dose not exists!'
fi
{% endhighlight %}

## 2. 流程控制

### 2.1 if elif else fi 控制符

完整的格式如下，其中，`elif`, `else` 可根据实际情况决定是否需要。

{% highlight shell %}
if condition1
then
    command1
elif condition2
    command2
else
    commandN
fi
{% endhighlight %}

实例：

{% highlight shell %}
num1=$[2*3]
num2=$[1+5]
if test $[num1] -eq $[num2]
then
    echo '两个数字相等!'
else
    echo '两个数字不相等!'
fi
{% endhighlight %}

### 2.2 for 循环

{% highlight shell %}
for var in item1 item2 ... itemN
do
    command1
    command2
    ...
    commandN
done
{% endhighlight %}

### 2.3 while 语句

{% highlight shell %}
while condition
do
    command
done
{% endhighlight %}

示例：

{% highlight shell %}
#!/bin/sh
int=1
while(( $int<=5 ))
do
        echo $int
        let "int++"
done
{% endhighlight %}

while循环可用于读取键盘信息。下面的例子中，输入信息被设置为变量FILM，按<Ctrl-D>结束循环。

{% highlight shell %}
echo '按下 <CTRL-D> 退出'
echo -n '输入你最喜欢的电影名: '
while read FILM
do
    echo "是的！$FILM 是一部好电影"
done
{% endhighlight %}

无限循环语法格式：

{% highlight shell %}
while :
do
    command
done

# 或者

while true
do
    command
done

# 或者
for (( ; ; ))
{% endhighlight %}

### 2.4 until 循环

until循环执行一系列命令直至条件为真时停止。
until循环与while循环在处理方式上刚好相反。
一般while循环优于until循环，但在某些时候—也只是极少数情况下，until循环更加有用。
until 语法格式:

{% highlight shell %}
until condition
do
    command
done
{% endhighlight %}

### 2.5 case 语句

{% highlight shell %}
case 值 in
模式1)
    command1
    command2
    ...
    commandN
    ;;
模式2）
    command1
    command2
    ...
    commandN
    ;;
esac
{% endhighlight %}

示例：

{% highlight shell %}
echo '输入 1 到 4 之间的数字:'
echo '你输入的数字为:'
read aNum
case $aNum in
    1)  echo '你选择了 1'
    ;;
    2)  echo '你选择了 2'
    ;;
    3)  echo '你选择了 3'
    ;;
    4)  echo '你选择了 4'
    ;;
    *)  echo '你没有输入 1 到 4 之间的数字'
    ;;
esac
{% endhighlight %}

### 2.6 break 和 continue 语句

break命令允许跳出所有循环（终止执行后面的所有循环）。
下面的例子中，脚本进入死循环直至用户输入数字大于5。要跳出这个循环，返回到shell提示符下，需要使用break命令。

{% highlight shell %}
#!/bin/bash
while :
do
    echo -n "输入 1 到 5 之间的数字:"
    read aNum
    case $aNum in
        1|2|3|4|5) echo "你输入的数字为 $aNum!"
        ;;
        *) echo "你输入的数字不是 1 到 5 之间的! 游戏结束"
            break
        ;;
    esac
done
{% endhighlight %}

continue命令与break命令类似，只有一点差别，它不会跳出所有循环，仅仅跳出当前循环。

{% highlight shell %}
#!/bin/bash
while :
do
    echo -n "输入 1 到 5 之间的数字: "
    read aNum
    case $aNum in
        1|2|3|4|5) echo "你输入的数字为 $aNum!"
        ;;
        *) echo "你输入的数字不是 1 到 5 之间的!"
            continue
            echo "游戏结束"
        ;;
    esac
done

{% endhighlight %}


## 参考文档

- [Shell 教程](http://www.runoob.com/linux/linux-shell.html)
- [linux shell 字符串操作（长度，查找，替换）详解](http://www.cnblogs.com/chengmo/archive/2010/10/02/1841355.html)
- [Linux 之 shell 比较运算符](http://blog.csdn.net/ithomer/article/details/6836382)
