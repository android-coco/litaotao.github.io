---
category: tools
published: false
layout: post
title: 我常用到的linux命令
description: 记录我80%时间里用到的那些linux命令～
---  

##  
## 1. ps
　　Linux中的ps命令是Process Status的缩写。ps命令用来列出系统中当前运行的那些进程。ps命令列出的是当前那些进程的快照，就是执行ps命令的那个时刻的那些进程，如果想要动态的显示进程信息，就可以使用top命令。  
　　要对进程进行监测和控制，首先必须要了解当前进程的情况，也就是需要查看当前进程，而 ps 命令就是最基本同时也是非常强大的进程查看命令。使用该命令可以确定有哪些进程正在运行和运行的状态、进程是否结束、进程有没有僵死、哪些进程占用了过多的资源等等。总之大部分信息都是可以通过执行该命令得到的。     
　　kill 命令用于杀死进程。   
　　linux上进程有5种状态:    

- 运行(正在运行或在运行队列中等待)    
- 中断(休眠中, 受阻, 在等待某个条件的形成或接受到信号)    
- 不可中断(收到信号不唤醒和不可运行, 进程必须等待直到有中断发生)    
- 僵死(进程已终止, 但进程描述符存在, 直到父进程调用wait4()系统调用后释放)    
- 停止(进程收到SIGSTOP, SIGSTP, SIGTIN, SIGTOU信号后停止运行运行)    

　　ps工具标识进程的5种状态码:   

- D 不可中断 uninterruptible sleep (usually IO) 
- R 运行 runnable (on run queue) 
- S 中断 sleeping 
- T 停止 traced or stopped 
- Z 僵死 a defunct (”zombie”) process 

- 命令格式：
ps[参数]
- 命令功能：  
用来显示当前进程的状态  
- 命令参数：    

        a  显示所有进程
        -a 显示同一终端下的所有程序
        -A 显示所有进程
        c  显示进程的真实名称
        -N 反向选择
        -e 等于“-A”
        e  显示环境变量
        f  显示程序间的关系
        -H 显示树状结构
        r  显示当前终端的进程
        T  显示当前终端的所有程序
        u  指定用户的所有进程
        -au 显示较详细的资讯
        -aux 显示所有包含其他使用者的行程 
        -C<命令> 列出指定命令的状况
        --lines<行数> 每页显示的行数
        --width<字符数> 每页显示的字符数
        --help 显示帮助信息
        --version 显示版本显示
 
实例1：显示所有进程信息  
命令：
ps -A  
输出：  

    [root@localhost test6]# ps -A
      PID TTY          TIME CMD
        1 ?        00:00:00 init
        2 ?        00:00:01 migration/0
        3 ?        00:00:00 ksoftirqd/0
      217 ?        00:00:00 cqueue/0
      ……省略部分结果

实例2：显示指定用户信息  
命令：  
ps -u root  
输出：  

    [root@localhost test6]# ps -u root
      PID TTY          TIME CMD
        1 ?        00:00:00 init
        2 ?        00:00:01 migration/0
       54 ?        00:00:00 kblockd/0
       55 ?        00:00:00 kblockd/1
       56 ?        00:00:00 kacpid
        ……省略部分结果

实例3：显示所有进程信息，连同命令行   
命令：  
ps -ef  
输出：  

    [root@localhost test6]# ps -ef
    UID        PID  PPID  C STIME TTY          TIME CMD
    root         1     0  0 Nov02 ?        00:00:00 init [3]                  
    root         2     1  0 Nov02 ?        00:00:01 [migration/0]
    root        54    49  0 Nov02 ?        00:00:00 [kblockd/0]
    root        55    49  0 Nov02 ?        00:00:00 [kblockd/1]
    root        56    49  0 Nov02 ?        00:00:00 [kacpid]
    ……省略部分结果

实例4： ps 与grep 常用组合用法，查找特定进程   
命令：  
ps -ef|grep ssh  
输出：  

    [root@localhost test6]# ps -ef|grep ssh
    root      2720     1  0 Nov02 ?        00:00:00 /usr/sbin/sshd
    root     17394  2720  0 14:58 ?        00:00:00 sshd: root@pts/0 
    root     17465 17398  0 15:57 pts/0    00:00:00 grep ssh

