---  
category: erlang  
published: false  
layout: post  
title: 那些年没错过的 Erlang 错误  
description: 记录 Erlang 实践过程中遇到过的错误  
---  
   

## Could not find wxe_driver.so  

Key words: wxe_driver.so, debugger, observer, osx, linux, windows
Problems:  

```
chenshan@mac007 lists$erl
Erlang/OTP 17 [erts-6.1] [source] [64-bit] [smp:4:4] [async-threads:10] [hipe] [kernel-poll:false]

Eshell V6.1  (abort with ^G)
1> debugger:start().
{error,{ {load_driver,"No driver found"},
        [{wxe_server,start,1,[{file,"wxe_server.erl"},{line,64}]},
         {wx,new,1,[{file,"wx.erl"},{line,114}]},
         {dbg_wx_mon,init,3,[{file,"dbg_wx_mon.erl"},{line,113}]}]}}

=ERROR REPORT==== 4-Nov-2014::23:34:28 ===
ERROR: Could not find 'wxe_driver.so' in: /usr/local/lib/erlang/lib/wx-1.3/priv
2> 
```  

Solutions:  
1. [solution 1, failed](http://stackoverflow.com/questions/21297465/erlang-debugger-error-could-not-find-wxe-driver-so)
> brew install wxmac  

## 2. 

