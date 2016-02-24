---
category: tools
published: true
layout: post
title: 一行代码，打造在线编辑器
description: 一行代码，打造一个在线编辑器，方便好用
---


## 1. 事情是这样的


事情是这样的，有一天要开会，我准备把会议的 outline 写到个 ***暂时*** 的 notebook 里，在会议的时候参考。

然后，问题就来了：

- 我不想打开 pages，excel，office 什么的；
- 我也不想打开 xcode 的 text editor，因为打开的窗口已经很多了，切换起来麻烦；
- 我也不想用正在写代码的 sublime 新建个文件，因为不想污染我写代码的环境，哈哈；

然后，想法就来了，要是能用浏览器来做编辑器就好了，然后突然想到很久之前看到的一篇文章，说如何用一行代码把 chrome 浏览器变成在线编辑器。哈哈，google 了下，果然找到解决方法了，果然是技术造福人类啊。

[# 极氪 # 仅一行代码，打造一个在线编辑器](http://36kr.com/p/201096.html)

可是还不够，这样每次都要拷贝，粘贴到浏览器里，多麻烦啊。要是能输入一个链接，直接就有这样一个在线编辑器，那多爽啊。哈哈。

想想它的原理，其实就是一个 html 文件嘛，更细致一点，就是一个很简单的，定制化的 textarea [我不确定是不是这个组件，但是这都不重要了，哈哈]，只要把这个 html 放到一个固定的，人人都能访问的地方不就行了？


## 2. 感谢 github

于是乎，解决方案就来了。首先得感谢 github 啊，让多少人零首付零还款就搭建了个博客，我也一样。既然博客都有了，那把上面的那个 html 文件放到博客上不就行了？

于是乎，我把上面的 html 保存到自己 github 博客的 `files/` 目录下面，然后直接访问 [litaotao.github.io/files/editor.html](http://litaotao.github.io/files/editor.html) 就可以了。哈哈，爽爽的赶脚。

以后就方便多了，再要写什么临时文本的时候，直接打开浏览器，输入 [litaotao.github.io/files/editor.html](http://litaotao.github.io/files/editor.html) 就可以了。怎么有一种逼格满满的赶脚，哈哈。

当然了，你也可以自己搞一个，下载这个 [html](https://github.com/litaotao/litaotao.github.io/raw/master/files/editor.html) 文件，然后放到你的博客下面就可以了。
