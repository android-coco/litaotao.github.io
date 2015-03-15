---
category: books
published: false
layout: post
title: spark专刊笔记之：Spark与MPI
description: 仅仅是记录我个人的读书记录，看官不必在意～
---

## 
## 1. sparkSQL发展历程
sparksql的前身是shark。在hadoop的发展中，为了给熟悉RDBMS但又不理解mapreduce的人提供工具，hive应运而生，是当时唯一运行在hadoop上的sql工具。但是，mr的计算过程中大量的中间磁盘落地过程消耗了大量io，降低运行效率，为了提高hive效率，大量的工具开始诞生：

- mapr的drill
- cloudera的impala
- shark

其中shark是spark组件之一，它修改了内存管理，物理计划，执行三个模块，使之能运行在spark引擎上，从而使得sql查询速度得到10-100倍的提升。
