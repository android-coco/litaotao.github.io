---
layout: post
published: false
title: 深度学习第一弹——MNIST for the Newbies
description: 维数一上去了，感觉脑壳就不够用了呀
---  


## 写在前面

最近抽时间看一些 AI 方面的东西，说实话，我一开始对这方面其实不是很重视的，毕竟现在发展还是处于很初级的阶段。但因为本身职业是跟金融有关的，最近看了不少产业相关的资料，也经常研究国家在各个产业链上的政策布局，以及经常看到不少国内外企业在 AI 方面的布局和成绩，觉得这个方向还是可圈可点的。所以还是准备花些时间掌握一些这方面的底层原理，做到知其然知其所以然。

不过其实我内心还是挺害怕的，现在科技这么发达，没准儿到我 ～60 来岁的时候，真会出现 《I, Robot》电影中的那些场景。《I, Robot》是 2004 年我最喜欢的演员 威尔斯密斯 主演的一部讲机器人觉醒的科幻片，如今过去13年，想想这些导演的思维其实还是很具有前瞻性的。


![robot_1.jpg](../images/robot_1.jpg)


## 1. AI, 深度学习，神经网络，机器学习

现在整个行业上其实还是略显浮躁的，搞过线性回归的人说自己懂机器学习，搞过机器学习的说自己研究神经网络，搞过神经网络的说自己做深度学习，搞深度学习的直接说自己是 AI 专家了。

不过话也说来，其实 `AI, 深度学习，神经网络，机器学习` 这四个方面目前也没有非常明晰的分类标准，或者说，也许在不久的某一天，都不存在这样的分类了，也许到时候直接说成 `AI 的不同等级` 吧。

所以在表述这个问题上，我更倾向于交流做过的模型，研究过的模型。


## 2. 所以 MNIST 是个啥

在很多书，在线培训网站上，基本上涉及到神经网络，深度学习，AI 的内容，都是以 MNIST 例子来开讲的，同时很多讲这些主题的 blog，也几乎没有哪篇没有谈到 MNIST。不过话说，我估计应该没多少人知道 MNIST 是啥的缩写吧，这也是我很强调知其然知其所以然的原因，对新知识，新事物的学习过程，不应该是被饲养般的全吞下去，应该细细咀嚼，慢慢品尝其中的韵味。

所以既然提到 AI，大家都先以 MNIST 作为入门例子，就连大 google 开放的 tensorflow 也是以 MNIST 作为开篇例子的，那 MNIST 究竟是个啥呢？

