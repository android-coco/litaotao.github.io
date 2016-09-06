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

- Green means everything is good (cluster is fully functional);
- yellow means all data is available but some replicas are not yet allocated (cluster is fully functional); Elasticsearch by default created one replica for index. Since we only have one node running at the moment, that one replica cannot yet be allocated (for high availability) until a later point in time when another node joins the cluster. 
- red means some data is not available for whatever reason;

### 1.5 List All Indexes

```
curl 'localhost:9200/_cat/indices?v'
```

### 1.6 Create an Index

```
curl -XPUT 'localhost:9200/customer?pretty'
curl 'localhost:9200/_cat/indices?v'
```

### 1.7 Index and Query a Document

```
curl -XPUT 'localhost:9200/customer/external/1?pretty' -d '
{
  "name": "John Doe"
}'
```

### 1.8 Delete an Index

```
curl -XDELETE 'localhost:9200/customer?pretty'
curl 'localhost:9200/_cat/indices?v'
```

### 1.9 Modifying Your Data

Elasticsearch provides data manipulation and search capabilities in near real time.

- PUT 相同ID会实现替换操作；PUT 新ID会生成一个新的索引文档；POST 不加ID会自动产生一个随机ID；

### 1.10 Updating Documents

```
curl -XPOST 'localhost:9200/customer/external/1/_update?pretty' -d '
{
  "doc": { "name": "Jane Doe" }
}'
```

- Updates can also be performed by using simple scripts. 

```
curl -XPOST 'localhost:9200/customer/external/1/_update?pretty' -d '
{
  "script" : "ctx._source.age += 5"
}'
```

### 1.11 Deleting Documents

```
curl -XDELETE 'localhost:9200/customer/external/2?pretty'
```

- We also have the ability to delete multiple documents that match a query condition. This example shows how to delete all customers whose names contain "John":

```
curl -XDELETE 'localhost:9200/customer/external/_query?pretty' -d '
{
  "query": { "match": { "name": "John" } }
}'
```

### 1.12 Batch Processing

- In addition to being able to index, update, and delete individual documents, Elasticsearch also provides the ability to perform any of the above operations in batches using the _bulk API.

### 1.13 Exploring Your Data

- generated json data from www.json-generator.com 
- loading and upload the dataset

```
curl -XPOST 'localhost:9200/bank/account/_bulk?pretty' --data-binary @accounts.json
curl 'localhost:9200/_cat/indices?v'
```

### 1.14 The Search API

