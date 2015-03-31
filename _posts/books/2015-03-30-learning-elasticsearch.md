---
category: books
published: false
layout: post
title: book-5. Learning ElasticSearch
description: 仅仅是记录我个人的读书记录，看官不必在意～
---

## 
## 1. Getting Started 

- Elasticsearch is a highly scalable open-source full-text search and analytics engine. It allows you to store, search, and analyze big volumes of data quickly and in near real time. It is generally used as the underlying engine/technology that powers applications that have complex search features and requirements.
- Can be used for:
    + search and autocomplete suggestions;
    + analyze and mine log info using Elasticsearch/Logstash/Kibana stack;
    + alerting platform;
    + analytics/business-intelligence and quickly investigate, analyze, visualize, and ask ad-hoc questions on a lot of data using Elasticsearch/Logstash/Kibana stack;

### 1.1 Basic Concepts:

+ NRT(Near Realtime)
+ Cluster
+ Node
+ Index: An index is a collection of documents that have somewhat similar characteristics. [same to database name in SQL];
+ Type: Within an index, you can define one or more types. A type is a logical category/partition of your index whose semantics is completely up to you. [same to tables in SQL];
+ Document: A document is a basic unit of information that can be indexed. [same to column in SQL];
+ Shards & Replicas: An index can potentially store a large amount of data that can exceed the hardware limits of a single node. Elasticsearch provides the ability to subdivide your index into multiple pieces called shards. 
    * Sharding is important for two primary reasons:
        - allows you to horizontally split/scale your content volume
        - allows you distribute and parallelize operations across shards (potentially on multiple nodes) thus increasing performance/throughput
    * Replication is important for two primary reasons:
        - provides high availability in case a shard/node fails.
        - allows you to scale out your search volume/throughput since searches can be executed on all replicas in parallel
    
### 1.2 Installation
Elasticsearch requires Java 7. Specifically as of this writing, it is recommended that you use the Oracle JDK version 1.8.0_25.

### 1.3 The Rest API
- Check your cluster, node, and index health, status, and statistics
Administer your cluster, node, and index data and metadata;
- Perform CRUD (Create, Read, Update, and Delete) and search operations against your indexes;
- Execute advanced search operations such as paging, sorting, filtering, scripting, faceting, aggregations, and many others;

### 1.4 Cluster Health

```
curl 'localhost:9200/_cat/health?v'
```

### 1.5 List All Indexes

```
curl 'localhost:9200/_cat/indices?v'
```