实例5：将目前属于您自己这次登入的 PID 与相关信息列示出来  
命令： 
ps -l  
输出：  

    [root@localhost test6]# ps -l
    F S   UID   PID  PPID  C PRI  NI ADDR SZ WCHAN  TTY          TIME CMD
    4 S     0 17398 17394  0  75   0 - 16543 wait   pts/0    00:00:00 bash
    4 R     0 17469 17398  0  77   0 - 15877 -      pts/0    00:00:00 ps
说明：  
各相关信息的意义：  

    F 代表这个程序的旗标 (flag)， 4 代表使用者为 super user
    S 代表这个程序的状态 (STAT)，关于各 STAT 的意义将在内文介绍
    UID 程序被该 UID 所拥有
    PID 就是这个程序的 ID ！
    PPID 则是其上级父程序的ID
    C CPU 使用的资源百分比
    PRI 这个是 Priority (优先执行序) 的缩写，详细后面介绍
    NI 这个是 Nice 值，在下一小节我们会持续介绍
    ADDR 这个是 kernel function，指出该程序在内存的那个部分。如果是个 running的程序，一般就是 "-"
    SZ 使用掉的内存大小
    WCHAN 目前这个程序是否正在运作当中，若为 - 表示正在运作
    TTY 登入者的终端机位置
    TIME 使用掉的 CPU 时间。
    CMD 所下达的指令为何
    在预设的情况下， ps 仅会列出与目前所在的 bash shell 有关的 PID 而已，所以， 当我使用 ps -l 的时候，只有三个 PID

实例6：列出目前所有的正在内存当中的程序  
命令：  
ps aux  
输出：  

    [root@localhost test6]# ps aux
    USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
    root         1  0.0  0.0  10368   676 ?        Ss   Nov02   0:00 init [3]                  
    root         2  0.0  0.0      0     0 ?        S<   Nov02   0:01 [migration/0]
    root         3  0.0  0.0      0     0 ?        SN   Nov02   0:00 [ksoftirqd/0]
    root         4  0.0  0.0      0     0 ?        S<   Nov02   0:01 [migration/1]
    root         5  0.0  0.0      0     0 ?        SN   Nov02   0:00 [ksoftirqd/1]
    ……省略部分结果

说明：  

    USER：该 process 属于那个使用者账号的
    PID ：该 process 的号码
    %CPU：该 process 使用掉的 CPU 资源百分比
    %MEM：该 process 所占用的物理内存百分比
    VSZ ：该 process 使用掉的虚拟内存量 (Kbytes)
    RSS ：该 process 占用的固定的内存量 (Kbytes)
    TTY ：该 process 是在那个终端机上面运作，若与终端机无关，则显示 ?，另外， tty1-tty6 是本机上面的登入者程序，若为 pts/0 等等的，则表示为由网络连接进主机的程序。
    STAT：该程序目前的状态，主要的状态有
    R ：该程序目前正在运作，或者是可被运作
    S ：该程序目前正在睡眠当中 (可说是 idle 状态)，但可被某些讯号 (signal) 唤醒。
    T ：该程序目前正在侦测或者是停止了
    Z ：该程序应该已经终止，但是其父程序却无法正常的终止他，造成 zombie (疆尸) 程序的状态
    START：该 process 被触发启动的时间
    TIME ：该 process 实际使用 CPU 运作的时间
    COMMAND：该程序的实际指令

实例7：列出类似程序树的程序显示   
命令：  
ps -axjf  
输出：  

    [root@localhost test6]# ps -axjf
    Warning: bad syntax, perhaps a bogus '-'? See /usr/share/doc/procps-3.2.7/FAQ
     PPID   PID  PGID   SID TTY      TPGID STAT   UID   TIME COMMAND
        0     1     1     1 ?           -1 Ss       0   0:00 init [3]         
        1    49     1     1 ?           -1 S<       0   0:00 [kthread]
       49    54     1     1 ?           -1 S<       0   0:00  \_ [kblockd/0]
       49    55     1     1 ?           -1 S<       0   0:00  \_ [kblockd/1]
       49    56     1     1 ?           -1 S<       0   0:00  \_ [kacpid]