There are two basic ways to run searches: 
- one is by sending search parameters through the REST request URI;
- the other by sending them through the[REST request body. The request body method allows you to be more expressive and also to define your searches in a more readable JSON format.

```
curl 'localhost:9200/bank/_search?q=*&pretty'
{
  "took" : 63,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "failed" : 0
  },
  "hits" : {
    "total" : 1000,
    "max_score" : 1.0,
    "hits" : [ {
      "_index" : "bank",
      "_type" : "account",
      "_id" : "1",
      "_score" : 1.0, "_source" : {"account_number":1,"balance":39225,"firstname":"Amber","lastname":"Duke","age":32,"gender":"M","address":"880 Holmes Lane","employer":"Pyrami","email":"amberduke@pyrami.com","city":"Brogan","state":"IL"}
    }, {
      "_index" : "bank",
      "_type" : "account",
      "_id" : "6",
      "_score" : 1.0, "_source" : {"account_number":6,"balance":5686,"firstname":"Hattie","lastname":"Bond","age":36,"gender":"M","address":"671 Bristol Street","employer":"Netagy","email":"hattiebond@netagy.com","city":"Dante","state":"TN"}
    }, {
      "_index" : "bank",
      "_type" : "account",
      ...
```

We are searching (_search endpoint) in the bank index, and the q=* parameter instructs Elasticsearch to match all documents in the index. The pretty parameter, again, just tells Elasticsearch to return pretty-printed JSON results.

As for the response, we see the following parts:

- took : time in milliseconds for Elasticsearch to execute the search
- timed_out : tells us if the search timed out or not
- _shards : tells us how many shards were searched, as well as a count of the successful/failed searched shards
- hits : search results
- hits.total : total number of documents matching our search criteria
- hits.hits : actual array of search results (defaults to first 10 documents)
- _score and max_score : ignore these fields for now

Here is the same exact search above using the alternative request body method:
The difference here is that instead of passing q=* in the URI, we POST a JSON-style query request body to the _search API. We’ll discuss this JSON query in the next section.

```
curl -XPOST 'localhost:9200/bank/_search?pretty' -d '
{
  "query": { "match_all": {} }
}'
```

### 1.15 Introducing the Query Language

Elasticsearch provides a JSON-style domain-specific language that you can use to execute queries. This is referred to as the Query DSL.

some e.g.s:

```
curl -XPOST 'localhost:9200/bank/_search?pretty' -d '
{
  "query": { "match_all": {} },
  "size": 1
}'
curl -XPOST 'localhost:9200/bank/_search?pretty' -d '
{
  "query": { "match_all": {} },
  "from": 10,
  "size": 10
}'
curl -XPOST 'localhost:9200/bank/_search?pretty' -d '
{
  "query": { "match_all": {} },
  "sort": { "balance": { "order": "desc" } }
}'
```

### 1.16 Executing Searches

- This example shows how to return two fields, account_number and balance (inside of _source), from the search:

```
curl -XPOST 'localhost:9200/bank/_search?pretty' -d '
{
  "query": { "match_all": {} },
  "_source": ["account_number", "balance"]
}'
```

- This example returns the account numbered 20:

```
curl -XPOST 'localhost:9200/bank/_search?pretty' -d '
{
  "query": { "match": { "account_number": 20 } }
}'
```

- This example returns all accounts containing the term "mill" or "lane" in the address:

```
curl -XPOST 'localhost:9200/bank/_search?pretty' -d '
{
  "query": { "match": { "address": "mill lane" } }
}'
```

- This example is a variant of match (match_phrase) that returns all accounts containing the phrase "mill lane" in the address:

```
curl -XPOST 'localhost:9200/bank/_search?pretty' -d '
{
  "query": { "match_phrase": { "address": "mill lane" } }
}'
```

- The bool query allows us to compose smaller queries into bigger queries using boolean logic.

```
curl -XPOST 'localhost:9200/bank/_search?pretty' -d '
{
  "query": {
    "bool": {
      "must": [
        { "match": { "address": "mill" } },
        { "match": { "address": "lane" } }
      ]
    }
  }
}'
```

- In contrast, this example composes two match queries and returns all accounts containing "mill" or "lane" in the address:

```
curl -XPOST 'localhost:9200/bank/_search?pretty' -d '
{
  "query": {
    "bool": {
      "should": [
        { "match": { "address": "mill" } },
        { "match": { "address": "lane" } }
      ]
    }
  }
}'
```

- This example composes two match queries and returns all accounts that contain neither "mill" nor "lane" in the address:

```
curl -XPOST 'localhost:9200/bank/_search?pretty' -d '
{
  "query": {
    "bool": {
      "must_not": [
        { "match": { "address": "mill" } },
        { "match": { "address": "lane" } }
      ]
    }
  }
}'
```

- This example returns all accounts of anybody who is 40 years old but don’t live in ID(aho):

```
curl -XPOST 'localhost:9200/bank/_search?pretty' -d '
{
  "query": {
    "bool": {
      "must": [
        { "match": { "age": "40" } }
      ],
      "must_not": [
        { "match": { "state": "ID" } }
      ]
    }
  }
}'
```

### 1.16 Executing Filters

All queries in Elasticsearch trigger computation of the relevance scores. In cases where we do not need the relevance scores, Elasticsearch provides another query capability in the form of <query-dsl-filters,filters>. Filters are similar in concept to queries except that they are optimized for much faster execution speeds for two primary reasons:

- Filters do not score so they are faster to execute than queries;
- Filters can be cached in memory allowing repeated search executions to be significantly faster than queries

- This example uses a filtered query to return all accounts with balances between 20000 and 30000, inclusive. In other words, we want to find accounts with a balance that is greater than or equal to 20000 and less than or equal to 30000:

```
curl -XPOST 'localhost:9200/bank/_search?pretty' -d '
{
  "query": {
    "filtered": {
      "query": { "match_all": {} },
      "filter": {
        "range": {
          "balance": {
            "gte": 20000,
            "lte": 30000
          }
        }
      }
    }
  }
}'
```

### 1.17 Executing Aggregations

Aggregations provide the ability to group and extract statistics from your data. The easiest way to think about aggregations is by roughly equating it to the SQL GROUP BY and the SQL aggregate functions. 

- To start with, this example groups all the accounts by state, and then returns the top 10 (default) states sorted by count descending (also default), same to `SELECT COUNT(*) from bank GROUP BY state ORDER BY COUNT(*) DESC` in SQL:

```
curl -XPOST 'localhost:9200/bank/_search?pretty' -d '
{
  "size": 0,
  "aggs": {
    "group_by_state": {
      "terms": {
        "field": "state"
      }
    }
  }
}'
```

- Building on the previous aggregation, this example calculates the average account balance by state (again only for the top 10 states sorted by count in descending order):

```
curl -XPOST 'localhost:9200/bank/_search?pretty' -d '
{
  "size": 0,
  "aggs": {
    "group_by_state": {
      "terms": {
        "field": "state"
      },
      "aggs": {
        "average_balance": {
          "avg": {
            "field": "balance"
          }
        }
      }
    }
  }
}'
```

- Building on the previous aggregation, let’s now sort on the average balance in descending order:

```
curl -XPOST 'localhost:9200/bank/_search?pretty' -d '
{
  "size": 0,
  "aggs": {
    "group_by_state": {
      "terms": {
        "field": "state",
        "order": {
          "average_balance": "desc"
        }
      },
      "aggs": {
        "average_balance": {
          "avg": {
            "field": "balance"
          }
        }
      }
    }
  }
}'
```

- This example demonstrates how we can group by age brackets (ages 20-29, 30-39, and 40-49), then by gender, and then finally get the average account balance, per age bracket, per gender:

```
curl -XPOST 'localhost:9200/bank/_search?pretty' -d '
{
  "size": 0,
  "aggs": {
    "group_by_age": {
      "range": {
        "field": "age",
        "ranges": [
          {
            "from": 20,
            "to": 30
          },
          {
            "from": 30,
            "to": 40
          },
          {
            "from": 40,
            "to": 50
          }
        ]
      },
      "aggs": {
        "group_by_gender": {
          "terms": {
            "field": "gender"
          },
          "aggs": {
            "average_balance": {
              "avg": {
                "field": "balance"
              }
            }
          }
        }
      }
    }
  }
}'
```

## 2. Setup

Elasticsearch is built using Java, and requires at least Java 7 in order to run. We recommend installing the Java 8 update 20 or later, or Java 7 update 55 or later. 

### 2.1 Configuration

- Environment Variables
    + Elasticsearch comes with built in JAVA_OPTS passed to the JVM started. 
    + Most times it is better to leave the default JAVA_OPTS as they are, and use the ES_JAVA_OPTS environment variable in order to set / change JVM settings or arguments.
    + The ES_HEAP_SIZE environment variable allows to set the heap memory that will be allocated to elasticsearch java process.
- System Configuration
    + In order to test how many open files the process can open, start it with -Des.max-open-files set to true. This will print the number of open files the process can open on startup.
    + retrieve the max_file_descriptors for each node using the Nodes Info API using `curl localhost:9200/_nodes/process?pretty`
- Virtual memory:
    + Elasticsearch uses a hybrid mmapfs / niofs directory by default to store its indices.
- Memory Settings:
- Elasticsearch Settings:
- Index Settings:
- Logging:

### 2.2 Directory Layout

- home: Home of elasticsearch installation;
- bin: Binary scripts including elasticsearch to start a node;
- conf: Configuration files including elasticsearch.yml;
- data: The location of the data files of each index / shard allocated on the node. Can hold multiple locations;
- logs: Log files location;
- plugins: Plugin files location. Each plugin will be contained in a subdirectory.

## 3. Document APIs

### 3.1 Single documents APIs - Index API

The index API adds or updates a typed JSON document in a specific index, making it searchable. 

### 3.2 Single documents APIs - Get API

The get API allows to get a typed JSON document from the index based on its id. 

- readtime;
- optional type;
- source filtering

```
curl -XGET 'http://localhost:9200/twitter/tweet/1?_source=false
```



```
```


```
```

```
```


```
```



```
```


```
```



```
```


```
```






## 扫一扫     

![2015-03-30-learning-elasticsearch.md](../../images/share/2015-03-30-learning-elasticsearch.md.jpg)