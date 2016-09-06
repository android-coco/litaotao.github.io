---
layout: post
published: true
title: 『 Tips 』SSH 免密码登录
description: 配置 ssh 免密码登录哦～
---  


## 写在前面

每次登录远程服务器都要输密码！！！

![no-way](../images/no-way.gif)


## 1. 事前准备

- 本地机器：local
- 远程机器：remote

## 2. 实操步骤

- 本地机器生成公钥，私钥: `ssh-keygen -t rsa`

{% highlight shell %}

taotao@mac007:~$ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/Users/chenshan/.ssh/id_rsa): /Users/chenshan/.ssh/id_rsa_test
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /Users/chenshan/.ssh/id_rsa_test.
Your public key has been saved in /Users/chenshan/.ssh/id_rsa_test.pub.
The key fingerprint is:
SHA256:gYV/PFrA08nktGUZ8LlFJ/Fhg7wDRjYQslmwf4UYJZc taotao@mac007
The key's randomart image is:
+---[RSA 2048]----+
|       =oXOO*o==.|
|      .oXoXE+=.+o|
|      .=.=+.+.o .|
|        o.= .=   |
|        S= o. .  |
|        . .      |
|                 |
|                 |
|                 |
+----[SHA256]-----+

taotao@mac007:~$ls ~/.ssh/ | grep test
id_rsa_test
id_rsa_test.pub

{% endhighlight %}

- 上传本地公钥到远程机器: `scp ~/.ssh/id_rsa_test.pub username@remote:.ssh/id_rsa_test.pub`

{% highlight shell %}

taotao@mac007:~$ scp ~/.ssh/id_rsa_test.pub username@remote:.ssh/id_rsa_test.pub
username@remote's password:
id_rsa_test.pub                                                                                   100%  412     0.4KB/s   00:00

{% endhighlight %}

- 在远程机器上设置 `authorized_keys` : `cat /root/.ssh/id_rsa_test.pub  >> /root/.ssh/authorized_keys`

## 3. 完成