## 2. kill  
　　Linux中的kill命令用来终止指定的进程（terminate a process）的运行，是Linux下进程管理的常用命令。通常，终止一个前台进程可以使用Ctrl+C键，但是，对于一个后台进程就须用kill命令来终止，我们就需要先使用ps/pidof/pstree/top等工具获取进程PID，然后使用kill命令来杀掉该进程。kill命令是通过向进程发送指定的信号来结束相应进程的。在默认情况下，采用编号为15的TERM信号。TERM信号将终止所有不能捕获该信号的进程。对于那些可以捕获该信号的进程就要用编号为9的kill信号，强行“杀掉”该进程。   
- 命令格式：  
kill[参数][进程号]  
- 命令功能：  
　　发送指定的信号到相应进程。不指定型号将发送SIGTERM（15）终止指定进程。如果任无法终止该程序可用“-KILL” 参数，其发送的信号为SIGKILL(9)，将强制结束进程，使用ps命令或者jobs 命令可以查看进程号。root用户将影响用户的进程，非root用户只能影响自己的进程。
- 命令参数：  

        -l  信号，若果不加信号的编号参数，则使用“-l”参数会列出全部的信号名称
        -a  当处理当前进程时，不限制命令名和进程号的对应关系
        -p  指定kill 命令只打印相关进程的进程号，而不发送任何信号
        -s  指定发送信号
        -u  指定用户 

注意：  

- kill命令可以带信号号码选项，也可以不带。如果没有信号号码，kill命令就会发出终止信号(15)，这个信号可以被进程捕获，使得进程在退出之前可以清理并释放资源。也可以用kill向进程发送特定的信号。例如：
kill -2 123
它的效果等同于在前台运行PID为123的进程时按下Ctrl+C键。但是，普通用户只能使用不带signal参数的kill命令或最多使用-9信号。  
- kill可以带有进程ID号作为参数。当用kill向这些进程发送信号时，必须是这些进程的主人。如果试图撤销一个没有权限撤销的进程或撤销一个不存在的进程，就会得到一个错误信息。   
- 可以向多个进程发信号或终止它们。   
- 当kill成功地发送了信号后，shell会在屏幕上显示出进程的终止信息。有时这个信息不会马上显示，只有当按下Enter键使shell的命令提示符再次出现时，才会显示出来。   
- 应注意，信号使进程强行终止，这常会带来一些副作用，如数据丢失或者终端无法恢复到正常状态。发送信号时必须小心，只有在万不得已时，才用kill信号(9)，因为进程不能首先捕获它。要撤销所有的后台作业，可以输入kill 0。因为有些在后台运行的命令会启动多个进程，跟踪并找到所有要杀掉的进程的PID是件很麻烦的事。这时，使用kill 0来终止所有由当前shell启动的进程，是个有效的方法。    

实例1：列出所有信号名称   
命令：  
kill -l   
输出：  

    [root@localhost test6]# kill -l
     1) SIGHUP       2) SIGINT       3) SIGQUIT      4) SIGILL
     5) SIGTRAP      6) SIGABRT      7) SIGBUS       8) SIGFPE
     9) SIGKILL     10) SIGUSR1     11) SIGSEGV     12) SIGUSR2
    13) SIGPIPE     14) SIGALRM     15) SIGTERM     16) SIGSTKFLT
    17) SIGCHLD     18) SIGCONT     19) SIGSTOP     20) SIGTSTP
    21) SIGTTIN     22) SIGTTOU     23) SIGURG      24) SIGXCPU
    25) SIGXFSZ     26) SIGVTALRM   27) SIGPROF     28) SIGWINCH
    29) SIGIO       30) SIGPWR      31) SIGSYS      34) SIGRTMIN
    35) SIGRTMIN+1  36) SIGRTMIN+2  37) SIGRTMIN+3  38) SIGRTMIN+4
    39) SIGRTMIN+5  40) SIGRTMIN+6  41) SIGRTMIN+7  42) SIGRTMIN+8
    43) SIGRTMIN+9  44) SIGRTMIN+10 45) SIGRTMIN+11 46) SIGRTMIN+12
    47) SIGRTMIN+13 48) SIGRTMIN+14 49) SIGRTMIN+15 50) SIGRTMAX-14
    51) SIGRTMAX-13 52) SIGRTMAX-12 53) SIGRTMAX-11 54) SIGRTMAX-10
    55) SIGRTMAX-9  56) SIGRTMAX-8  57) SIGRTMAX-7  58) SIGRTMAX-6
    59) SIGRTMAX-5  60) SIGRTMAX-4  61) SIGRTMAX-3  62) SIGRTMAX-2
    63) SIGRTMAX-1  64) SIGRTMAX
