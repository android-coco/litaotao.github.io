---
category: python
published: false
layout: post
title: 伴我一路走来的那些bug们，你们好    
description: bug，永远是程序员最忠实的朋友，你打他骂他虐他，他还是一如既然滴追随你~~~
---    


## 1. failed to write data to stream

- 环境：ipython, OSX
- 操作：在ipython里import 一个pure module
- 描述： Python - ERROR - failed to write data to stream: <open file '<stdout>', mode 'w' at 0x104c8f150>
- 办法：export PYTHONIOENCODING=UTF-8 will solve it.
- 相关：[stackoverflow](http://stackoverflow.com/questions/28115375/python-error-failed-to-write-data-to-stream-open-file-stdout-mode-w)


## 2. Git: fatal: Pathspec is in submodule

- 环境：OSX, Git
- 操作：git add *
- 描述：有一个github repo [暂且叫father]，其中这个repo里有子module [暂且叫 child]，且这个child也是作为一个独立的github repo存在，我更改了child下的一些文件，然后在father下执行git add，准备在father下直接commit和push，执行git add 的时候出错，提示 `Pathspec is in submodule`。
- 办法：现在child下add，commit和push，然后再到father下add，commit和push；   
- 相关：最好的方式是：在child下git branch 一个新的分支，然后在这个分支上修改，然后add，commit，push；修改好child后，再到father下新建一个分支，执行add，commit，push。最后，要merge的时候，也是先merge掉child，然后再merge掉father。因为child作为一个独立的repo，所有的更改都要在child这个独立repo下面做更改，由于项目需要，child作为father的一个子module，不能直接在father里更改child然后再add，commit，push。因为father里的child，只是链接到了child这个独立repo。或者说，father里的child只是独立的child的一个只读镜像。   

