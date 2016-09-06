---
category: erlang
published: false
layout: post
title: 如何调试Erlang程序
description: 简单试用下Erlang下的调试方法和工具
---

## I. 从我在Erlang and OTP in Action中第六章中的错误说起
　　前两天看EOIA这本书，觉得终于可以用Erlang来搞点东西玩了，于是决定按照书中流程来实践一下所谓的缓存系统。
谨慎起见，我还是半抄半写把simple_cache的源码写好了，当前目录结构如下：

```
chenshan@mac007 6-EOIA$tree
.
├── ebin
│   ├── prim_consult.beam
│   ├── sc_app.beam
│   ├── sc_element.beam
│   ├── sc_store.beam
│   ├── sc_sup.beam
│   ├── simple_cache.app
│   └── simple_cache.beam
└── src
    ├── prim_consult.beam
    ├── prim_consult.erl
    ├── sc_app.erl
    ├── sc_element.erl
    ├── sc_store.erl
    ├── sc_sup.erl
    └── simple_cache.erl
```

**小提示：**   
> 1、要把src目录下的erl源文件编译，并把编译后的beam文件放到ebin下有一个快捷的方法，在当前目录下执行：erlc -o ebin/ src/*.erl；  
> 2、上面出现的prim_consult.erl和prim_consult.beam不用管，后面会提到的，这是我阅读application源码时提取出来的； 

　　然后进入ebin目录，打开erlang执行环境，用application:start(simple_cache).启动我们的缓存系统，opps，这个时候就出错了。   

```
chenshan@mac007 6-EOIA$cd ebin/
chenshan@mac007 ebin$erl
Erlang/OTP 17 [erts-6.1] [source] [64-bit] [smp:4:4] [async-threads:10] [hipe] [kernel-poll:false]

Eshell V6.1  (abort with ^G)
1> application:start(simple_cache).  
{error,
    {bad_return,
        {
        {sc_app,start,[normal,[]]},
         {'EXIT',
             {undef,
                 [{sr_store,init,[],[]},
                  {sc_app,start,2,[{file,"../src/sc_app.erl"},{line,6}]},
                  {application_master,start_supervisor,3,
                      [{file,"application_master.erl"},{line,326}]},
                  {application_master,start_the_app,5,
                      [{file,"application_master.erl"},{line,308}]},
                  {application_master,start_it_new,7,
                      [{file,"application_master.erl"},{line,294}]}]}}}}}

=INFO REPORT==== 22-Oct-2014::23:47:18 ===
    application: simple_cache
    exited: {bad_return,
                {
                {sc_app,start,[normal,[]]},
                 {'EXIT',
                     {undef,
                         [{sr_store,init,[],[]},
                          {sc_app,start,2,
                              [{file,"../src/sc_app.erl"},{line,6}]},
                          {application_master,start_supervisor,3,
                              [{file,"application_master.erl"},{line,326}]},
                          {application_master,start_the_app,5,
                              [{file,"application_master.erl"},{line,308}]},
                          {application_master,start_it_new,7,
                              [{file,"application_master.erl"},
                               {line,294}]}]}}}}
    type: temporary
2> 
```

## II. 看看application行为在启动一个otp应用的简单流程
　　首先，在erlang环境下执行code:which(application)查看application编译后的文件路径：

```
Eshell V6.1  (abort with ^G)
1> code:which(application).
"/usr/local/lib/erlang/lib/kernel-3.0.1/ebin/application.beam"
```

　　然后，找到application的源文件，熟悉OTP项目目录结构的同志应该很清楚这里应该怎么做了吧，回顾一下OTP项目目录结构：  
> 
* doc  存放文档；
+ ebin  存放编译后的代码以及应用包含应用元数据的app文件；
- include  存放公共头文件；
- priv  存放各种需要随应用一起发布的其他内容，如模板文件，共享文件对象以及DLL等；
- src  存放应用源代码；

　　所以简单就能找到application的源文件了，在/usr/local/lib/erlang/lib/kernel-3.0.1/src/下面，这个目录里面还有其他源文件，安全、简单的方法是拷贝到临时目录里来看，看下面：  

```
root@kali:~/Desktop/erl/6-EOIA/ebin# mkdir ~/Desktop/temp
root@kali:~/Desktop/erl/6-EOIA/ebin# cp /usr/local/lib/erlang/lib/kernel-3.0.1/src/application*.erl ~/Desktop/ temp/
root@kali:~/Desktop/erl/6-EOIA/ebin# ls ~/Desktop/te
temp/ test/
root@kali:~/Desktop/erl/6-EOIA/ebin# ls ~/Desktop/temp/
application_controller.erl  application.erl  application_master.erl  application_starter.erl
```

　　Ok, 一切就绪，开干了！先在application.erl里找到start这个函数，如下。  

```
-spec start(Application) -> 'ok' | {'error', Reason} when
      Application :: atom(),
      Reason :: term().

start(Application) ->
    start(Application, temporary).

-spec start(Application, Type) -> 'ok' | {'error', Reason} when
      Application :: atom(),
      Type :: restart_type(),
      Reason :: term().

start(Application, RestartType) ->
    case load(Application) of
  ok ->
      Name = get_appl_name(Application),
      application_controller:start_application(Name, RestartType);
  {error, {already_loaded, Name}} ->
      application_controller:start_application(Name, RestartType);
  Error ->
      Error
    end.
```

　　可以发现，start已经是一个很高层的封装了，源代码注释里也说了，application.erl只是对application_master.erl和application_controller.erl的一个封装。这里我们是调用了start/1，即以temporary为重启方式来启动我们的simple_cache。start过程从宏观上分为两大步：load和start。其中先load，后start，load的结果有三种：  
> 
- ok：加入start流程；  
- {error, {already_loaded, Name}}：失败，原因是这个应用已经load过了，可以直接加入start流程；  
- Error：错误，且错误原因不详，需要看console里的输出分析； 

　　Ok, 思路清晰了，我们就split it into two seperate but sequential procedures，一步一步来，争取最后不靠调试就解决我们上面遇到的问题吧， here we go！


## III. load应用的过程分析   

![load 流程图分析](../../images/erlang-application-load.jpg)




## IV. start应用的过程分析



## V. 挖掘程序错误















理论上来讲，这是个很简单的事情，甚至可以说不能再简单了。

1. 在VirtualBox里面建一个OpenSolaris 64bit的虚拟机，配置足够大的内存和硬盘
2. 把[SmartOS live ISO](https://us-east.manta.joyent.com/Joyent_Dev/public/SmartOS/smartos-latest.iso)挂载在光驱上
3. 启动，回答屏幕上几个问题，搞定

没错，SmartOS就是这么简单。甚至可以用个[简单的脚本](http://www.perkin.org.uk/posts/automated-virtualbox-smartos-installs.html)自动化完成。

## 创建SmartOS zone

SmartOS里面的zone就是OS container，轻量级，隔离性好，所以一般搞搞都先弄一个，简单的应该是这么搞搞就行了

先导入镜像

```
imgadm import fdea06b0-3f24-11e2-ac50-0b645575ce9d
```

然后创建一个json描述文件

```
cd /opt
vi myvm.json
```



```json
{
 "brand": "joyent",
 "image_uuid": "fdea06b0-3f24-11e2-ac50-0b645575ce9d",
 "alias": "web01",
 "hostname": "web01",
 "max_physical_memory": 512,
 "quota": 20,
 "nics": [
  {
    "nic_tag": "admin",
    "ip": "10.88.88.52",
    "netmask": "255.255.255.0",
    "gateway": "10.88.88.2"
  }
 ]
}
```

最后

```
vmadm create -f myvm.json
```

完事了`zlogin`到你的机器就行了。

好了我就不班门弄斧了，我都是从[这里](http://wiki.smartos.org/display/DOC/How+to+create+a+zone+%28+OS+virtualized+machine+%29+in+SmartOS)抄的。

## 老湿，我的zone上不了外网啊！

**更新：这件事情在最新版的SmartOS中应该已经修复了，见[这里](http://www.listbox.com/member/archive/184463/2014/05/sort/time_rev/page/1/entry/14:199/20140525031110:BCCD6764-E3DB-11E3-AC74-888FDBEDD5D3/)。**

_以下内容应该已经过时，但是还是留下做个参考吧_

> VirtualBox我设置成NAT了？啥啥我也设对了？问题解决不了，joyent的源码我都快看完了，我的zone还是上不了外网啊？？？？？？

我也上不了 :)

在joyent的SmartOS wiki看到这么点[信息](http://wiki.smartos.org/display/DOC/How+to+create+a+Virtual+Machine+in+SmartOS)(页内搜索Zone Networking Issues)。老实说，给出了方向，连接都失效了，细节全留给你自己想了。一句话，领导风范。

具体的这事情是这样：

1. 默认SmartOS ISO只针对vmware做了优化，所以默认建了个vmware的bridge，还把默认网卡绑上了。
用`dladm show-link`看看，有个`vmwarebr`吧。

2. 按照joyent指出的方向，问题就在要建一个叫做`vboxbr`而不是`vmwarebr`。看来是硬编码问题，典型的扯淡问题。

那么来做

先删了那个vmwarebr

```
dladm remove-bridge -l e1000g0 vmwarebr
dladm delete-bridege vmwarebr
```

再建一个

```
dladm create-bridge -l e1000g0 vboxbr
```

理论上讲这样就行了。不用重启zone，就行了。joyent是这么保证的，但是实际上有点问题，可能要把某zone删了重来（或者重新配置网络）。注意zone的网卡的mask和gateway要和e1000g0的一致。

举个栗子吧

```
[root@08-00-27-1e-28-f6 ~]# netstat -rn

Routing Table: IPv4
  Destination           Gateway           Flags  Ref     Use     Interface
-------------------- -------------------- ----- ----- ---------- ---------
default              10.0.2.2             UG        4     122171 e1000g0
10.0.2.0             10.0.2.15            U         3          0 e1000g0
127.0.0.1            127.0.0.1            UH        2         84 lo0
192.168.56.0         192.168.56.13        U         4     223275 e1000g1
```

可见主网卡`e1000g0`的gateway是`10.0.2.2`，网段是`10.0.2.x`。那么zone的nic就应该如下配置

```json
{
  "nics": [
    {
      "nic_tag": "admin",
      "ip": "10.0.2.52",
      "netmask": "255.255.255.0",
      "gateway": "10.0.2.2"
    }
  ]
}
```

其中`ip`那里我随便选了个`10.0.2.52`，反正不和别的机器冲突就行。


## 扫一扫     

![2014-10-27-how-to-debug-erlang-programs.md](../../images/share/2014-10-27-how-to-debug-erlang-programs.md.jpg)