---
layout: post
published: false
title: 使用celery常见的错误  
description: 记录我在使用celery过程中遇到过的一些错误。
---  


##  
## 1. Celery task always PENDING

- 错误信息：
    + 在celery日志里发现任务已经执行成功，但在客户端不能获取任务结果，且任务状态一直显示为"PENDING"。

- 代码结构：
    + 在SO上已经有这个问题的答案了，详细可以在看[这里](http://stackoverflow.com/questions/27357732/celery-task-always-pending)。

    ```
        from celery import Celery

        app = Celery('risktools.distributed.celery_tasks',
                     backend='redis://localhost',
                     broker='redis://localhost')

        @app.task(ignore_result=False)
        def add(x, y):
            return x + y

        @app.task(ignore_result=False)
        def add_2(x, y):
            return x + y
    ```

    + 客户端操作如下：

    ```
    >>> result_1 = add.delay(1, 2)    
    >>> result_1.state
    'PENDING'
    >>> result_2 = add_2.delay(2, 3)    
    >>> result_2.state
    'PENDING'
    ```

    + celery 服务端日志如下：

    ```
    celery -A celery1 worker --loglevel=info 
    ...
    ...
    ...
    [2014-12-08 15:00:09,262: INFO/MainProcess] Received task: risktools.distributed.celery_tasks.add[01dedca1-2db2-48df-a4d6-2f06fe285e45]
    [2014-12-08 15:00:09,267: INFO/MainProcess] Task celery_tasks.add[01dedca1-2db2-48df-a4d6-2f06fe28
    5e45] succeeded in 0.0019998550415s: 3
    [2014-12-08 15:00:24,219: INFO/MainProcess] Received task: risktools.distributed.celery_tasks.add[cb5505ce-cf93-4f5e-aebb-9b2d98a11320]
    [2014-12-08 15:00:24,230: INFO/MainProcess] Task celery_tasks.add[cb5505ce-cf93-4f5e-aebb-9b2d98a1
    1320] succeeded in 0.010999917984s: 5
    ```

- 分析及解决方案
    + 在celery服务端日志里有一个 **concurrency**的配置项，应该是指处理并发方式，默认是以fork方式来处理并发的。可是windows下的python是不支持fork操作的，根据上面那个SO的回答和日志分析，我猜想应该是这个原因。下面是这个日志：

    ```
     -------------- celery@SHN1408GPVG612 v3.1.17 (Cipater)
    ---- **** -----
    --- * ***  * -- Windows-7-6.1.7601-SP1
    -- * - **** ---
    - ** ---------- [config]
    - ** ---------- .> app:         celery1:0x3b62080
    - ** ---------- .> transport:   redis://10.20.70.80:6379/0
    - ** ---------- .> results:     redis://10.20.70.80:6379/1
    - *** --- * --- .> concurrency: 4 (prefork)
    -- ******* ----
    --- ***** ----- [queues]
     -------------- .> celery           exchange=celery(direct) key=celery
    ```

    + windows下的python不支持fork操作的示例：

    ```
    ### windows
    In [1]: import os

    In [2]: print os.getpid()
    14524

    In [3]: help(os.fork)
    ---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)
    <ipython-input-3-51bc700bdf1d> in <module>()
    ----> 1 help(os.fork)

    AttributeError: 'module' object has no attribute 'fork'

    In [4]:

    ### linux
    In [1]: import os 

    In [2]: print os.getpid()
    437

    In [3]: help(os.fork)
    Help on built-in function fork in module posix:

    fork(...)
        fork() -> pid
        
        Fork a child process.
        Return 0 to child process and PID of child to parent process.

    In [4]: 

    ```

    + 解决方法：在启动celery服务端的时候加上 pool 参数，指定为solo，这个时候看到concurrency的值变了，不再是默认值fork。

    ```
    celery -A celery1 worker --loglevel=info  --pool=solo
    ...
    ...
    ...
     -------------- celery@SHN1408GPVG612 v3.1.17 (Cipater)
    ---- **** -----
    --- * ***  * -- Windows-7-6.1.7601-SP1
    -- * - **** ---
    - ** ---------- [config]
    - ** ---------- .> app:         celery1:0x3b6f5c0
    - ** ---------- .> transport:   redis://10.20.70.80:6379/0
    - ** ---------- .> results:     redis://10.20.70.80:6379/1
    - *** --- * --- .> concurrency: 4 (solo)
    -- ******* ----
    --- ***** ----- [queues]
     -------------- .> celery
     ...
     ...
     ...
    ```

- 参考：
    + StackOverflow：[SO](http://stackoverflow.com/questions/27357732/celery-task-always-pending)
    + StackOverflow: [SO](https://stackoverflow.com/questions/25495613/celery-getting-started-not-able-to-retrieve-results-always-pending)
    + Github Issue: [Github](https://github.com/celery/celery/issues/2146)




## 扫一扫     

![2015-01-20-errors-using-celery.md](../../images/share/2015-01-20-errors-using-celery.md.jpg)