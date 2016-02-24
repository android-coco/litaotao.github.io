---
category: erlang
published: true
layout: post
title: 解读 Erlang lists 源码
description: 据说在 Erlang 里，操作lists是最平凡的，那就让我们一起来看看lists是怎么实现的吧~~
---

## 写在前面  
　　lists官方文档在此[http://erlang.org/doc/man/lists.html](http://erlang.org/doc/man/lists.html)，不知因为什么原因，官方文档中函数顺序和lists.erl源码里的顺序完全不一样。我是按照源码里的顺序来写的，目的是为了熟悉一下Erlang的编程风格和巩固基础语法。也不会所有函数都提到，挑下面一些来学习学习。
>
**1.  属性说明**    
**2.  keyfind/3**  
**3.  suffix/2**     
**4.  seq/2, seq/3**  
**5.  sort/1**
**6.  merge/1**  
**7.  concat/1**  
**8.  flatten/1, flatten/2**  
**10. filter/2, map/2, filtermap/2**  
**11. foldl/3, foldr/3**   
**12. keydelete/3**  
**13. keymap/3**


## 1. 属性说明

　　源文件里注明了 `-compile({no_auto_import, [max/2]}).`，这是一个预定义的模块属性【预定义的模块属性有以下四种：`module，import，export，compile，vsn`】。其中`-compile(Options)`是将Options添加到编译器选项表中，Options可以是单个原子，也可以是一个列表。这里的`no_auto_import`是说函数max/2不要自动从erlang模块里导出了，这是为了解决内置函数冲突。没听明白吧，ok，下面详细讲讲这个。至于模块属性，详见《Erlang程序设计》第二版，8.4节；有关compile选项，请移步[http://erlang.org/doc/man/compile.html](http://erlang.org/doc/man/compile.html)。  
　　首先，什么叫自动导出：easy，自动导出就是你不加模块前缀就可以运行的函数。平常使用模块函数不都是模块名:函数名的吗。比如说我们要使用erlang模块里的max函数，一般都是erlang:max这样使用。so，顾名思义，如果max函数在erlang里是自动导出的，那我猜想我们可以直接在console里运行max函数了，而且注意，在console里不加模块名直接运行的max函数一定是定义在erlang这个模块里面的。猜想一下，如果含有其他模块【假定为erl】也定义了一个max函数，并且也自动导出了，那当你直接运行max函数时，erlang虚拟机是该运行erl里的max呢还是erlang里的max呢。  
　　好的，简单测试下，直接看代码得了:  

{% highlight shell %}

root@kali:~/Desktop/erlcode# erl
Erlang/OTP 17 [erts-6.1] [source] [64-bit] [smp:4:4] [async-threads:10] [hipe] [kernel-poll:false]

Eshell V6.1  (abort with ^G)
1> erlang:max(1,2).
2
2> max(1,2).
2
3>

{% endhighlight %}

  
　　现在，这个问题解决了，那我们来看看，为什么在lists模块里要阻止max/2自动导入呢。just think it，就和我上面说的一样，防止自动导出的核心是什么？不就是为了防止函数冲突吗？so，我猜想我们lists.erl模块里也有一个max/2函数，而且这个max/2函数的实现必须是和erlang模块里的实现是不同的。CTRL+F查找，果然不出所料：　　

{% highlight erlang %}

%% max(L) -> returns the maximum element of the list L

-spec max(List) -> Max when
      List :: [T,...],
      Max :: T,
      T :: term().

max([H|T]) -> max(T, H).

max([H|T], Max) when H > Max -> max(T, H);
max([_|T], Max)              -> max(T, Max);
max([],    Max)              -> Max.

{% endhighlight %}

　　好了，到这里关于模块预定义属性就差不多了，以后遇到了再慢慢补上。

## 2. keyfind/3  
 　　lists里的`keyfind/3, keymember/3, keysearch/3, member/2, reverse/2`都是通过内置函数实现的，源码都在erl_bif_types.erl这个文件里面。在keyfind/3的定义中，看到了pos_integer()这样一个变量类型，看来基础还是不行啊，没办法，大家有空都来这里补补基础吧。[7 Types and Function Specifications](http://www.erlang.org/doc/reference_manual/typespec.html)  

## 3. suffix/2  
　　之所以要介绍suffix，是想借suffix来简单介绍一下Erlang里的布尔表达式和所谓的短路布尔表达式。函数定义和实现如下，检查Suffix是否是List的后缀。实现就用了两行，真是精湛啊，突然发现其实很多操作不用循环也能很清楚的表达了。  
　　这里的 andalso 叫做短路布尔表达式，其含义是指 `Expr1 andalso Expr2` 这样一个表达式只有在Expr1为真的情况下才会执行Expr2。同样可以理解一下orelse这个短路布尔表达式。而普通的布尔表达式和其他语言里一样的，not, and, or, xor。  

{% highlight erlang %}

%% suffix(Suffix, List) -> (true | false)

-spec suffix(List1, List2) -> boolean() when
      List1 :: [T],
      List2 :: [T],
      T :: term().

suffix(Suffix, List) ->
    Delta = length(List) - length(Suffix),
    Delta >= 0 andalso nthtail(Delta, List) =:= Suffix.

{% endhighlight %}  

## 4. seq/2  
　　seq/2是一个高级接口，调用了一个三参数的接口`seq_loop(N, X, L)`，如下，其中N=Last-First+1，是需要生成的长度，X=Last，是最后一个元素的值，L是一个空列表[]，将结果保存到第三个参数L中，最后再返回它。而生成这个列表的方法确实很高效，要么一次生成4个数，要么一次生成2个数，要么生成一个数或者直接返回结果。而实际应用中，大多数情况应该都是一次生成4个数，然后可能会调用1到2次一次生成2个数，最后要么直接返回结果，要么就再生成1个数后再返回结果。极为高效！我又想起了Python里相似的range函数，过两天看看Python里是怎么实现的。  

{% highlight erlang %}

-spec seq(From, To) -> Seq when
      From :: integer(),
      To :: integer(),
      Seq :: [integer()].

seq(First, Last)
    when is_integer(First), is_integer(Last), First-1 =< Last ->
    seq_loop(Last-First+1, Last, []).

seq_loop(N, X, L) when N >= 4 ->
     seq_loop(N-4, X-4, [X-3,X-2,X-1,X|L]);
seq_loop(N, X, L) when N >= 2 ->
     seq_loop(N-2, X-2, [X-1,X|L]);
seq_loop(1, X, L) ->
     [X|L];
seq_loop(0, _, L) ->
     L.

{% endhighlight %}  

## 5. sort/1  
　　Link:   

## 6. merge/1 
　　Link: 

## 7. concat/1   
　　concat函数本身的意图是把参数组合成一个项式，特别需要注意的是，当这个项式是可打印的时候，就打印其字符串形式的结果，当该项式是不可打印的时候，就以把它组合成一个list形式。我们先看下面的例子： 

{% highlight shell %}  

root@kali:~/Desktop/erlcode/lists# erl
Erlang/OTP 17 [erts-6.1] [source] [64-bit] [smp:4:4] [async-threads:10] [hipe] [kernel-poll:false]

Eshell V6.1  (abort with ^G)
1> lists:concat([1,2,3]).
"123"
2> lists:concat([1,2,3,a,b,c]).
"123abc"
3> lists:concat([1,2,3,[a,b,c]]).
[49,50,51,a,b,c]
4> lists:concat([1,2,3,[1,2,3]]).
[49,50,51,1,2,3]
5> lists:concat([1,2,3,a,b,c,[1,2,3]]).
[49,50,51,97,98,99,1,2,3]
6> lists:concat([1,2,3,a,b,c,[1,2,[a,b,c],3]]).
[49,50,51,97,98,99,1,2,[a,b,c],3]
7> lists:concat([1,2,3,a,b,c,[1,2,[a,b,c],3],d,e,f]).
[49,50,51,97,98,99,1,2,[a,b,c],3,100,101,102]

{% endhighlight %}  

　　从例子1、2可以看出，若参数是一个无嵌套的term组成的list，则会返回由这些term组成的一个字符串；若参数是含有嵌套的list，则会把最外层term打印成其在ASCII中的下标，而嵌套的会保持原形。我想这个函数一般都会用在无嵌套的情况吧。下面是源码。  

{% highlight erlang %}

%% concat(L) concatenate the list representation of the elements
%%  in L - the elements in L can be atoms, numbers of strings.
%%  Returns a list of characters.

-spec concat(Things) -> string() when
      Things :: [Thing],
      Thing :: atom() | integer() | float() | string().

concat(List) ->
    flatmap(fun thing_to_list/1, List).

thing_to_list(X) when is_integer(X) -> integer_to_list(X);
thing_to_list(X) when is_float(X)   -> float_to_list(X);
thing_to_list(X) when is_atom(X)    -> atom_to_list(X);
thing_to_list(X) when is_list(X)    -> X.       %Assumed to be a string

-spec flatmap(Fun, List1) -> List2 when
      Fun :: fun((A) -> [B]),
      List1 :: [A],
      List2 :: [B],
      A :: term(),
      B :: term().

flatmap(F, [Hd|Tail]) ->
    F(Hd) ++ flatmap(F, Tail);
flatmap(F, []) when is_function(F, 1) -> [].

{% endhighlight %}  

## 8. flatten/1, flatten/2   

　　flatten/1 和 flatten/2 都是把一个有嵌套的list返回成一个无嵌套的list的函数，其中flatten/2允许在flatten/1的结果后再append一个list，而且不管这个list的形式。其实一会儿可以在源码里看见，flatten/1和flatten/2的唯一区别是flatten/1相当于flatten/2的第二个参数是一个空list。  

{% highlight erlang %}  

-spec flatten(DeepList) -> List when
      DeepList :: [term() | DeepList],
      List :: [term()].

flatten(List) when is_list(List) ->
    do_flatten(List, []).

-spec flatten(DeepList, Tail) -> List when
      DeepList :: [term() | DeepList],
      Tail :: [term()],
      List :: [term()].

flatten(List, Tail) when is_list(List), is_list(Tail) ->
    do_flatten(List, Tail).

do_flatten([H|T], Tail) when is_list(H) ->
    do_flatten(H, do_flatten(T, Tail));
do_flatten([H|T], Tail) ->
    [H|do_flatten(T, Tail)];
do_flatten([], Tail) ->
    Tail.

{% endhighlight %}  

## 10. filter/2, map/2, filtermap/2

　　先看看函数参数，filter函数是对List1里的每个term都应用一次Pred函数，然后将能使Pred函数返回true的元素按序构成一个新的列表返回。map函数是对List1里对每个term都应用一次Fun函数，然后将Fun函数在每个元素上都返回值按顺序构造成返回值。顾名思义，filtermap函数就是这两个函数的结合，即先filter，再做map操作。下面是源码，有时候发现，如果看document看烦了，可以选择性地看看源码，也许比看document管用。  

{% highlight erlang %}

-spec map(Fun, List1) -> List2 when
      Fun :: fun((A) -> B),
      List1 :: [A],
      List2 :: [B],
      A :: term(),
      B :: term().

map(F, [H|T]) ->
    [F(H)|map(F, T)];
map(F, []) when is_function(F, 1) -> [].

-spec filter(Pred, List1) -> List2 when
      Pred :: fun((Elem :: T) -> boolean()),
      List1 :: [T],
      List2 :: [T],
      T :: term().

filter(Pred, List) when is_function(Pred, 1) ->
    [ E || E <- List, Pred(E) ].   

-spec filtermap(Fun, List1) -> List2 when
      Fun :: fun((Elem) -> boolean() | {'true', Value}),
      List1 :: [Elem],
      List2 :: [Elem | Value],
      Elem :: term(),
      Value :: term().

filtermap(F, [Hd|Tail]) ->
    case F(Hd) of
  true ->
      [Hd|filtermap(F, Tail)];
  {true,Val} ->
      [Val|filtermap(F, Tail)];
  false ->
      filtermap(F, Tail)
    end;
filtermap(F, []) when is_function(F, 1) -> [].

{% endhighlight %}  


## 扫一扫     

![2014-10-31-erlang-lists-source-code.md](../../images/share/2014-10-31-erlang-lists-source-code.md.jpg)