---
category: books
published: false
layout: post
title: book-4. Web 高性能开发参考资料
description: 个人搜集的一些关于 Web高性能开发的书籍和文章。
---


## 
## 0. 写在前面

　　工作一年多了，发现自己还是没什么长进。学技术这件事儿，还是得靠自己啊，所以我准备以专题的形式来提升自己的能力。这篇我总结了一些搜集的比较好的讲web高性能开发的文章和书籍，都是我自己看过的。以后再也不怕别人问到高性能web的经验和知识了，用老话说，就算没吃过猪肉也应该见过猪跑吧，咱就算没经历过高性能web开发实践，也至少了解一些这方面的知识吧。哈哈。

## 1. 模式相关  

- [设计模式概览图](http://colobu.com/2014/09/05/design-pattern-cheatsheet/)    
　　以图形的形式简单阐述了各种模式的概念，图画得不错，表述也清晰，可以有空翻开看看；
![design_pattern.png](../images/design_pattern.png)

- [软件架构模式](http://colobu.com/2015/04/08/software-architecture-patterns/)   
　　是作者对这本书的[Software Architecture Patterns](http://www.oreilly.com/programming/free/files/software-architecture-patterns.pdf) 笔记和总结，写得很详细，可以时常参考，提升架构方面的基础和概念，同时，有时间也推荐读读原书，原书PDF链接在后面。   
　　这里面提的架构有：分层架构，事件驱动架构，微内核架构，微服务架构，基于空间的架构。

- [微服务架构快速指南](http://colobu.com/2015/04/10/microservice-architecture-a-quick-guide/)   
　　不常听说为服务架构，简单的理解，就是介于monolithic和SOA模式之间的一个架构模式，比monolithic灵活，轻便，比SOA有更强的组织性。不必过于在乎三者之间的差别，根据实际情况选择合适自己项目的架构模式。

- [微服务架构的设计模式](http://colobu.com/2015/04/24/microservice-design-patterns/)   
　　是**微服务架构快速指南**的细节篇，里面介绍了一些常用的微服务架构的设计模式，在设计项目架构的时候，如果没有什么思路，这篇文章是很好的参考资料。简单的说，里面提到了常用的微服务设计模式：聚合器，代理，链式服务，分支，数据共享，异步消息。

## 2. 高性能网站相关  

- [如何构建高扩展性网站](http://colobu.com/2015/04/20/how-to-build-a-scalable-website/)   
　　是一本小册子[《高扩展性网站的50条原则》](http://book.douban.com/subject/10756899/)的读书笔记。这本书不错，值得一看，在设计、改进项目架构时都可以拿来翻翻，不错的小册子。

- [最佳免费的网站性能测试工具](http://colobu.com/2014/09/26/best-free-website-speed-testing-tools/)   
　　这篇博文是我认为最有实际意义的一篇博文之一了，里面提到了12个免费的网站性能测试工具，比如大名鼎鼎的google pagespeed insights。我的建议是，在进行任何优化前，都先简单地用这些工具在线测试一下。不要盲目地进行后台的优化，更不要盲目的去设计一些高端的算法来做所谓的加速。比如说，一个请求后台返回的时间控制在100ms之内，但发起这个请求的js脚本被写在一个很大的js文件里面，导致下载这个js文件需要数百毫秒，那此时应该怎么优化呢？别跟我说你会让你的后台工程师去找一什么高大上的算法来解决这个问题。   




## 3. 参考书籍
- [Software Architecture Patterns](http://www.oreilly.com/programming/free/files/software-architecture-patterns.pdf)
- [高扩展性网站的50条原则](http://book.douban.com/subject/10756899/)




