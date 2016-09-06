---
category: web
published: false
layout: post
title: auto-complete / auto-suggest 之一，概念原理
description: 记录我在实现 auto-complete / auto-suggest 过程中的点点滴滴。
---  


##
## 写在前面
最近在做一个搜索框的自动补全功能，发现这方面还真是有不小的细节需要处理。网上的资料很少，基本就是一些简单的 demo，或者
简单的说 `多发几个 ajax 请求` 类似的话。在我看来，这种说法和 `问一个乞丐需不需要吃饭`，毫无用处。于是自己在做这个功能
的过程中搜集了一些个人觉得不错的资料，也看看能不能把实现的代码抽出来，做成一套简单的框架放到 github 上。


## 1. auto-complete 和 auto-suggest 的定义，区别

其实我一开始也不知道 `auto-complete` 和 `auto-suggest` 之间有什么区别，甚至在之前的一段时间内我还以为这两个名词
其实是同一个意思。所以有时候在和同事，朋友交流的时候，一会儿说 `auto-suggest`，一会儿说 `auto-complete`。后来 google
的时候无意间发现了一篇好文 : [Designing Search: As-You-Type suggestions](http://uxmag.com/articles/designing-search-as-you-type-suggestions)。

这篇文章讲得很好，除了讲 auto-complete 和 auto-suggestion，还讲到了 instant search，虽然不是从技术角度来讲，但对于
概念上的理解很有帮助。

按照文章里说的：

```
Use auto-complete to:

  Facilitate accurate and efficient data entry
  Select from a finite list of names or symbols

Use auto-suggest to:

  Facilitate novel query reformulations
  Select from an open-ended list of terms or phrases
  Encourage exploratory search (with a degree of complexity and mental effort that is appropriate to the task). Where appropriate, complement search suggestions with recent searches

Use instant results to:

  Promote specific items or products
```

Instant search 很好理解，用过的人都知道。
Auto-complete呢，按照上面的说法，其实也没多大差别。简单的说：

- auto-complete:
  + 事先有一个定义好的列表，返回列表里以用户输入的关键字为前缀的关键词；
  + 即，auto-complete 可以用这句代码来表示：`[keyword for keyword in keywords_defined_by_us_before if keyword.startswith(user_input_prefix)]`

- auto-suggest:
  + 事先有一个定义好的列表，返回列表里含有用户输入的关键字的关键词；；
  + 即，auto-suggest 可以用这句代码来表示：`[keyword for keyword in keywords_defined_by_us_before if user_input_prefix in keyword]`

下面是有道词典的 auto-complete 和 quora 的 auto-suggest 的截图，这下子就一目了然了。

-----

![auto-complete.jpg](../images/auto-complete.jpg)
------

![auto-suggestion.jpg](../images/auto-suggestion.jpg)


## 2. 应用场景与实现方案

### 2.1  三思而后行

在做这个功能之前，确实听说过大概有哪些解决方案，其中最常见的就是传说中的前缀树，字典树，前缀匹配，倒排索引类似的，后来也看到有人用 redis 来实现的。应该说，
不乏解决方案，但是如何选择就是考验人的时候了。我觉得，在决定如何做之前，需要考虑一下几点因素：

- 你要做的是 auto-suggest 还是 auto-complete
  + auto-complete: 那可以构建前缀树来做；
  + auto-suggest: 因为需要做一些 `string.contains(substring)` 类似的工作，所以简单的前缀树不能解决这类问题。根据数据量大小情况决定。
- 你的预定义的关键词量有多少
  + 数据量很小，几千几万个［ 只是一个概念，我自己并没有做过测试，仅供参考］，那直接用
  `[keyword for keyword in keywords_defined_by_us_before if user_input_prefix in keyword]` 了吧。当然如果蛋疼的话，就去搞搞 elastic search，
  搞搞 cluster 什么的。
  + 数据量一半，几十万个 ［ 只是一个概念，我自己并没有做过测试，仅供参考］，可以看看有没有什么现成的，高效率的倒排索引的库什么的，或者自己实现一个。
  + 数据量很多很多，可以考虑用用 elastic search 自带的 suggester 功能，虽然 es 的文档烂的像卸妆后的明星一样，但是还是值得参考的，本文最后有一些参考文章。
- 你的用户量有多大，预计请求的频率会有多少
  + 这个其实也挺重要的，在server端这边我还没有做过什么测试，所以也不好说。但是这点在设计客户端搜索策略到时候是很值得思考的，详情见后文。

### 2.2 我选择的解决方案

首先明确一下，我们的应用场景是，用户在 APP 的社区里会搜索一些感兴趣的帖子，所以这类关键字并不像有道词典的那样有规则，有模式，所以我们要实现一个 auto-suggest 的功能。
其次，因为我们的预定义的关键词数量是很少的，因为社区主要是针对 18 － 40 岁这部分准备怀孕的，已怀孕和已生小孩儿的女性朋友，所以话题很有针对性，关键词数量在几十万这个级别。
最后，用户量有多大，预计请求的频率会有多少，这点恐怕不能透露，要不然下个月没工资领了，不能开荤了，哈哈。

因为时间紧急，并且我们现在社区里的很多东西都放到 elastic search 里了，所以我也决定就用 es 的 suggester 来做这个 auto-suggest。虽然不是特别有必要用 es 来做，但是
这样做是觉得把社区搜索相关的东西统一放到 es 里应该会比较好。

## 3. 续集：使用 es 实现能在生产环境使用的 suggestion


## 参考文章

- [https://github.com/rodricios/autocomplete](https://github.com/rodricios/autocomplete)
- [designing-search-as-you-type-suggestions](http://uxmag.com/articles/designing-search-as-you-type-suggestions)
- [elastic blog: you complete me](https://www.elastic.co/blog/you-complete-me)
- [使用 Redis 实现自动补全功能](http://segmentfault.com/a/1190000002712454)
- [自动补全（智能提示）原理与实现](http://blog.csdn.net/lgnlgn/article/details/8816218)
- [Multi-field Partial Word Autocomplete in Elasticsearch Using nGrams](http://qbox.io/blog/multi-field-partial-word-autocomplete-in-elasticsearch-using-ngrams)
- [What doest the weight means in completion suggester?](https://discuss.elastic.co/t/what-doest-the-weight-means-in-completion-suggester/33345)