说明：  
只有第9种信号(SIGKILL)才可以无条件终止进程，其他信号进程都有权利忽略。     下面是常用的信号：   

    HUP    1    终端断线
    INT     2    中断（同 Ctrl + C）
    QUIT    3    退出（同 Ctrl + \）
    TERM   15    终止
    KILL    9    强制终止
    CONT   18    继续（与STOP相反， fg/bg命令）
    STOP    19    暂停（同 Ctrl + Z）

实例2：得到指定信号的数值   
命令：  
输出：  

    [root@localhost test6]# kill -l KILL
    9[root@localhost test6]# kill -l SIGKILL
    9[root@localhost test6]# kill -l TERM
    15[root@localhost test6]# kill -l SIGTERM
    15[root@localhost test6]#

实例3：先用ps查找进程，然后用kill杀掉   
命令：  
kill [pid number]    
输出：  

    [root@localhost test6]# ps -ef|grep vim 
    root      3268  2884  0 16:21 pts/1    00:00:00 vim install.log
    root      3370  2822  0 16:21 pts/0    00:00:00 grep vim
    [root@localhost test6]# kill 3268 
    [root@localhost test6]# kill 3268 
    -bash: kill: (3268) - 没有那个进程
    [root@localhost test6]#

实例4：彻底杀死进程   
命令：   
kill –9 [pid number]   
输出：  

    [root@localhost test6]# ps -ef|grep vim 
    root      3268  2884  0 16:21 pts/1    00:00:00 vim install.log
    root      3370  2822  0 16:21 pts/0    00:00:00 grep vim
    [root@localhost test6]# kill –9 3268 
    [root@localhost test6]# kill 3268 
    -bash: kill: (3268) - 没有那个进程
    [root@localhost test6]#

实例5：杀死指定用户所有进程  
命令：  
kill -9 $(ps -ef | grep peidalinux)  
kill -u peidalinux  
输出：  

    [root@localhost ~]# kill -9 $(ps -ef | grep peidalinux) 
    [root@localhost ~]# kill -u peidalinux

实例6：init进程是不可杀的   
命令：  
kill -9 1   
输出：  

    [root@localhost ~]# ps -ef|grep init
    root         1     0  0 Nov02 ?        00:00:00 init [3]                  
    root     17563 17534  0 17:37 pts/1    00:00:00 grep init
    [root@localhost ~]# kill -9 1
    [root@localhost ~]# kill -HUP 1
    [root@localhost ~]# ps -ef|grep init
    root         1     0  0 Nov02 ?        00:00:00 init [3]                  
    root     17565 17534  0 17:38 pts/1    00:00:00 grep init
    [root@localhost ~]# kill -KILL 1
    [root@localhost ~]# ps -ef|grep init
    root         1     0  0 Nov02 ?        00:00:00 init [3]                  
    root     17567 17534  0 17:38 pts/1    00:00:00 grep init
    [root@localhost ~]#

说明：   
　　init是Linux系统操作中不可缺少的程序之一。所谓的init进程，它是一个由内核启动的用户级进程。内核自行启动（已经被载入内存，开始运行，并已初始化所有的设备驱动程序和数据结构等）之后，就通过启动一个用户级程序init的方式，完成引导进程。所以,init始终是第一个进程（其进程编号始终为1）。   其它所有进程都是init进程的子孙。init进程是不可杀的！  

## 3. netstat  
　　Netstat 命令用于显示各种网络相关信息，如网络连接，路由表，接口状态 (Interface Statistics)，masquerade 连接，多播成员 (Multicast Memberships) 等等。   
　　执行netstat后，其输出结果为:   

    Active Internet connections (w/o servers)
    Proto Recv-Q Send-Q Local Address Foreign Address State
    tcp 0 2 210.34.6.89:telnet 210.34.6.96:2873 ESTABLISHED
    tcp 296 0 210.34.6.89:1165 210.34.6.84:netbios-ssn ESTABLISHED
    tcp 0 0 localhost.localdom:9001 localhost.localdom:1162 ESTABLISHED
    tcp 0 0 localhost.localdom:1162 localhost.localdom:9001 ESTABLISHED
    tcp 0 80 210.34.6.89:1161 210.34.6.10:netbios-ssn CLOSE

    Active UNIX domain sockets (w/o servers)
    Proto RefCnt Flags Type State I-Node Path
    unix 1 [ ] STREAM CONNECTED 16178 @000000dd
    unix 1 [ ] STREAM CONNECTED 16176 @000000dc
    unix 9 [ ] DGRAM 5292 /dev/log
    unix 1 [ ] STREAM CONNECTED 16182 @000000df