MNIST 是 Mixed National Institute of Standards and Technology database 的简称，从英文原意上还挺难知道到底是干嘛的，不过从官方网站上最终还是找到了它的具体含义 [http://yann.lecun.com/exdb/mnist/](http://yann.lecun.com/exdb/mnist/)，MNIST 是一个数据库，这个数据库中存储了各个国家地区，不同标准的手写数字，并且是存储的内容都是结果标准化处理了的，专门用于关于手写体识别方面的技术应用。


## 3. MNIST 数据结构啥样子呢

介绍 MNIST 的原理之前，我们先来看看它的数据结构是个啥样吧。这里我们直接复用 tensorflow 官方的代码，链接在这儿：[MNIST For ML Beginners](https://www.tensorflow.org/get_started/mnist/beginners)。或者也可以直接看我的 github 上的代码：[https://github.com/litaotao/tensorflow_guide/blob/master/Official%20Document%20-%20Section%201%20:%20get%20started/MNIST%20For%20ML%20Beginners.ipynb](https://github.com/litaotao/tensorflow_guide/blob/master/Official%20Document%20-%20Section%201%20:%20get%20started/MNIST%20For%20ML%20Beginners.ipynb)

数据结构可以直接看下面的截图，我们分两部分来说：

- `mnist.train.image`: 是一个 ndarray，里面每一个元素是用来训练的图片数据
- `mnist.train.image[index]`: 是一个大小为 (784, ) 的 ndarray，里面每一个元素代表这个图片【标准化为 28*28 大小的正方形】在每个像素框中的像素值【或者是灰度值】
- `mnist.train.labels`: 是一个 ndarray，里面的每一个元素指 mnist.train.image 中根据下标对应的图片真实代表值
- `mnist.train.labels[index]`: 是一个大小为 (10, ) 的 ndarray，里面每一个元素只有 0，1 两种取值，代表了 mnist.train.image[index] 这个图片对应的真实值 

![robot_2_mnist.jpg](../images/robot_2_mnist.jpg)

举个例子，如上图所示：

我们看下 `mnist.train.images[0]` 的具体内容，其代表一张标准化为 (28, 28) 的手写数字图片在每一个像素上的值，然后 `mnist.train.labels[0]`的值为 `[ 0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.]`，其中第 1 个元素【下标为 1，序号从 0 开始哦】为 1，其他皆为 0，代表 `mnist.train.images[0]` 这张图片代表的真实值是 1。如果 `mnist.train.labels[0]` 的值为 `[ 0.,  0.,  0.,  0.,  0.,  5.,  0.,  0.,  0.,  0.]`，其中第 5 个元素【下标为 5，序号从 0 开始哦】为 1，其他皆为 0，则说明 `mnist.train.images[0]` 这张图片代表的真实值是 1。

当然为了验证，可以把 `mnist.train.images[0]` 这张图画出来看看：

![robot_3_mnist_pixel.jpg](../images/robot_3_mnist_pixel.jpg)

看到这里，再理解下面这两张图应该就比较轻松了吧：

![robot_3_mnist-train-xs.png](../images/robot_3_mnist-train-xs.png)
![robot_4_mnist-train-ys.png](../images/robot_4_mnist-train-ys.png)


## 4. 那么 softmax 又是个什么鬼

关于 softmax 其实我一开始也挺纳闷的，特别是看到一堆公式后，不过现在回顾来看，其实初学时也不必过于深究。现在可以先知道它和一般的回归有啥区别，以及它存在的意义及用途，之后再慢慢琢磨那些公式也可。因为有些东西，只有用起来才能理解其中的含义。

我们常见的回归一般都是这种形式： `y = A * X + b`，即给定一个 x 序列，输出一个特定的值。而 softmax 是指给定一个 x 序列，输出该序列符合某个结果的概率或者置信度。比如说，现在我们 x 是一个 28 * 28 = 784 长的一个 list，代表一张手写数字的像素序列，经过 softmax 回归后，可以得到这个像素序列分别属于 0 ～ 9 中，每个数字的概率。


## 5. 所以，是时候揭开这个公式的神秘面纱了


## 文中的 latex 公式

{% highlight latex %}
## 权重矩阵

\begin{bmatrix}

w_{11} & w_{12} & w_{13} & ... & w_{1,10}
\\w_{21} & w_{22} & w_{23} & ... & w_{2,10}
\\.
\\.
\\.
\\w_{784,1} & w_{784,2} & w_{784,3} & ... & w_{784,10}
\end{bmatrix}


## 样本图片矩阵
\begin{bmatrix}

x_{11} & x_{12} & x_{13} & ... & x_{1,784}
\\x_{21} & x_{22} & x_{23} & ... & x_{2,784}
\\.
\\.
\\.
\\x_{n,1} & x_{n,2} & x_{n,3} & ... & x_{n,784}
\end{bmatrix}

{% endhighlight %}


## 附注

- [What's an MNIST](https://www.youtube.com/watch?v=iQdWX1327XQ)
- [http://yann.lecun.com/exdb/mnist/](http://yann.lecun.com/exdb/mnist/)
- [MNIST For ML Beginners](https://www.tensorflow.org/get_started/mnist/beginners)
- [online latex equation editor](http://www.hostmath.com/)
- []()