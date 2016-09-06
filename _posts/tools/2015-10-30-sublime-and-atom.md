---
category: tools
published: false
layout: post
title: sublime 和 atom 对比
description: I still love sublime, but atom is much younger and sexy.
---


##
## 写在前面  

- 首先，这只是我个人的一个对比，也许很多功能在 sublime 里面也能实现，只是我不知道而已。
- 其次，因为用了 sublime 真的已经很久了，所以对比的时候难免会有偏见，没办法。

***I still love sublime, but atom is much younger and sexy.***

![sublime-atom-lady-1.jpg](../images/sublime-atom-lady-1.jpg)

## 1. 配置

## 2. 主题

## 2.1 目录树

我不得不说，atom 的目录树显示比 sublime 的要方便多了，之前一直被 sublime 的目录书困扰。首先是颜色，因为我一直用 Monokai 的主题，
但 sublime 的目录树是白色的啊，白色的啊，这对比度真的太强了。而且 sublime 的目录书感觉对比性不太好，可能是因为 indent 太少了吧。
下面是一个简单的对比图。



## 3. 第三方集成

### 3.1 github

- 如果你打开的文件是在一个 github repo 里的话，在 atom 的右下角会显示该文件的 `git status` 信息，即当前所在分支，当前文件改动情况。

![atom-github.jpg](../images/atom-github.jpg)

- 文件夹和文件的高亮显示，在左侧目录树中会高亮显示此次更改过的文件。在文件被 `commit` 后才会取消高亮，其中高亮有两种：
  - green：新建的文件，就是当前 repo 里还没有被 track 的文件
  - orange：表示文件被更新

![atom-highlight-file.jpg](../images/atom-highlight-file.jpg)

- 保证文本最后一行空行，这个细节做得很贴心啊，当你保存文件的时候，如果：
  + 当前光标所在行是文本最末一行，那 atom 会自动给当前文本新增一行空行
  + 当前文末有大于1行的空白行，那 atom 会删除多余空白行，保证最末只有一行空行
  + 总之，atom 会让你的文件结尾有且只有一行空行

这点很细心啊。如果你的文末有很多空行，首先看起来就不方便，占着茅坑不**啊。其次也是最重要的，就像 [stackoverflow](http://stackoverflow.com/questions/5813311/no-newline-at-end-of-file) 这个问答里所说的

```
Note that it is a good style to always put the newline as a last character if it is allowed by the file format. Furthermore, for example, for C and C++ header files it is required by the language standard.
```

所以，以后还是用 atom 吧，光这点就吸引我了，details make success.


### 3.2 markdown

应该说，sublime 的 markdown 支持还是不错的，可以安装一些插件来实现预览。但是 atom 集成度更高。首先是 atom editor 本身对markdown的语法
支持很好，看起来很舒服。其次是它不用安装其他什么包就可以通过 `control + shift + m` 来实时预览了。

这里不知道为什么不能 render 图片，提了个 [issue](https://github.com/atom/markdown-preview/issues/323).

![atom-markdown.jpg](../images/atom-markdown.jpg)
