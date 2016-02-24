---
category: books
published: true
layout: post
title: 『 读书笔记 』 50 Tips and Tricks for MongoDB Developers
description: 仅仅是记录我个人的读书记录，看官不必在意～
---
  

## 写在前面
　　book 开头的文章都是记录我个人的读书记录的，里面分情况会记录下面这些东西：目录，读书感想，技术分享和推荐等。如果只是写下目录，那大多是留给自己以后看的。我不会把书长篇大论地翻译成中文，只会写下能对我个人以后真正有用的东西。
　　这是一本讲mongodb实践的经验书籍，就66页，除去前面目录什么的，也就50来页，对我个人还是挺有用的，所以我写下其目录，供以后复习时用。没必要写什么读书笔记，毕竟大脑才是最好用的u盘。  

## 目录
>
1. Duplicate data for speed, reference data for integrity
2. Normalize if you need to future-proof 
3. data
3. Try to fetech data in a single query
4. Embed dependent fields
5. Embed "point-in-time" data
6. Do not embed fields that have unbound growth
7. Pre-populate anything you can
8. Preallocate space, whenever possible
9. Store embedded information in arrays for anonymous access
10. Desigin documents to be self-sufficient
11. Prefer $-operators to JavaScript
12. Compute aggregations as you go
13. Write code to handle data integrity issues
14. Use the correct types
15. Override _id when you have your own simple, unique id
16. Avoid using a document for _id
17. Do not use database references
18. Don't use GridFS for small binary data
19. Handle "seamless" failover
20. Handle replica set failure and failover
21. Minimize disk access
22. Use indexes to do more with less memory
23. Don't always use an index
24. Create indexes that cover your queries
25. Use compound indexes to make multiple queries fast
26. Create hierarchical documents for faster scans
27. AND-queries should match as little as possible as fast as possible
28. OR-queries should match as much as possible as soon as possible
29. Write to the journal for single server, replicas for multiserver
30. Always use replication, journaling, or both
31. Do not depend on repair to recover data
32. Understand getlasterror
33. Always use safe writes in development
34. Use w with replication
35. Always use wtimeout with w
36. Don's use fsync on every write
37. Start up normally after a crash
38. Take instant-in-time backups of durable servers
39. Manually clean up your chunks collections
40. Compact database with repair
41. Don't change the number of votes for members of a replic set
42. Replica sets can be reconfigured without a master up
43. --shardsvr and --configsvr aren't required
44. Only use --notablescan in development
45. Learn some JavaScript
46. Manage all of your servers and databases from one shell
47. Get "help" for any function
48. Create startup files
49. Add your own functions
50. Use a single connection to read your own writes

##  推荐资料  

[中文翻译](http://blog.51cto.com/zt/107)



## 扫一扫     

![2014-11-09-50-tips-and-tricks-for-mongodb-developer.md](../../images/share/2014-11-09-50-tips-and-tricks-for-mongodb-developer.md.jpg)