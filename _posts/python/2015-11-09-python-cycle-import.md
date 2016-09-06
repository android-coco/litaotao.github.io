---
category: python
published: true
layout: post
title: python 循环引用
description: 循环引用的原因及一些避免方法。
---


## 1. import module 流程

首先，明确一下 `import module_name` 和 `from module_name import module_element` 是两条可执行的语句。
其次，`sys.modules` 里记录了当前 run time 下所有已经导出的 module。

- 如果 module_name 不在 sys.modules 中，那 import module_name 将会执行:
    + 1. `sys.modules[ module_name ] = [empty pyc file]`
    + 2. execute module_name to generate a module_name.pyc file
    + 3. `sys.modules[ module_name ] = module_name.pyc file path`
- 如果 module_name 已经在 sys.moudles 中，那会去 load 对应的 pyc file，但关键就在这里的 pyc 文件，有两种情况:
    + 上面第一步生成的 pyc 文件，大多数循环引用导致 AttributeError 错误的原因；
    + 上面第三部生成的 pyc 文件，正常情况，不会出异常。


## 2. 如何避免循环引用

- 延迟导入(lazy import)
- 将 `from xxx import yyy` 改成 `import xxx;xxx.yyy` 来访问的形式，这种办法并不能解决所有场景下的问题
- 合理组织代码



## 参考文档

- [Circular (or cyclic) imports in Python](http://stackoverflow.com/questions/744373/circular-or-cyclic-imports-in-python)
- [解决循环import的问题](http://blog.csdn.net/handsomekang/article/details/19010407)
