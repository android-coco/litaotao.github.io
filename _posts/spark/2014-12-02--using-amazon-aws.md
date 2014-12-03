---
category: spark
published: false
layout: post
title: ［touch spark］3. Amazon AWS 使用攻略
description: 准备在AWS上跑spark的看过来了~~~
---  

##  
## 1. 申请Amazon AWS账号   
　　申请Amazon AWS需要绑定信用卡，无奈兄弟我从来没用过信用卡，所以只能跑到[global cash](https://www.globalcash.hk/)申请一张虚拟信用卡了。有关申请虚拟信用卡的教程[这里](http://www.freehao123.com/globalcash/)已经有了，我就不重复了。

## 2. 在EC2上创建一个spark集群  
### 2.1 前期准备  
　　本文中用到的所有脚本都是基于python 2.x写的，且在Linux和0S X上测试通过。  

### 2.2 创建EC2 keys  
　　首先确保你的地区是US EAST，在右上角可以选择区域，即帐号名右侧。还没找到的请看下图：  
![choose ec2 region](../../images/choose ec2 region.jpg)  

　　然后在帐号名->Security Credentials->Dashboard 下的 Details->Security Status->Manage Security Credentials->Access Keys->Create New Access Key创建keys，这里最好把keys记录下来，以后好用。  
　　设置变量，下面的KEY_ID, ACCESS_KEY是在你创建keys的时候产生的：

```  
export AWS_ACCESS_KEY_ID=<ACCESS_KEY_ID>
export AWS_SECRET_ACCESS_KEY=<SECRET_ACCESS_KEY>
```  

### 2.3 创建key pair  
　　在EC2 Dashboard左侧边栏->Network & Security->Key Pairs->Create Key Pair。这里会需要你输入一个key pair name，最好搞一个简单好记的，因为以后也会用到。创建成功后会自动下载一个用于后期验证登录的文件，下载该文件把其复制到用户家目录下，确保其权限至少是600，保险起见执行 chmod 600 key_pair_file。  

### 2.4 下载启动脚本  
```  
git clone git://github.com/amplab/ampcamp.git  
```  

### 2.5 建立并启动集群  
　　若上面的启动脚本下载成功后，本地会有一个ampcamp的文件夹，cd 到ampcamp文件夹里，执行下面命令启动集群。其中key_file是刚刚下载并复制到家目录下的验证文件，name_of_key_pair是你创建key_pair的时候自己命名的。  

``` 
./spark-ec2 -i <key_file> -k <name_of_key_pair> --copy launch ampcamp
``` 

　　上面这个过程大约会持续15-20分钟，耐心等待一下。如果期间出现下面这个问题，那是因为没有把key_pair文件复制到家目录下去。

```
rsync: connection unexpectedly closed (0 bytes received so far) [sender]
rsync error: unexplained error (code 255) at io.c(605) [sender=3.0.9]
Traceback (most recent call last):
  File "./spark_ec2.py", line 759, in <module>
    main()
  File "./spark_ec2.py", line 648, in main
    setup_cluster(conn, master_nodes, slave_nodes, zoo_nodes, opts, True)
  File "./spark_ec2.py", line 363, in setup_cluster
    deploy_files(conn, "deploy.generic", opts, master_nodes, slave_nodes, zoo_nodes)
  File "./spark_ec2.py", line 604, in deploy_files
    subprocess.check_call(command, shell=True)
  File "/root/anaconda/lib/python2.7/subprocess.py", line 540, in check_call
    raise CalledProcessError(retcode, cmd)
subprocess.CalledProcessError: Command 'rsync -rv -e 'ssh -o StrictHostKeyChecking=no -i ../company.pem' '/tmp/tmp6YpLzV/' 'root@ec2-54-172-219-206.compute-1.amazonaws.com:/'' returned non-zero exit status 255
root@ubuntu2:~/Desktop/spark/ampcamp# cp ../company.pem .
```  

　　如果一切顺利（但愿），最后会有消息提示创建成功：SUCCESS: Cluster successfully launched! You can login to the master at ***


### 2.6 其他相关命令    
　　第一个命令获取ampcamp集群的master节点，这个需要在集群启动成功后执行一次，因为后续也要用到这个节点地址，所以最好把master 节点地址记录下来。第二个命令是删除集群。    

```  
./spark-ec2 -i <key_file> -k <key_pair> get-master ampcamp   
./spark-ec2 -i <key_file> -k <key_pair> destroy ampcamp  
```  