　　从整体上看，netstat的输出结果可以分为两个部分：

　　一个是Active Internet connections，称为有源TCP连接，其中"Recv-Q"和"Send-Q"指%0A的是接收队列和发送队列。这些数字一般都应该是0。如果不是则表示软件包正在队列中堆积。这种情况只能在非常少的情况见到。

　　另一个是Active UNIX domain sockets，称为有源Unix域套接口(和网络套接字一样，但是只能用于本机通信，性能可以提高一倍)。
Proto显示连接使用的协议,RefCnt表示连接到本套接口上的进程号,Types显示套接口的类型,State显示套接口当前的状态,Path表示连接到套接口的其它进程使用的路径名。

- 常见参数  

    -a (all)显示所有选项，默认不显示LISTEN相关
    -t (tcp)仅显示tcp相关选项
    -u (udp)仅显示udp相关选项
    -n 拒绝显示别名，能显示数字的全部转化成数字。
    -l 仅列出有在 Listen (监听) 的服務状态

    -p 显示建立相关链接的程序名
    -r 显示路由信息，路由表
    -e 显示扩展信息，例如uid等
    -s 按各个协议进行统计
    -c 每隔一个固定时间，执行该netstat命令。

提示：LISTEN和LISTENING的状态只有用-a或者-l才能看到

实例 1. 列出所有端口 (包括监听和未监听的)：列出所有端口， netstat -a  

    # netstat -a | more
     Active Internet connections (servers and established)
     Proto Recv-Q Send-Q Local Address           Foreign Address         State
     tcp        0      0 localhost:30037         *:*                     LISTEN
     udp        0      0 *:bootpc                *:*
     
    Active UNIX domain sockets (servers and established)
     Proto RefCnt Flags       Type       State         I-Node   Path
     unix  2      [ ACC ]     STREAM     LISTENING     6135     /tmp/.X11-unix/X0
     unix  2      [ ACC ]     STREAM     LISTENING     5140     /var/run/acpid.socket


实例 2. 列出所有端口 (包括监听和未监听的)：列出所有 tcp 端口， netstat -at

    # netstat -at
     Active Internet connections (servers and established)
     Proto Recv-Q Send-Q Local Address           Foreign Address         State
     tcp        0      0 localhost:30037         *:*                     LISTEN
     tcp        0      0 localhost:ipp           *:*                     LISTEN
     tcp        0      0 *:smtp                  *:*                     LISTEN
     tcp6       0      0 localhost:ipp           [::]:*                  LISTEN

实例 3. 列出所有端口 (包括监听和未监听的)：列出所有 udp 端口， netstat -au  

    # netstat -au
     Active Internet connections (servers and established)
     Proto Recv-Q Send-Q Local Address           Foreign Address         State
     udp        0      0 *:bootpc                *:*
     udp        0      0 *:49119                 *:*
     udp        0      0 *:mdns                  *:*

实例 3. 找出程序运行的端口，并不是所有的进程都能找到，没有权限的会不显示，使用 root 权限查看所有的信息。  

    # netstat -ap | grep ssh
     tcp        1      0 dev-db:ssh           101.174.100.22:39213        CLOSE_WAIT  -
     tcp        1      0 dev-db:ssh           101.174.100.22:57643        CLOSE_WAIT  -

找出运行在指定端口的进程   

    # netstat -an | grep ':80'

实例 4. IP和TCP分析，查看连接某服务端口最多的的IP地址

    wss8848@ubuntu:~$ netstat -nat | grep "192.168.1.15:22" |awk '{print $5}'|awk -F: '{print $1}'|sort|uniq -c|sort -nr|head -20
    18 221.136.168.36
    3 154.74.45.242
    2 78.173.31.236
    2 62.183.207.98
    2 192.168.1.14
    2 182.48.111.215
    2 124.193.219.34
    2 119.145.41.2
    2 114.255.41.30
    1 75.102.11.99

备注：  
这篇 [blog](linux命令五分钟系列之四十三) 说netstat命令似乎已经不再维护了，后续将被ip和ss命令取代。那我们也来顺带了解一下ip和ss这两个命令吧。  
![netstat-replaced](../images/netstat_subsititute.jpg) 

## 4. ip  


## 5. ss  


## 6. vimdiff


## 扫一扫     

![2014-12-12-linux-commands.md](../../images/share/2014-12-12-linux-commands.md.jpg)