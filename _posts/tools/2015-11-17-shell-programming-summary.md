---
category: tools
published: false
layout: post
title: shell 编程总结
description: 再不总结一下就真的忘了。
---


##
## 1. 基本概念

### 1.1 什么是 shell

业界所说的shell通常都是指shell脚本，但要知道，shell和shell script是两个不同的概念:

- Shell 是一个用C语言编写的程序，它是用户使用Linux的桥梁, 这个应用程序提供了一个界面，用户通过这个界面访问操作系统内核的服务。
- Shell 也是一种命令语言和一种程序设计语言，Shell 脚本（shell script），是一种用shell编写的脚本程序。

### 1.2 Shell 环境

Shell 编程跟java、php编程一样，只要有一个能编写代码的文本编辑器和一个能解释执行的脚本解释器就可以了。Linux的Shell种类众多，常见的有：  

- Bourne Shell（/usr/bin/sh或/bin/sh）  
- Bourne Again Shell（/bin/bash）  
- C Shell（/usr/bin/csh）  
- K Shell（/usr/bin/ksh）  
- Shell for Root（/sbin/sh）  


大多数情况下提到 shell 都是指 Bash，也就是 Bourne Again Shell，由于易用和免费，Bash在日常工作中被广泛使用。同时，
Bash也是大多数Linux系统默认的Shell。
在一般情况下，人们并不区分 Bourne Shell 和 Bourne Again Shell，所以，像 `#!/bin/sh` ，它同样也可以改为 `#!/bin/bash`。
`#!` 告诉系统其后路径所指定的程序即是解释此脚本文件的Shell程序。

### 1.3 shell 脚本的执行

- 作为可执行程序

```
chmod +x ./test.sh  #使脚本具有执行权限
./test.sh  #执行脚本
```

注意，一定要写成`./test.sh`，而不是`test.sh`，运行其它二进制的程序也一样，直接写`test.sh`，linux系统会去PATH里寻找有没有叫`test.sh`的，
而只有`/bin, /sbin, /usr/bin，/usr/sbin`等在PATH里，你的当前目录通常不在PATH里，所以写成`test.sh`是会找不到命令的，
要用`./test.sh`告诉系统说，就在当前目录找。

- 作为 [shell] 解释器参数 : 直接运行解释器，其参数就是shell脚本的文件名

```
/bin/sh test.sh
/bin/php test.php
```

## 2. shell 变量

定义变量时，变量名不加美元符号:

```
your_name="runoob.com"
```

注意，变量名和等号之间不能有空格，同时，变量名的命名须遵循如下规则：

- 首个字符必须为字母（a-z，A-Z）。
- 中间不能有空格，可以使用下划线。
- 不能使用标点符号。
- 不能使用bash里的关键字（可用help命令查看保留关键字）。

除了显式地直接赋值，还可以用语句给变量赋值，如：

```
for file in `ls /etc`
```

使用一个定义过的变量，只要在变量名前面加美元符号即可，如：

```
your_name="qinjx"
echo $your_name
echo ${your_name}
```

变量名外面的花括号是可选的，加不加都行，加花括号是为了帮助解释器识别变量的边界，比如下面这种情况：

```
for skill in Ada Coffe Action Java do
    echo "I am good at ${skill}Script"
done
```

如果不给skill变量加花括号，写成 `echo "I am good at $skillScript"`，解释器就会把$skillScript当成一个变量（其值为空），
代码执行结果就不是我们期望的样子了。推荐给所有变量加上花括号，这是个好的编程习惯。
已定义的变量，可以被重新定义，如：

```
your_name="tom"
echo $your_name
your_name="alibaba"
echo $your_name
```

### 2.1 字符串

字符串可以用单引号，也可以用双引号，也可以不用引号。

- 单引号
    - 单引号里的任何字符都会原样输出，单引号字符串中的变量是无效的；
    - 单引号字串中不能出现单引号（对单引号使用转义符后也不行）。

```
str='this is a string'
```

- 双引号
    - 双引号里可以有变量
    - 双引号里可以出现转义字符

```
your_name='qinjx'
str="Hello, I know your are \"$your_name\"! \n"
```

###










## 参考文档

- [Shell 教程](http://www.runoob.com/linux/linux-shell.html)
